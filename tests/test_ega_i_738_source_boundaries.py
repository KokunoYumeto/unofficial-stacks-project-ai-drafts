"""Independent three-version literals and adversarial raw-source replay tests.

The owned declarations, full proofs and excluded boundaries are transcribed
from the separately reviewed source preparation, not the checker tables.
Surrounding bytes are synthetic: no fixture certifies a complete source or
mathematical admission. Actual whole-source replay is the bounded CLI gate.
"""
import copy
import hashlib
import io
import json
from pathlib import Path
import unittest
from unittest.mock import MagicMock, patch

from tools import check_ega_i738_source_boundaries as check


BLOCKS = {
    "old_fr": r"""\begin{env}[7.3.8]
\label{I.7.3.8-fr}
Soient $X$, $Y$ deux préschémas ayant chacun un nombre fini de composantes
irréductibles, et soit $f:X\to Y$ un morphisme dont la restriction à
l'ensemble des points génériques des composantes irréductibles de $X$ est une
surjection sur l'ensemble des points génériques des composantes irréductibles
de $Y$. Alors on a
\[
  f^*(\mathscr{R}(Y))=\mathscr{R}(X).
  \tag{7.3.8.1}\label{I.7.3.8.1-fr}
\]
\end{env}

En effet, on est ramené (en vertu de
(\hyperref[I.7.3.3-fr]{7.3.3})) au cas où $X$ et $Y$ sont irréductibles, de
points génériques $x$, $y$, avec $f(x)=y$~; donc
\[
  (f^*(\mathscr{R}(Y)))_x
  =\mathscr{O}_y\otimes_{\mathscr{O}_y}\mathscr{O}_x
  =\mathscr{O}_x
\]
(\hyperref[0.4.3.1-fr]{0, 4.3.1}), ce qui démontre (7.3.8.1) en vertu de
(\hyperref[I.7.3.5-fr]{7.3.5}).

\subsection{Faisceaux de torsion et faisceaux sans torsion.}
\label{subsection:I.7.4-fr}

\begin{env}[7.4.1]
\label{I.7.4.1-fr}
""",
    "corrected_fr": r"""\paragraph{(I, 7.3.8).}
Remplacer le texte actuel, qui est erroné, par le suivant :

Soient $X,Y$ deux préschémas intègres, ce qui entraîne que
$\sh{R}(X)$ (resp. $\sh{R}(Y)$) est un $\sh{O}_X$-Module (resp. un
$\sh{O}_Y$-Module) quasi-cohérent (I, 7.3.3). Soit $f:X\to Y$ un
morphisme dominant; alors il existe un homomorphisme canonique de
$\sh{O}_X$-Modules
\oldpage[II]{222}
\markboth{A. GROTHENDIECK --- Chap. II}{A. GROTHENDIECK --- Chap. II}
\begin{equation}
\label{ega2:addendum:I.7.3.8.1-fr}
  \tau:f^*(\sh{R}(Y))\to\sh{R}(X).
\tag{7.3.8.1}
\end{equation}

Supposons d'abord $X=\Spec(A)$ et $Y=\Spec(B)$ affines d'anneaux
intègres $A$ et $B$, $f$ correspondant donc à un homomorphisme injectif
$B\to A$, qui se prolonge en un monomorphisme $L\to K$ du corps des
fractions $L$ de $B$ dans le corps des fractions $K$ de $A$.
L'homomorphisme (7.3.8.1) correspond alors à l'homomorphisme canonique
\[
  L\otimes_B A\to K
\]
(I, 1.6.5). Dans le cas général, pour tout couple d'ouverts affines non
vides $U\subset X$, $V\subset Y$ tels que $f(U)\subset V$, on définit
de la façon précédente un homomorphisme $\tau_{U,V}$ et on constate
aussitôt que si $U'\subset U$, $V'\subset V$,
$f(U')\subset V'$, $\tau_{U,V}$ prolonge $\tau_{U',V'}$, d'où notre
assertion. Si $x,y$ sont les points génériques de $X$ et $Y$
respectivement, on a $f(x)=y$,
\[
  \bigl(f^*(\sh{R}(Y))\bigr)_x
  =\sh{O}_y\otimes_{\sh{O}_y}\sh{O}_x
  =\sh{O}_x
\]
(0, 4.3.1), et $\tau_x$ est donc un isomorphisme.

\paragraph{(I, 9.5.2).}
""",
    "en": r"""\begin{env}[7.3.8]
\label{I.7.3.8}
\footnote{\emph{[Trans.] This paragraph was changed entirely in the Errata of EGA~II.}}
Let $X$ and $Y$ be two \emph{integral} preschemes, which implies that $\sh{R}(X)$ (resp. $\sh{R}(Y)$) is a quasi-coherent $\sh{O}_X$-module (resp. $\sh{O}_Y$-module) \sref{I.7.3.3}.
Let $f:X\to Y$ be a \emph{dominant} morphism; then there exists a canonical homomorphism of $\sh{O}_X$-modules
\[
\label{I.7.3.8.1}
  \tau:f^*(\sh{R}(Y))\to\sh{R}(X).
  \tag{7.3.8.1}
\]
\end{env}

\begin{proof}
Suppose first that $X=\Spec(A)$ and $Y=\Spec(B)$ are affine, given by integral rings $A$ and $B$, with $f$ thus corresponding to an injective homomorphism $B\to A$ which extends to a monomorphism $L\to K$ from the field of fractions $L$ of $B$ to the field of fractions $K$ of $A$.
The homomorphism \sref{I.7.3.8.1} then corresponds to the canonical homomorphism $L\otimes_B A\to K$ \sref{I.1.6.5}.
In the general case, for each pair of nonempty affine open sets $U\subset X$ and $V\subset Y$ such that $f(U)\subset V$, we define, as above, a homomorphism $\tau_{U,V}$ and we immediately have that, if $U'\subset U$, $V'\subset V$, $f(U')\subset V'$, then $\tau_{U,V}$ extends $\tau_{U',V'}$, and hence our assertion.
If $x$ and $y$ are the generic points of $X$ and $Y$ respectively, then we have $f(x)=y$,
\[
  (f^*(\sh{R}(Y)))_x=\sh{O}_y\otimes_{\sh{O}_y}\sh{O}_x=\sh{O}_x
\]
\sref[0]{0.4.3.1} and $\tau_x$ is thus an \emph{isomorphism}.
\end{proof}

\subsection{Torsion sheaves and torsion-free sheaves}
\label{subsection:I.7.4}
\label{I.7.4}

\begin{env}[7.4.1]
\label{I.7.4.1}
""",
}
VERSIONS = ("old_fr", "corrected_fr", "en")
FIRST = {"old_fr": 648, "corrected_fr": 470, "en": 380}
OFFSET = {"old_fr": 32381, "corrected_fr": 17633, "en": 29936}
LENGTH = {"old_fr": 38226, "corrected_fr": 19746, "en": 35788}
LINE_COUNT = {"old_fr": 786, "corrected_fr": 522, "en": 466}
PINNED_SHA = {
    "old_fr": "73581030E142AD91D51F07A6DE7648101ECA92C7542EA52A2575F098F171F522",
    "corrected_fr": "EC20D329248B99CF0533CB868DBDF8135D5BDAFA233133814DB67F8CD4F09643",
    "en": "B36636DA91ADA9B74A7F2B4BF1C18E4576D35B363947D06EA475BCBA2918ADBC",
}
URLS = {
    "old_fr": "https://raw.githubusercontent.com/KokunoYumeto/ega-fr/6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega1/ega1-7-fr.tex",
    "corrected_fr": "https://raw.githubusercontent.com/KokunoYumeto/ega-fr/6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega2/ega2-errata-addenda-fr.tex",
    "en": "https://raw.githubusercontent.com/KokunoYumeto/ega-en/94d5c73ac9263b26043ad0551646b824b1030c9b/source/ega1/ega1-7.tex",
}
RANGES = {
    "old_fr": {"owned": (648, 671), "statement": (648, 659), "proof": (661, 670),
               "proof_body": (661, 670), "excluded_next": (672, 676)},
    "corrected_fr": {"owned": (470, 507), "statement": (473, 484), "proof": (486, 506),
                     "proof_body": (486, 506), "excluded_next": (508, 508),
                     "replacement_instruction": (470, 471), "page_marker": (478, 478),
                     "running_header": (479, 479), "equation": (480, 484)},
    "en": {"owned": (380, 402), "statement": (380, 390), "proof": (392, 401),
           "proof_body": (393, 400), "excluded_next": (403, 408), "translator_note": (382, 382),
           "proof_open": (392, 392), "proof_close": (401, 401)},
}


def split_raw(raw):
    return [part + b"\n" for part in raw.split(b"\n")[:-1]]


def fixture(version):
    """Exact reviewed spans/offsets/counts; deliberately non-authority remainder."""
    lines = [b"\n"] * (FIRST[version] - 1)
    label = b"% SYNTHETIC NON-AUTHORITY SURROUNDING BYTES "
    lines[0] = label + b"x" * (OFFSET[version] - len(lines) - len(label)) + b"\n"
    raw = b"".join(lines) + BLOCKS[version].encode("utf-8")
    tail_count = LINE_COUNT[version] - len(split_raw(raw))
    raw += b"\n" * (tail_count - 1)
    tail = b"% synthetic later material, not a reviewed source "
    raw += tail + b"x" * (LENGTH[version] - len(raw) - len(tail) - 1) + b"\n"
    assert len(raw) == LENGTH[version]
    assert len(split_raw(raw)) == LINE_COUNT[version]
    return raw


def span(raw, first, last):
    lines = split_raw(raw)
    block = b"".join(lines[first - 1:last])
    offset = len(b"".join(lines[:first - 1]))
    return {"lf_line_start": first, "lf_line_end": last, "bytes": len(block),
            "sha256": hashlib.sha256(block).hexdigest().upper(), "byte_offset_start": offset,
            "byte_offset_end_exclusive": offset + len(block)}


def independent_metadata(raw, version):
    """No checker tables, extraction or expected-contract calls."""
    return {"url": URLS[version], "full_bytes": len(raw),
            "full_sha256": hashlib.sha256(raw).hexdigest().upper(),
            "full_lf_lines": len(split_raw(raw)),
            "proof_form": "wrapped" if version == "en" else "unwrapped",
            "spans": {key: span(raw, *bounds) for key, bounds in RANGES[version].items()}}


def pinned_metadata(version):
    result = independent_metadata(fixture(version), version)
    result["full_sha256"] = PINNED_SHA[version]
    return result


def replace_line(raw, number, content):
    lines = split_raw(raw)
    lines[number - 1] = content
    return b"".join(lines)


def leaf_paths(value, prefix=()):
    for key, child in value.items():
        if isinstance(child, dict):
            yield from leaf_paths(child, (*prefix, key))
        else:
            yield (*prefix, key)


def at_path(value, path):
    for key in path:
        value = value[key]
    return value


class SourceBoundary738Tests(unittest.TestCase):
    def test_independent_complete_three_version_literals_and_metadata(self):
        for version in VERSIONS:
            raw = fixture(version)
            self.assertEqual(check.expected_contract(version), pinned_metadata(version), version)
            self.assertEqual(check.validate_artifact(pinned_metadata(version), version), [])
            self.assertEqual(check.artifact(raw, version), independent_metadata(raw, version))
            self.assertEqual(check.verify_structure(raw, version), [])
        self.assertEqual([pinned_metadata(v)["spans"]["owned"]["bytes"] for v in VERSIONS], [834, 1502, 1470])

    def test_synthetic_fixtures_and_coordinated_self_rehash_never_certify_whole_sources(self):
        for version in VERSIONS:
            raw = fixture(version)
            self.assertEqual(check.verify_source(raw, version),
                             [version + ".source.full_sha256: pinned identity/boundary mismatch"])
            self.assertTrue(check.validate_artifact(independent_metadata(raw, version), version))
            self.assertTrue(check.verify_source(raw, version, independent_metadata(raw, version)))

    def test_all_six_version_swaps_are_rejected(self):
        for version in VERSIONS:
            for other in set(VERSIONS) - {version}:
                self.assertTrue(check.validate_artifact(pinned_metadata(other), version))
                self.assertTrue(check.verify_source(fixture(other), version, pinned_metadata(version)))

    def test_complete_proof_ownership_and_next_boundary_are_disjoint(self):
        for version in VERSIONS:
            parts = pinned_metadata(version)["spans"]
            self.assertEqual(parts["owned"]["byte_offset_end_exclusive"], parts["excluded_next"]["byte_offset_start"])
            self.assertEqual(parts["proof"]["byte_offset_start"], parts["statement"]["byte_offset_end_exclusive"] + 1)
            self.assertEqual(parts["owned"]["byte_offset_end_exclusive"], parts["proof"]["byte_offset_end_exclusive"] + 1)
            if version == "en":
                self.assertEqual(parts["proof"]["bytes"] - parts["proof_body"]["bytes"], 26)
                self.assertEqual(parts["proof_open"]["byte_offset_end_exclusive"], parts["proof_body"]["byte_offset_start"])
                self.assertEqual(parts["proof_close"]["byte_offset_start"], parts["proof_body"]["byte_offset_end_exclusive"])
            else:
                self.assertEqual(parts["proof"], parts["proof_body"])
            altered = pinned_metadata(version)
            altered["spans"]["owned"] = span(fixture(version), FIRST[version], RANGES[version]["excluded_next"][1])
            self.assertTrue(check.validate_artifact(altered, version))
            altered = pinned_metadata(version)
            altered["spans"]["proof"] = copy.deepcopy(parts["statement"])
            self.assertTrue(check.validate_artifact(altered, version))

    def test_every_contract_leaf_type_inventory_and_copy_are_independent(self):
        for version in VERSIONS:
            expected = pinned_metadata(version)
            for path in leaf_paths(expected):
                old = at_path(expected, path)
                values = (old + 1, float(old), True, None) if type(old) is int else (old + "changed", "", None, [])
                for new in values:
                    altered = copy.deepcopy(expected)
                    at_path(altered, path[:-1])[path[-1]] = new
                    self.assertTrue(check.validate_artifact(altered, version), (version, path, new))
            for key in expected:
                altered = copy.deepcopy(expected)
                del altered[key]
                self.assertTrue(check.validate_artifact(altered, version))
            for key in expected["spans"]:
                altered = copy.deepcopy(expected)
                altered["spans"]["unreviewed_741"] = altered["spans"].pop(key)
                self.assertTrue(check.validate_artifact(altered, version))
            altered = check.expected_contract(version)
            altered["spans"]["proof"]["bytes"] = 0
            self.assertEqual(check.expected_contract(version), expected)

    def test_every_owned_and_excluded_line_is_required_without_normalization(self):
        for version in VERSIONS:
            raw = fixture(version)
            for n in range(FIRST[version], RANGES[version]["excluded_next"][1] + 1):
                line = split_raw(raw)[n - 1]
                replacements = (b"omitted clause\n",) if line == b"\n" else (b"\n", b"% " + line, b" \t" + line)
                for replacement in replacements:
                    damaged = replace_line(raw, n, replacement)
                    self.assertTrue(check.verify_structure(damaged, version), (version, n))
                    self.assertTrue(check.verify_source(damaged, version, independent_metadata(damaged, version)))

    def test_notes_replacement_instruction_internal_page_and_header_are_required(self):
        for version, key in (("en", "translator_note"), ("corrected_fr", "replacement_instruction"),
                             ("corrected_fr", "page_marker"), ("corrected_fr", "running_header"),
                             ("corrected_fr", "equation")):
            raw = fixture(version)
            first, last = RANGES[version][key]
            lines = split_raw(raw)
            for n in range(first, last + 1):
                lines[n - 1] = b"\n"
            damaged = b"".join(lines)
            self.assertIn(key + ": exact literal source span mismatch", check.verify_structure(damaged, version))
            altered = pinned_metadata(version)
            del altered["spans"][key]
            self.assertTrue(check.validate_artifact(altered, version))
        parts = pinned_metadata("corrected_fr")["spans"]
        self.assertLess(parts["statement"]["byte_offset_start"], parts["page_marker"]["byte_offset_start"])
        self.assertLess(parts["page_marker"]["byte_offset_end_exclusive"], parts["statement"]["byte_offset_end_exclusive"])

    def test_wrapped_english_unwrapped_french_and_foreign_nesting_are_distinct(self):
        for version in VERSIONS:
            raw = fixture(version)
            first, last = RANGES[version]["proof"]
            for n in (first, last):
                line = split_raw(raw)[n - 1]
                for token in (b"\\begin{proof} ", b"\\end{proof} ", b"\\begin{foreign} "):
                    errors = check.verify_structure(replace_line(raw, n, token + line), version)
                    self.assertTrue(any("wrapper" in error for error in errors))
                if version == "en":
                    self.assertTrue(any("wrapper" in error for error in check.verify_structure(replace_line(raw, n, b"\n"), version)))

    def test_scoped_labels_and_page_markers_are_globally_unique(self):
        marker_lines = {"old_fr": (648, 649, 657, 673, 675, 676),
                        "corrected_fr": (470, 478, 481, 508),
                        "en": (380, 381, 386, 404, 405, 407, 408)}
        for version in VERSIONS:
            raw = fixture(version)
            for n in marker_lines[version]:
                marker = split_raw(raw)[n - 1]
                errors = check.verify_structure(raw + marker, version)
                self.assertTrue(any("globally unique" in error for error in errors), (version, n))
                self.assertEqual(check.verify_structure(raw + b"% " + marker, version), [])

    def test_outside_material_is_not_reowned_but_changes_fail_whole_identity(self):
        for version in VERSIONS:
            raw = replace_line(fixture(version), FIRST[version] - 1, b"unreviewed preceding mathematics\n")
            raw += b"unreviewed later mathematics\n"
            self.assertEqual(check.verify_structure(raw, version), [])
            self.assertTrue(check.verify_source(raw, version, independent_metadata(raw, version)))

    def test_raw_lf_utf8_size_version_and_metadata_fail_closed(self):
        for version in VERSIONS:
            raw = fixture(version)
            for damaged in (None, "not bytes", bytearray(raw), b"", raw[:-1], raw.replace(b"\n", b"\r\n"),
                            b"\xff\n", b"\xef\xbb\xbf" + raw, b"x" * 1048577 + b"\n",
                            b"".join(split_raw(raw)[:RANGES[version]["excluded_next"][1] - 1])):
                self.assertTrue(check.verify_source(damaged, version))
            unusual = raw.replace(b"SYNTHETIC", b"SYNTHETIC\x0c\xe2\x80\xa8", 1)
            self.assertEqual(len(check.raw_lines(unusual)), LINE_COUNT[version])
            self.assertEqual(check.verify_structure(unusual, version), [])
        for version in ("fr", "wrong", None, [], True):
            self.assertTrue(check.validate_artifact({}, version))
            self.assertTrue(check.verify_source(b"x\n", version))
            with self.assertRaises(ValueError):
                check.artifact(b"x\n", version)
        for value in (None, [], {}, True):
            self.assertTrue(check.validate_artifact(value, "en"))
        for first, last in ((0, 1), (1, 3), (2, 1), (True, 1), (1, 2.0), ("1", 2)):
            with self.assertRaises(ValueError):
                check.raw_span([b"a\n", b"bc\n"], first, last)
        self.assertEqual(check.raw_span([b"a\n", b"bc\n"], 2, 2), span(b"a\nbc\n", 2, 2))


class BoundedReplay738Tests(unittest.TestCase):
    def test_cached_and_network_routes_are_one_bounded_read_per_version(self):
        for version in VERSIONS:
            cached = MagicMock(spec=Path)
            cached.open.return_value.__enter__.return_value.read.return_value = fixture(version)
            with patch.object(check, "urlopen", side_effect=AssertionError("network forbidden")):
                self.assertEqual(check.read_source(pinned_metadata(version), version, cached), fixture(version))
            cached.open.assert_called_once_with("rb")
            cached.open.return_value.__enter__.return_value.read.assert_called_once_with(LENGTH[version] + 1)
            response = MagicMock()
            response.__enter__.return_value.read.return_value = fixture(version)
            with patch.object(check, "urlopen", return_value=response) as fetch:
                self.assertEqual(check.fetch_source(version), fixture(version))
            fetch.assert_called_once_with(URLS[version], timeout=30)
            response.__enter__.return_value.read.assert_called_once_with(LENGTH[version] + 1)

    def test_short_oversized_nonbytes_and_transport_failure_never_retry(self):
        for returned in (b"", fixture("en")[:-1], fixture("en") + b"x", "not bytes", None):
            response = MagicMock()
            response.__enter__.return_value.read.return_value = returned
            with patch.object(check, "urlopen", return_value=response) as fetch:
                with self.assertRaises(ValueError):
                    check.fetch_source("en")
                fetch.assert_called_once()
        with patch.object(check, "urlopen", side_effect=OSError("bounded failure")) as fetch:
            with self.assertRaises(OSError):
                check.fetch_source("en")
            fetch.assert_called_once()

    def test_malformed_or_swapped_contracts_and_bad_caps_do_no_source_io(self):
        cached = MagicMock(spec=Path)
        with patch.object(check, "urlopen") as fetch:
            for version in VERSIONS:
                expected = pinned_metadata(version)
                bad = [None, [], {}, {**expected, "full_bytes": True},
                       {**expected, "full_bytes": 1048577}, {**expected, "spans": {}},
                       {**expected, "url": "https://example.invalid/"}]
                bad += [pinned_metadata(other) for other in set(VERSIONS) - {version}]
                for receipt in bad:
                    for cache in (None, cached):
                        with self.assertRaises(ValueError):
                            check.read_source(receipt, version, cache)
            for version in ("fr", None, []):
                with self.assertRaises(ValueError):
                    check.fetch_source(version, cached)
            for size in (True, 0, 1048576, 1048577):
                with patch.dict(check.SOURCE_IDENTITIES, {"en": (size, PINNED_SHA["en"], LINE_COUNT["en"])}):
                    with self.assertRaises(ValueError):
                        check.fetch_source("en", cached)
            fetch.assert_not_called()
            cached.open.assert_not_called()

    def test_cli_validates_all_three_contracts_before_any_read_and_rejects_duplicate_keys(self):
        receipt = {"languages": {version: pinned_metadata(version) for version in VERSIONS}}
        invalid = ["{", "[]", "{}", '{"languages":[]}', '{"languages":{"old_fr":{}}}']
        for version in VERSIONS:
            for key in receipt["languages"][version]:
                altered = copy.deepcopy(receipt)
                altered["languages"][version][key] = "invalid"
                invalid.append(json.dumps(altered))
            for other in set(VERSIONS) - {version}:
                altered = copy.deepcopy(receipt)
                altered["languages"][version] = pinned_metadata(other)
                invalid.append(json.dumps(altered))
        invalid.append(json.dumps({"languages": {**receipt["languages"], "unreviewed": {}}}))
        valid = json.dumps(receipt)
        invalid += [valid.replace('"full_bytes": 38226', '"full_bytes": 0, "full_bytes": 38226'),
                    valid.replace('"languages":', '"languages": {}, "languages":', 1)]
        for text in invalid:
            with patch.object(Path, "read_text", return_value=text), patch.object(check, "read_source") as read, \
                    patch("sys.stdout", new_callable=io.StringIO) as output:
                self.assertTrue(check.main([]))
                read.assert_not_called()
                self.assertEqual(json.loads(output.getvalue())["status"], "FAIL")

    def test_cli_missing_receipt_and_three_transport_failures_are_structured(self):
        with patch.object(Path, "read_text", side_effect=FileNotFoundError("absent")), \
                patch.object(check, "read_source") as read, patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertTrue(check.main([]))
            read.assert_not_called()
            self.assertEqual(json.loads(output.getvalue())["status"], "FAIL")
        receipt = {"languages": {version: pinned_metadata(version) for version in VERSIONS}}
        with patch.object(Path, "read_text", return_value=json.dumps(receipt)), \
                patch.object(check, "read_source", side_effect=OSError("bounded failure")) as read, \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertTrue(check.main([]))
            self.assertEqual(read.call_count, 3)
            self.assertEqual(len(json.loads(output.getvalue())["errors"]), 3)

    def test_cli_does_not_confuse_successful_transport_with_whole_source_certification(self):
        receipt = {"languages": {version: pinned_metadata(version) for version in VERSIONS}}
        with patch.object(Path, "read_text", return_value=json.dumps(receipt)), \
                patch.object(check, "read_source", side_effect=lambda expected, version, cached: fixture(version)), \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertTrue(check.main([]))
            result = json.loads(output.getvalue())
            self.assertEqual(set(result["sources"]), set(VERSIONS))
            self.assertTrue(all(source["status"] == "FAIL" for source in result["sources"].values()))
            self.assertEqual(len(result["errors"]), 3)

    def test_cli_passing_plumbing_uses_each_cache_without_writes(self):
        receipt = {"languages": {version: pinned_metadata(version) for version in VERSIONS}}
        with patch.object(Path, "read_text", return_value=json.dumps(receipt)) as load, \
                patch.object(check, "read_source", side_effect=lambda expected, version, cached: fixture(version)) as read, \
                patch.object(check, "verify_source", return_value=[]) as verify, \
                patch.object(Path, "write_text") as write_text, patch.object(Path, "write_bytes") as write_bytes, \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertFalse(check.main(["--old-french", "old-fr.tex", "--corrected-french", "corrected-fr.tex", "--english", "en.tex"]))
            load.assert_called_once_with(encoding="utf-8")
            self.assertEqual(read.call_count, 3)
            self.assertEqual(verify.call_count, 3)
            self.assertEqual([call.args[2] for call in read.call_args_list], [Path("old-fr.tex"), Path("corrected-fr.tex"), Path("en.tex")])
            write_text.assert_not_called()
            write_bytes.assert_not_called()
            result = json.loads(output.getvalue())
            self.assertEqual(result["schema"], "ega-i738-raw-source-boundary-replay/v1")
            self.assertEqual(result["status"], "PASS")
        self.assertEqual(check.RECEIPT.name, "ega-i-7.3.8-semantic-checkpoint-2026-09-08.json")


if __name__ == "__main__":
    unittest.main()
