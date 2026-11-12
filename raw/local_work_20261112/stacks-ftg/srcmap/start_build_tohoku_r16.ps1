$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$bootstrap = Join-Path $root 'srcmap\start_build_tohoku_r16.py'
$expectedBytes = 1330
$expectedSha256 = 'F1F3B9C8DC37A3990D2A7C86BE16608354343DB684F81D8A29DD088CA9CAC2A5'
$item = Get-Item -LiteralPath $bootstrap
if ($item.Length -ne $expectedBytes) {
    throw "Bootstrap byte count drift: $($item.Length)"
}
$actualSha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $bootstrap).Hash
if ($actualSha256 -ne $expectedSha256) {
    throw "Bootstrap SHA-256 drift: $actualSha256"
}
& python -I -B $bootstrap
if ($LASTEXITCODE -ne 0) {
    throw "Tohoku r16 mapping bootstrap failed with exit code $LASTEXITCODE"
}
