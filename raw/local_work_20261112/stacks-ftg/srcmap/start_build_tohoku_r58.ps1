$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$driver = $MyInvocation.MyCommand.Path
$bootstrap = Join-Path $root 'srcmap\start_build_tohoku_r58.py'
$python = 'user\miniconda3\python.exe'
function Hash([byte[]]$bytes) {
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try { return (($sha.ComputeHash($bytes) | ForEach-Object { $_.ToString('X2') }) -join '') }
    finally { $sha.Dispose() }
}
$driverPayload = [System.IO.File]::ReadAllBytes($driver)
$driverAttestation = [ordered]@{ path='srcmap/start_build_tohoku_r58.ps1'; bytes=$driverPayload.Length; sha256=(Hash $driverPayload); contract='self_read_hash_then_one_shot_bootstrap_envelope' } | ConvertTo-Json -Compress
$bootstrapPayload = [System.IO.File]::ReadAllBytes($bootstrap)
$bootstrapSha = Hash $bootstrapPayload
$encoded = [Convert]::ToBase64String($bootstrapPayload)
$runner = @'
import base64,hashlib,sys
path=sys.argv[1]; payload=base64.b64decode(sys.argv[2]); expected=int(sys.argv[3]); sha=sys.argv[4]
if len(payload)!=expected or hashlib.sha256(payload).hexdigest().upper()!=sha: raise RuntimeError("bootstrap payload drift")
ns={'__name__':'__main__','__file__':path,'BOOTSTRAP_ATTESTATION':{'path':'srcmap/start_build_tohoku_r58.py','bytes':len(payload),'sha256':sha}}
exec(compile(payload,path,'exec'),ns)
'@
$runnerEncoded = [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($runner))
$priorEnvelope=$env:TOHOKU_R58_ENVELOPE; $priorDriver=$env:TOHOKU_R58_DRIVER_ATTESTATION
try {
    $env:TOHOKU_R58_ENVELOPE='tohoku-r58-one-shot-envelope-v1'
    $env:TOHOKU_R58_DRIVER_ATTESTATION=$driverAttestation
    & $python -I -B -c 'import base64,sys;exec(base64.b64decode(sys.argv.pop(1)))' $runnerEncoded $bootstrap $encoded $bootstrapPayload.Length $bootstrapSha
    if ($LASTEXITCODE -ne 0) { throw "Tohoku r58 bootstrap failed with exit code $LASTEXITCODE" }
} finally {
    if ($null -eq $priorEnvelope) { Remove-Item Env:TOHOKU_R58_ENVELOPE -ErrorAction SilentlyContinue } else { $env:TOHOKU_R58_ENVELOPE=$priorEnvelope }
    if ($null -eq $priorDriver) { Remove-Item Env:TOHOKU_R58_DRIVER_ATTESTATION -ErrorAction SilentlyContinue } else { $env:TOHOKU_R58_DRIVER_ATTESTATION=$priorDriver }
}
