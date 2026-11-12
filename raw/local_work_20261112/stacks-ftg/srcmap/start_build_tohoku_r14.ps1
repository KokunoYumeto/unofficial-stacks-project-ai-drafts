$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$bootstrap = Join-Path $root 'srcmap\start_build_tohoku_r14.py'
$expectedBytes = 1330
$expectedSha256 = 'B53732AFF53B1CE537E8491164A3DD09E05BFD98F7C327B72CF2F9D82F41B5FE'
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
    throw "Tohoku r14 mapping bootstrap failed with exit code $LASTEXITCODE"
}
