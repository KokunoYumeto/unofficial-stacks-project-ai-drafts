$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$bootstrap = Join-Path $root 'srcmap\start_build_tohoku_r17.py'
$expectedBytes = 1330
$expectedSha256 = '9CA1716B682819894CB3B36DF34E51F3D82E62CF9AC61423A8328A6EEFBFB6BB'
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
    throw "Tohoku r17 mapping bootstrap failed with exit code $LASTEXITCODE"
}
