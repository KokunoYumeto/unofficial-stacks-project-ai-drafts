$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$bootstrap = Join-Path $root 'srcmap\start_build_tohoku_r18.py'
$expectedBytes = 1330
$expectedSha256 = '33FDA531403C1FB9CAD3B8B6C01B1614CF71F889C7792075E42A513006F23C5C'
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
    throw "Tohoku r18 mapping bootstrap failed with exit code $LASTEXITCODE"
}
