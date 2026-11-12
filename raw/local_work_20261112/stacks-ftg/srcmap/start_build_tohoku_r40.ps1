$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$bootstrap = Join-Path $root 'srcmap\start_build_tohoku_r40.py'
$expectedBytes = 1498
$expectedSha256 = '20273ABF13401162111785E41DB42B23A0BB7DD23A45233FEF4F2FC9992463B2'
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
$priorEnvelope = $env:TOHOKU_R40_ENVELOPE
try {
    $env:TOHOKU_R40_ENVELOPE = 'tohoku-r40-same-bytes-envelope-v1'
    & python -I -B -c $runner $bootstrap $encoded
    if ($LASTEXITCODE -ne 0) {
        throw "Tohoku r40 mapping bootstrap failed with exit code $LASTEXITCODE"
    }
} finally {
    if ($null -eq $priorEnvelope) {
        Remove-Item Env:TOHOKU_R40_ENVELOPE -ErrorAction SilentlyContinue
    } else {
        $env:TOHOKU_R40_ENVELOPE = $priorEnvelope
    }
}
