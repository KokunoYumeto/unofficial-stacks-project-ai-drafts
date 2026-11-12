$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$bootstrap = Join-Path $root 'srcmap\start_build_tohoku_r15.py'
$expectedBytes = 1330
$expectedSha256 = 'F1114609930F3F36D3DB574B8F1070A9DA27BDA62317F2F590B86BBF205AF925'
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
    throw "Tohoku r15 mapping bootstrap failed with exit code $LASTEXITCODE"
}
