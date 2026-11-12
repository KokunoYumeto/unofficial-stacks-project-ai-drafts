$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$driver = $MyInvocation.MyCommand.Path
$bootstrap = Join-Path $root 'srcmap\start_build_tohoku_r42.py'
$expectedBootstrapBytes = 3751
$expectedBootstrapSha256 = '387E27E4B9100809F1784AE1E94214790A318DF5F89D7E3D4F766B6CD6B676F5'

$driverPayload = [System.IO.File]::ReadAllBytes($driver)
$sha = [System.Security.Cryptography.SHA256]::Create()
try {
    $driverHashBytes = $sha.ComputeHash($driverPayload)
} finally {
    $sha.Dispose()
}
$driverSha256 = (($driverHashBytes | ForEach-Object { $_.ToString('X2') }) -join '')
$driverAttestation = [ordered]@{
    path = 'srcmap/start_build_tohoku_r42.ps1'
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
        'path': 'srcmap/start_build_tohoku_r42.py',
        'bytes': len(payload),
        'sha256': actual_sha256,
    },
}
exec(compile(payload, path, 'exec'), namespace)
'@

$priorEnvelope = $env:TOHOKU_R42_ENVELOPE
$priorDriverAttestation = $env:TOHOKU_R42_DRIVER_ATTESTATION
try {
    $env:TOHOKU_R42_ENVELOPE = 'tohoku-r42-one-shot-envelope-v1'
    $env:TOHOKU_R42_DRIVER_ATTESTATION = $driverAttestation
    & python -I -B -c $runner $bootstrap $encoded $expectedBootstrapBytes $expectedBootstrapSha256
    if ($LASTEXITCODE -ne 0) {
        throw "Tohoku r42 mapping bootstrap failed with exit code $LASTEXITCODE"
    }
} finally {
    if ($null -eq $priorEnvelope) {
        Remove-Item Env:TOHOKU_R42_ENVELOPE -ErrorAction SilentlyContinue
    } else {
        $env:TOHOKU_R42_ENVELOPE = $priorEnvelope
    }
    if ($null -eq $priorDriverAttestation) {
        Remove-Item Env:TOHOKU_R42_DRIVER_ATTESTATION -ErrorAction SilentlyContinue
    } else {
        $env:TOHOKU_R42_DRIVER_ATTESTATION = $priorDriverAttestation
    }
}
