$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$bootstrap = Join-Path $root 'srcmap\start_build_tohoku_r41.py'
$expectedBytes = 1498
$expectedSha256 = 'F58D45E655BEC48A35DFD9780CFF9066BE71076044FB827BEABB647EFB6DAAFA'
$payload = [System.IO.File]::ReadAllBytes($bootstrap)
if ($payload.Length -ne $expectedBytes) {
    throw "Bootstrap byte count drift: $($payload.Length)"
}
$sha = [System.Security.Cryptography.SHA256]::Create()
try {
    $hashBytes = $sha.ComputeHash($payload)
} finally {
    $sha.Dispose()
}
$actualSha256 = (($hashBytes | ForEach-Object { $_.ToString('X2') }) -join '')
if ($actualSha256 -ne $expectedSha256) {
    throw "Bootstrap SHA-256 drift: $actualSha256"
}
$encoded = [Convert]::ToBase64String($payload)
$runner = @'
import base64
import sys

path = sys.argv[1]
payload = base64.b64decode(sys.argv[2])
namespace = {'__name__': '__main__', '__file__': path}
exec(compile(payload, path, 'exec'), namespace)
'@
$priorEnvelope = $env:TOHOKU_R41_ENVELOPE
try {
    $env:TOHOKU_R41_ENVELOPE = 'tohoku-r41-same-bytes-envelope-v1'
    & python -I -B -c $runner $bootstrap $encoded
    if ($LASTEXITCODE -ne 0) {
        throw "Tohoku r41 mapping bootstrap failed with exit code $LASTEXITCODE"
    }
} finally {
    if ($null -eq $priorEnvelope) {
        Remove-Item Env:TOHOKU_R41_ENVELOPE -ErrorAction SilentlyContinue
    } else {
        $env:TOHOKU_R41_ENVELOPE = $priorEnvelope
    }
}
