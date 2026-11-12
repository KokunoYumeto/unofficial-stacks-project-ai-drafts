$ErrorActionPreference = 'Stop'

$helperPath = Join-Path $PSScriptRoot 'build_tohoku_r9.py'
$envelopePath = $PSCommandPath
$envelopeBytes = (Get-Item -LiteralPath $envelopePath).Length
$envelopeSha256 = (Get-FileHash -LiteralPath $envelopePath -Algorithm SHA256).Hash.ToUpperInvariant()
$expectedBytes = 41212
$expectedSha256 = 'DD9F702F90AB4A0CF10249BD996D609E1838B57F8895D5248E4CD3421657D83F'
$pythonCode = @'
import hashlib
import pathlib
import sys

path = pathlib.Path(sys.argv[1])
expected_bytes = int(sys.argv[2])
expected_sha256 = sys.argv[3]
envelope_path = pathlib.Path(sys.argv[4])
envelope_bytes = int(sys.argv[5])
envelope_sha256 = sys.argv[6]
data = path.read_bytes()
digest = hashlib.sha256(data).hexdigest().upper()
if (len(data), digest) != (expected_bytes, expected_sha256):
    raise ValueError('Frozen Tohoku r9 dossier helper identity drift')
record = {
    'path': 'srcmap/build_tohoku_r9.py',
    'bytes': len(data),
    'sha256': digest,
    'contract': 'one_read_hash_then_exec_same_bytes',
}
envelope_data = envelope_path.read_bytes()
envelope_digest = hashlib.sha256(envelope_data).hexdigest().upper()
if (len(envelope_data), envelope_digest) != (envelope_bytes, envelope_sha256):
    raise ValueError('Tohoku r9 dossier launcher envelope changed before helper execution')
envelope_record = {
    'path': 'srcmap/start_build_tohoku_r9.ps1',
    'bytes': envelope_bytes,
    'sha256': envelope_sha256,
    'contract': 'self_read_hash_before_helper_exec',
}
scope = {
    '__name__': '__main__',
    '__file__': str(path),
    '__package__': None,
    '__verified_helper_snapshot__': record,
    '__verified_envelope_snapshot__': envelope_record,
}
exec(compile(data, str(path), 'exec', dont_inherit=True), scope)
raise RuntimeError('Tohoku r9 dossier helper returned without SystemExit')
'@

& python -I -S -B -c $pythonCode $helperPath $expectedBytes $expectedSha256 $envelopePath $envelopeBytes $envelopeSha256
exit $LASTEXITCODE
