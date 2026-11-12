$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$bootstrap = Join-Path $root 'srcmap\start_build_tohoku_r37.py'
$expectedBytes = 1498
$expectedSha256 = '022BBFC7C05792F0401CB33F72A0FEBBFCDD6447ED018D1E6B64D7FA81B2A46E'
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
$priorEnvelope = $env:TOHOKU_R37_ENVELOPE
try {
    $env:TOHOKU_R37_ENVELOPE = 'tohoku-r37-same-bytes-envelope-v1'
    & python -I -B -c $runner $bootstrap $encoded
    if ($LASTEXITCODE -ne 0) {
        throw "Tohoku r37 mapping bootstrap failed with exit code $LASTEXITCODE"
    }
} finally {
    if ($null -eq $priorEnvelope) {
        Remove-Item Env:TOHOKU_R37_ENVELOPE -ErrorAction SilentlyContinue
    } else {
        $env:TOHOKU_R37_ENVELOPE = $priorEnvelope
    }
}
