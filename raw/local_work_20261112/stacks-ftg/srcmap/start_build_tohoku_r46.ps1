$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$driver = $MyInvocation.MyCommand.Path
$bootstrap = Join-Path $root 'srcmap\start_build_tohoku_r46.py'
$python = 'user\miniconda3\python.exe'
$expectedPythonBytes = 104264
$expectedPythonSha256 = '7679E53FA969789309E81FDAD0D52B8CDA5F83C9ABF7CB31A3C58BF24B31E264'
$expectedPythonVersion = '3.13.9'
$expectedBootstrapBytes = 3842
$expectedBootstrapSha256 = 'F7C78341132D2A3AC8F8834467241FA68D1623E4EDA9DAF345034608C35FEEC3'

$driverPayload = [System.IO.File]::ReadAllBytes($driver)
$sha = [System.Security.Cryptography.SHA256]::Create()
try {
    $driverHashBytes = $sha.ComputeHash($driverPayload)
} finally {
    $sha.Dispose()
}
$driverSha256 = (($driverHashBytes | ForEach-Object { $_.ToString('X2') }) -join '')
$driverAttestation = [ordered]@{
    path = 'srcmap/start_build_tohoku_r46.ps1'
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
        'path': 'srcmap/start_build_tohoku_r46.py',
        'bytes': len(payload),
        'sha256': actual_sha256,
    },
}
exec(compile(payload, path, 'exec'), namespace)
'@

$priorEnvelope = $env:TOHOKU_R46_ENVELOPE
$priorDriverAttestation = $env:TOHOKU_R46_DRIVER_ATTESTATION
try {
    $env:TOHOKU_R46_ENVELOPE = 'tohoku-r46-one-shot-envelope-v1'
    $env:TOHOKU_R46_DRIVER_ATTESTATION = $driverAttestation
    & $python -I -B -c $runner $bootstrap $encoded $expectedBootstrapBytes $expectedBootstrapSha256
    if ($LASTEXITCODE -ne 0) {
        throw "Tohoku r46 mapping bootstrap failed with exit code $LASTEXITCODE"
    }
} finally {
    if ($null -eq $priorEnvelope) {
        Remove-Item Env:TOHOKU_R46_ENVELOPE -ErrorAction SilentlyContinue
    } else {
        $env:TOHOKU_R46_ENVELOPE = $priorEnvelope
    }
    if ($null -eq $priorDriverAttestation) {
        Remove-Item Env:TOHOKU_R46_DRIVER_ATTESTATION -ErrorAction SilentlyContinue
    } else {
        $env:TOHOKU_R46_DRIVER_ATTESTATION = $priorDriverAttestation
    }
}
