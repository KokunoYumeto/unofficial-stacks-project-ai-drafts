param(
    [Parameter(Mandatory = $true)][string]$UpstreamRoot,
    [Parameter(Mandatory = $true)][string]$WorkRoot1,
    [Parameter(Mandatory = $true)][string]$WorkRoot2,
    [Parameter(Mandatory = $true)][string]$PrivateRoot1,
    [Parameter(Mandatory = $true)][string]$PrivateRoot2,
    [Parameter(Mandatory = $true)][string]$GuardLogRoot,
    [string]$Python = 'python',
    [ValidateRange(1,86400)][int]$CommandTimeoutSeconds = 7200
)

$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
$configPath = Join-Path $root 'candidate.config.json'
if (-not (Test-Path -LiteralPath $configPath -PathType Leaf)) { throw 'Copy this wrapper and its C# guard to the actual candidate root before execution.' }
$config = Get-Content -LiteralPath $configPath -Raw | ConvertFrom-Json
if ($config.candidate_id -ne 'stacks-errata-a04446e-r48') { throw 'Unexpected candidate identity.' }
$pythonCommand = Get-Command $Python -CommandType Application -ErrorAction Stop | Select-Object -First 1
$pythonExe = $pythonCommand.Source
if (-not [IO.Path]::IsPathRooted($pythonExe)) { throw 'Python must resolve to an executable file.' }
$guardSource = Join-Path $root 'CapturedR48Tree20260910.cs'
if ('CapturedR48Tree20260910' -as [type]) { throw 'Use a fresh PowerShell process so the guard source cannot be shadowed by a loaded type.' }
Add-Type -Path $guardSource
$receiptPath = Join-Path $root 'builds\TEX_MUTEX_RECEIPT.json'
if (Test-Path -LiteralPath $receiptPath) { throw 'Existing mutex receipt must be preserved; use a new recorded build attempt.' }
$guardPath = [IO.Path]::GetFullPath($GuardLogRoot)
$newPaths = @($WorkRoot1, $WorkRoot2, $PrivateRoot1, $PrivateRoot2, $guardPath) | ForEach-Object { [IO.Path]::GetFullPath($_).TrimEnd('\') }
if (($newPaths | Select-Object -Unique).Count -ne 5) { throw 'All work, private evidence, and guard-log directories must be distinct.' }
foreach ($path in $newPaths) {
    if (Test-Path -LiteralPath $path) { throw "Build, private and guard roots must be new and absent: $path" }
    foreach ($other in $newPaths) { if ($path.StartsWith($other + '\', [StringComparison]::OrdinalIgnoreCase)) { throw 'New evidence/work roots must not contain one another.' } }
}
foreach ($protected in @([IO.Path]::GetFullPath($root).TrimEnd('\'), [IO.Path]::GetFullPath($UpstreamRoot).TrimEnd('\'))) {
    if ($guardPath -eq $protected -or $guardPath.StartsWith($protected + '\', [StringComparison]::OrdinalIgnoreCase)) { throw 'Raw guard logs must stay outside candidate and upstream.' }
}
if (-not (Test-Path -LiteralPath $UpstreamRoot -PathType Container)) { throw 'Pinned upstream root missing.' }
[IO.Directory]::CreateDirectory($guardPath) | Out-Null
$mutexName = 'Global\InterlanguageTeXSlotV1'
$waitSeconds = 60
$texMutex = [Threading.Mutex]::new($false, $mutexName)
$held = $false
$failure = $null
$script:activeTree = $null
$receipt = [ordered]@{
    schema='stacks-r48-tex-mutex-execution/v1'; candidate_id=$config.candidate_id
    mutex_name=$mutexName; wait_timeout_seconds=$waitSeconds
    acquisition_started_at_utc=[DateTime]::UtcNow.ToString('o'); acquired=$false; acquired_at_utc=$null
    abandoned_mutex_recovered=$false; holder_pid=$PID; guarded_commands=@()
    captured_tree_guard=[ordered]@{path='CapturedR48Tree20260910.cs'; sha256=(Get-FileHash -LiteralPath $guardSource -Algorithm SHA256).Hash; mechanism='CREATE_SUSPENDED -> unnamed KILL_ON_JOB_CLOSE Job Object -> resume'; breakaway_allowed=$false}
    command_timeout_seconds=$CommandTimeoutSeconds; released=$false; released_at_utc=$null; passed=$false; failure=$null
}

function Save-Receipt {
    [IO.Directory]::CreateDirectory((Split-Path -Parent $receiptPath)) | Out-Null
    [IO.File]::WriteAllText($receiptPath, (($receipt | ConvertTo-Json -Depth 12) + "`n"), [Text.UTF8Encoding]::new($false))
}
function Public-FailureText {
    param([string]$Message)
    $profilePath=[Environment]::GetFolderPath('UserProfile')
    if ($profilePath) { return $Message.Replace($profilePath, '<USER_ROOT>').Replace($profilePath.Replace('\','/'), '<USER_ROOT>') }
    return $Message
}
function Close-CapturedTree {
    if ($null -ne $script:activeTree) {
        # This call ends only after every process in this captured job has terminated.
        $script:activeTree.Dispose()
        if (-not $script:activeTree.CleanupCompleted) { throw 'Captured tree cleanup was not confirmed; mutex must remain held.' }
    }
}
function Invoke-CapturedPython {
    param([string]$Role, [string[]]$Arguments, [bool]$RecordMutexCommand = $true)
    $outPath=Join-Path $guardPath ($Role + '.stdout.txt')
    $errPath=Join-Path $guardPath ($Role + '.stderr.txt')
    $row=[ordered]@{role=$Role; started_at_utc=[DateTime]::UtcNow.ToString('o'); exit_code=$null; root_pid=$null; assigned_before_resume=$false; captured_total_processes=0; root_exited_before_tree=$false; cleanup_completed=$false; termination_requested=$false; failure=$null}
    if ($RecordMutexCommand) { $receipt.guarded_commands += $row; Save-Receipt }
    try {
        $script:activeTree=[CapturedR48Tree20260910]::new($pythonExe, [string[]](@('-B') + $Arguments), $root, $outPath, $errPath)
        $row.root_pid=$script:activeTree.Id
        $row.assigned_before_resume=$script:activeTree.AssignedBeforeResume
        $watch=[Diagnostics.Stopwatch]::StartNew()
        while (-not $script:activeTree.WaitForExit(250)) {
            if ($script:activeTree.RootHasExited) {
                $row.root_exited_before_tree=$true
                $row.exit_code=$script:activeTree.ExitCode
                if ($row.exit_code -ne 0) { throw "$Role root failed with exit code $($row.exit_code); remaining captured descendants will be terminated." }
            }
            if ($watch.Elapsed.TotalSeconds -ge $CommandTimeoutSeconds) { throw "$Role exceeded the bounded command timeout." }
        }
        $row.exit_code=$script:activeTree.ExitCode
        if ($row.exit_code -ne 0) { throw "$Role failed with exit code $($row.exit_code)" }
    } catch {
        $row.failure=Public-FailureText $_.Exception.Message
        throw
    } finally {
        Close-CapturedTree
        if ($null -ne $script:activeTree) {
            $row.captured_total_processes=$script:activeTree.FinalTotalProcesses
            $row.cleanup_completed=$script:activeTree.CleanupCompleted
            $row.termination_requested=$script:activeTree.TerminationRequested
            $script:activeTree=$null
        }
        $row.completed_at_utc=[DateTime]::UtcNow.ToString('o')
        foreach ($pair in @(@('stdout',$outPath),@('stderr',$errPath))) {
            if (Test-Path -LiteralPath $pair[1] -PathType Leaf) { $row[$pair[0]]=[ordered]@{private_filename=[IO.Path]::GetFileName($pair[1]); bytes=(Get-Item -LiteralPath $pair[1]).Length; sha256=(Get-FileHash -LiteralPath $pair[1] -Algorithm SHA256).Hash} }
        }
        if ($RecordMutexCommand) { Save-Receipt }
        else { [IO.File]::WriteAllText((Join-Path $guardPath 'POST_RELEASE_BINDING.json'), (($row | ConvertTo-Json -Depth 8) + "`n"), [Text.UTF8Encoding]::new($false)) }
    }
}

Save-Receipt
try {
    try { $held=$texMutex.WaitOne([TimeSpan]::FromSeconds($waitSeconds)) }
    catch [Threading.AbandonedMutexException] { $held=$true; $receipt.abandoned_mutex_recovered=$true }
    if (-not $held) { throw 'Bounded TeX mutex acquisition timed out; no build worker was started.' }
    $receipt.acquired=$true; $receipt.acquired_at_utc=[DateTime]::UtcNow.ToString('o'); Save-Receipt
    Invoke-CapturedPython 'fresh_candidate_authority_build_1' @((Join-Path $root 'replay-build.py'),'--upstream-root',$UpstreamRoot,'--work-root',$WorkRoot1,'--private-evidence-root',$PrivateRoot1)
    Invoke-CapturedPython 'fresh_candidate_authority_build_2' @((Join-Path $root 'replay-build.py'),'--upstream-root',$UpstreamRoot,'--work-root',$WorkRoot2,'--private-evidence-root',$PrivateRoot2)
    Invoke-CapturedPython 'deterministic_pdf_comparison' @((Join-Path $root 'deterministic-replay.py'),'--first-private-build-root',$PrivateRoot1)
    Invoke-CapturedPython 'immediate_log_and_build_preflight' @((Join-Path $root 'build-receipt.py'),'--preflight')
} catch {
    $failure=$_; $receipt.failure=Public-FailureText $_.Exception.Message
} finally {
    # Never release/dispose the mutex while this reference still denotes an uncleaned job.
    Close-CapturedTree
    if ($held) {
        $texMutex.ReleaseMutex(); $held=$false
        $receipt.released=$true; $receipt.released_at_utc=[DateTime]::UtcNow.ToString('o')
    }
    $texMutex.Dispose()
    $receipt.passed=($null -eq $failure -and $receipt.acquired -and $receipt.released -and $receipt.guarded_commands.Count -eq 4)
    Save-Receipt
}
if ($null -ne $failure) { throw $failure }
# This inspected child performs no TeX: it binds the now-final released mutex receipt.
# Capture it too, but do not change the already hash-bound mutex receipt afterward.
Invoke-CapturedPython 'post_release_receipt_binding' @((Join-Path $root 'build-receipt.py')) $false
Write-Output (([ordered]@{passed=$true; mutex=$mutexName; receipt=$receiptPath; captured_tree_guard=$true} | ConvertTo-Json -Compress))
