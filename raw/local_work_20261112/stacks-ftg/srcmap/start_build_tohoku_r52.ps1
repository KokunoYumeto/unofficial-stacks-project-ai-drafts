$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$driver = $MyInvocation.MyCommand.Path
$bootstrap = Join-Path $root 'srcmap\start_build_tohoku_r52.py'
$python = 'user\miniconda3\python.exe'
$expectedPythonBytes = 104264
$expectedPythonSha256 = '7679E53FA969789309E81FDAD0D52B8CDA5F83C9ABF7CB31A3C58BF24B31E264'
$expectedPythonVersion = '3.13.9'
$expectedBootstrapBytes = 3751
$expectedBootstrapSha256 = '1AE0730919281BF49D61905EA9DF8BC6744FEE0B45E956FC57C8D29279018553'

$driverPayload = [System.IO.File]::ReadAllBytes($driver)
$sha = [System.Security.Cryptography.SHA256]::Create()
try {
    $driverHashBytes = $sha.ComputeHash($driverPayload)
} finally {
    $sha.Dispose()
}
$driverSha256 = (($driverHashBytes | ForEach-Object { $_.ToString('X2') }) -join '')
$driverAttestation = [ordered]@{
    path = 'srcmap/start_build_tohoku_r52.ps1'
    bytes = $driverPayload.Length
    sha256 = $driverSha256
    contract = 'self_read_hash_then_one_shot_bootstrap_envelope'
} | ConvertTo-Json -Compress

$bootstrapPayload = [System.IO.File]::ReadAllBytes($bootstrap)
if ($bootstrapPayload.Length -ne $expectedBootstrapBytes) {
    throw "Bootstrap byte count drift: $($bootstrapPayload.Length)"
}
$sha = [System.Security.Cryptography.SHA256]::Create()
try {
    $bootstrapHashBytes = $sha.ComputeHash($bootstrapPayload)
} finally {
    $sha.Dispose()
}
$bootstrapSha256 = (($bootstrapHashBytes | ForEach-Object { $_.ToString('X2') }) -join '')
if ($bootstrapSha256 -ne $expectedBootstrapSha256) {
    throw "Bootstrap SHA-256 drift: $bootstrapSha256"
}

$pythonPayload = [System.IO.File]::ReadAllBytes($python)
if ($pythonPayload.Length -ne $expectedPythonBytes) {
    throw "Python byte count drift: $($pythonPayload.Length)"
}
$sha = [System.Security.Cryptography.SHA256]::Create()
try {
    $pythonHashBytes = $sha.ComputeHash($pythonPayload)
} finally {
    $sha.Dispose()
}
$pythonSha256 = (($pythonHashBytes | ForEach-Object { $_.ToString('X2') }) -join '')
if ($pythonSha256 -ne $expectedPythonSha256) {
    throw "Python SHA-256 drift: $pythonSha256"
}
$pythonVersion = [System.Diagnostics.FileVersionInfo]::GetVersionInfo($python).FileVersion
if ($pythonVersion -ne $expectedPythonVersion) {
    throw "Python file version drift: $pythonVersion"
}

$encoded = [Convert]::ToBase64String($bootstrapPayload)
$runner = @'
import base64
import hashlib
import sys

path = sys.argv[1]
payload = base64.b64decode(sys.argv[2])
expected_bytes = int(sys.argv[3])
expected_sha256 = sys.argv[4]
actual_sha256 = hashlib.sha256(payload).hexdigest().upper()
if len(payload) != expected_bytes or actual_sha256 != expected_sha256:
    raise RuntimeError("PowerShell-to-Python bootstrap payload drift")
namespace = {
    '__name__': '__main__',
    '__file__': path,
    'BOOTSTRAP_ATTESTATION': {
        'path': 'srcmap/start_build_tohoku_r52.py',
        'bytes': len(payload),
        'sha256': actual_sha256,
    },
}
exec(compile(payload, path, 'exec'), namespace)
'@
$runnerPayload = [System.Text.Encoding]::UTF8.GetBytes($runner)
$runnerEncoded = [Convert]::ToBase64String($runnerPayload)
$runnerCommand = 'import base64,sys;code=base64.b64decode(sys.argv.pop(1));exec(code)'

$priorEnvelope = $env:TOHOKU_R52_ENVELOPE
$priorDriverAttestation = $env:TOHOKU_R52_DRIVER_ATTESTATION
try {
    $env:TOHOKU_R52_ENVELOPE = 'tohoku-r52-one-shot-envelope-v1'
    $env:TOHOKU_R52_DRIVER_ATTESTATION = $driverAttestation
    & $python -I -B -c $runnerCommand $runnerEncoded $bootstrap $encoded $expectedBootstrapBytes $expectedBootstrapSha256
    if ($LASTEXITCODE -ne 0) {
        throw "Tohoku r52 mapping bootstrap failed with exit code $LASTEXITCODE"
    }
} finally {
    if ($null -eq $priorEnvelope) {
        Remove-Item Env:TOHOKU_R52_ENVELOPE -ErrorAction SilentlyContinue
    } else {
        $env:TOHOKU_R52_ENVELOPE = $priorEnvelope
    }
    if ($null -eq $priorDriverAttestation) {
        Remove-Item Env:TOHOKU_R52_DRIVER_ATTESTATION -ErrorAction SilentlyContinue
    } else {
        $env:TOHOKU_R52_DRIVER_ATTESTATION = $priorDriverAttestation
    }
}
