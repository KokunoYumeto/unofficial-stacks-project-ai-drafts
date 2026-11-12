#!/usr/bin/env python3
"""Build the no-overwrite Tohoku Stacks mapping successor D000993."""

from __future__ import annotations

import contextlib
import csv
import hashlib
import io
import json
import os
import re
import subprocess
import sys
from collections.abc import Iterator
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "tohoku_r38"
TARGET = ROOT / "tohoku_r39"
STAGE = ROOT / ".tohoku-r39-txn"
PROJECT = Path(
    r"user\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\03_working_translations"
    r"\tohoku_bilingual_canonical_stacks_20260804_r1"
)
SEM = PROJECT / "sem" / "r14"
SEM_QA = PROJECT / "qa" / "v68r33"
READER_QA = PROJECT / "qa" / "v68r32" / "check.json"
P141_SOURCE = PROJECT / "production" / "p141_fix1" / "check.json"
READER_BUILD = PROJECT / "build" / "v068c3r12" / "build.json"
AUTHORITY = PROJECT / "authority_snapshot"

EXPECTED_GIT_NONCLAIM = {
    "inspection_performed": False,
    "reason": "No Git operation was needed for this bounded local successor.",
    "predecessor_receipt": {
        "path": "tohoku_r38/r38-check.json",
        "bytes": 17781,
        "sha256": "968E52D710E7D08E8970EC0D3F25F9C726352C003C23602519BAA86F8C0FACC4",
    },
    "remote_server_freshness_verified": False,
}

EXPECTED_SOURCE = {
    "STATUS.md": (641, "EFD593429E3AC37859580629B2F8340ABC246D839443BACDD75AD62EF92BE8FE"),
    "cfg.json": (5193, "A088704D7E156113C62FD95B3344DBB08D8EEAD543F934A60152E70C3CB5A446"),
    "check.json": (74954, "58E6F6A024AF9A6BD3CC309EC7727C4BCC05C12602EA299BED3165E4DB3520F1"),
    "dec.csv": (353176, "E3F0D5396A824C41F1EFBF7683CF522DC901AB18EF6CE0DBD8083E7695E8A50E"),
    "intake.json": (1877, "EB529D8C7981784C3991C013513DC4E167A198DAFEA774EC92AA22816435F247"),
    "issues.csv": (23487, "B131717123CAF4F444898DACD85AD636A2C70349BA1FC7EE45A0E9012A5CC188"),
    "map.csv": (469114, "1EC4E4F85D89DD65CBBB31783249DE239C28B9E230BB0223CD6CFCF19F0B6DEB"),
    "mcheck.json": (64782, "8B64D2840C3FC9AFB79CC5EF1DB69C3E576E65CED7486B83E64E2D1B26CE3431"),
    "r38-check.json": (17781, "968E52D710E7D08E8970EC0D3F25F9C726352C003C23602519BAA86F8C0FACC4"),
    "stx.csv": (5268730, "61459E55403E3CDEC3F9AB851336FAAD0C2EBEE45154BB6482E8ECA921CBCC8D"),
    "tcand.csv": (478316, "FD899040BC1C9D1B85C904DDC15B0771C8E3B877DBB6417A32CC159649C9FDB8"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (391679, "739F58491FCBF452B41EEE65E97CE515DD2B618438DA77BA08A07E6BD7969B15"),
}
EXPECTED_SOURCE_SURFACE = (
    15,
    7154727,
    "935C2631C3061C4229589204D99979CAE7666B05E5186D55E57D07A39F447DED",
)

EXPECTED_TOOLS = {
    "srcmap/intake.py": (9923, "CFD53B71649BEF84A166397AA18E39AC5E4EDF00DD860142B2936F886AB080B1"),
    "srcmap/scan.py": (3403, "269E4D2F73405BDA82F373F04AF0109431416FF25CCA874F0051D193BC444D30"),
    "srcmap/map.py": (27167, "57A92E34DB189E0EE95E6816074DB686C5616590C33DF823EF8EB9E9AFC2E1DF"),
    "fga/mkidx.py": (14844, "4425B5D021B3E35371DEBB567881697F88DF6F533ACFC9783A749CE1A5176A6B"),
    "fga/mkmap.py": (22213, "7281F57EC7439E00431F2962DF9A6944779294955A9C4369615FFF04318B0053"),
    "fga/__pycache__/mkidx.cpython-313.pyc": (21123, "A78A1E45C6EB3960139B1D2A8AF42E5B10768034F0A87274448EBA69779BD424"),
    "fga/__pycache__/mkmap.cpython-313.pyc": (26471, "1AA6B79FFE873AB6C2E58FF2A9826DE6FDB6B1DD69A8D3473FD5F56168F2077D"),
    "tags/tags": (991506, "C5C7017FB5C50B60295B30801CA1B5BAB8F5B379F61B084D8219441938125FCF"),
}

EXPECTED_SEM_QA = {
    "sem-input.json": (293150, "EB8F801D62ADEFAA93EC2418B29B69FF9ED07B6F77F705A847621411A0676497"),
    "sem-check.json": (6707, "93B3075BA187F92D9C6E2A09A91E0B8BCD09F3E8A995DD6D82FFA4643406DC38"),
}
EXPECTED_REPAIR_RECEIPTS = {
    "production/p141_fix1/check.json": (
        P141_SOURCE,
        6579,
        "E8936C2A0D376A2B8EC48EB3B1D70DA76927F59112548A168A5589311F2B3658",
    ),
    "build/v068c3r12/build.json": (
        READER_BUILD,
        92774,
        "D3E4CD6540E221EE0F6DEEB1E4E87BB4E572328EABA1681356AB71631894D4FD",
    ),
    "qa/v68r32/check.json": (
        READER_QA,
        10340,
        "E34B9BB8180F5A359985A0CA408CC3F2E8B004C9FA6110D9D510F32C8EE91EF9",
    ),
}

EXPECTED_AUTHORITY = {
    "jstage_part_I_9_2_119.pdf": (7305283, "5A8E5720BC2EF8905BF85F7919C65AC4A87A31CFC854BD77E6B5084C0D2DEBEF"),
    "jstage_part_II_9_3_185.pdf": (3984260, "8D632A04EE0FA987B40B721BEE6E64BB3E641D6A1CE02335556213F1564C9A53"),
}

EXPECTED_ARTIFACTS = {
    "homology.tex": (371262, "B4D00EF51FC4181236736A2A046EAE86975371BD2130C4F30151BEB383858758"),
    "homology.aux": (28402, "4BBBC8F0862AABFE88FF45923C65700A181D0E3C152E3068DB8425D7DE52684F"),
    "homology.log": (39260, "B1C578F33DE33287F99035171B31689A1AF18779EA200C577A8E556CC45374F0"),
    "homology.pdf": (1065209, "729067E7C568D031D1455A6E16C90AB1BAF103C7710E68BAF227726199C35A7C"),
    "modules.tex": (227768, "6BDE2852FFC50945A781FE7598FE96EC69D8B650EEF5C4C608C440D9E7E53BC0"),
    "modules.log": (35913, "D2989C27651EACA9A5AA4BD22FCF67E7273EF67D0CC0DA9606C23844E7D94BE1"),
    "modules.pdf": (758941, "1254E015413AFF83541031659835E3B02998D1F43550FB83D00D07A5DE3CB3E9"),
    "cohomology.tex": (814928, "C120A56D9C3788BE467DDDBA310F8A2FDDE0AB3326ED7B9183E8B16337418AD4"),
    "cohomology.log": (47485, "95EFD946BDA79140BBA240055142E4F13E2F8E53A690DD5B74690D6449A386D2"),
    "cohomology.pdf": (1832179, "50DE21B2916AF71A8B05774FCBAB754A750F599CC34C0E2B62CE069526E29822"),
    "injectives.tex": (130520, "5BC898D7A1A1017D28C6C28CA5F318D3E96A12A333CE6684FF13600316DA5D22"),
    "injectives.log": (35028, "5F0474FCF38F15F733CEF9DCA12044FB54D9E87BFAE5FD2B219E830AA46CC404"),
    "injectives.pdf": (633384, "7D651B4DB0A9D03D24195CCF3BCD726817867057BC082F8A996A30AD8E858D58"),
}

BUILD_SPECS = {
    "homology": {"pdf_pages": 113, "visual_reviewed_pages": [47, 48, 49, 50, 51, 52]},
    "modules": {"pdf_pages": 58, "visual_reviewed_pages": [5, 6]},
    "cohomology": {"pdf_pages": 214, "visual_reviewed_pages": [162, 163, 164]},
    "injectives": {"pdf_pages": 38, "visual_reviewed_pages": [18, 19, 20]},
}

EXPECTED_AUX_LABEL_LINES = (
    r"\newlabel{lemma-finite-effaceability-universality}{{13.18}{48}{Finite effaceability criterion}{subsection.13.18}{}}",
    r"\newlabel{equation-finite-effaceability-factor}{{13.18.1}{49}{Cohomological delta-functors}{equation.13.18.1}{}}",
    r"\newlabel{lemma-right-satellites-exactness-criterion}{{13.19}{51}{Exactness criterion for right satellites}{subsection.13.19}{}}",
    r"\newlabel{equation-right-satellites-nested-subobjects}{{13.19.1}{51}{Exactness criterion for right satellites}{equation.13.19.1}{}}",
)

NEW_LOCAL_LABELS = (
    "homology-equation-finite-effaceability-factor",
    "homology-equation-right-satellites-nested-subobjects",
    "homology-lemma-finite-effaceability-universality",
    "homology-lemma-right-satellites-exactness-criterion",
)
EXPECTED_NEW_LABEL_ROWS = {
    "homology-equation-finite-effaceability-factor": {
        "file": "homology.tex",
        "line": "4525",
        "kind": "equation",
        "short_label": "equation-finite-effaceability-factor",
        "section_label": "section-cohomological-delta-functor",
        "text_sha256": "A9AEA9E4EFB3E7F0DF3209FBC301F98FBC2E529F3074A62307253E94589A4CC7",
    },
    "homology-equation-right-satellites-nested-subobjects": {
        "file": "homology.tex",
        "line": "4690",
        "kind": "equation",
        "short_label": "equation-right-satellites-nested-subobjects",
        "section_label": "section-cohomological-delta-functor",
        "text_sha256": "ED3C4D4AB85D584E0B8CC3A06AED7B0DA9302EE08A106EE0CE56CBE7D6B939B5",
    },
    "homology-lemma-finite-effaceability-universality": {
        "file": "homology.tex",
        "line": "4413",
        "kind": "lemma",
        "short_label": "lemma-finite-effaceability-universality",
        "section_label": "section-cohomological-delta-functor",
        "text_sha256": "3EA60B226561D2CA036D079B9025B252587C68039E8406D6EC50BAEBCEF87C47",
    },
    "homology-lemma-right-satellites-exactness-criterion": {
        "file": "homology.tex",
        "line": "4670",
        "kind": "lemma",
        "short_label": "lemma-right-satellites-exactness-criterion",
        "section_label": "section-cohomological-delta-functor",
        "text_sha256": "010EB6791248E7546B959711753D3023B605B4B66BE21E600D14733B9C8E9C20",
    },
}
EXPECTED_TOPIC_CANDIDATE_ADDED = tuple(
    ("delta-functor", label) for label in NEW_LOCAL_LABELS
)

DECISION_ROWS = [
    {
        "decision_id": "D000993",
        "unit_id": "tohoku:prop:2.2.1",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": (
            "homology-lemma-finite-effaceability-universality;"
            "homology-lemma-right-satellites-injective-effacements;"
            "homology-lemma-graded-connecting-functor-dualities"
        ),
        "rationale": (
            "After the registered p. 141 range and variance corrections, Stacks proves "
            "exactly the finite unpadded assertion on degrees 0 through a. For covariant "
            "exact graded connecting functors, positive effaceability implies universality, "
            "and under injective effacements universality implies positive effaceability by "
            "comparison with the finite restriction of the right-satellite system. Applied "
            "to the opposite source, the same lemma gives the contravariant statement with "
            "co-effaceability and projective effacements. No enough-injectives, all-degree, "
            "exact-satellite, or derived-functor hypothesis is substituted."
        ),
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000731",
    },
]

ISSUE_ROWS = [
    {
        "issue_id": "I000027",
        "unit_id": "tohoku:prop:2.2.1",
        "status": "resolved",
        "kind": "source_variance_hypothesis_conflation",
        "claim": (
            "The printed p. 141 proposition applies positive effaceability and the "
            "injective-effacement converse to an exact partial graded connecting functor "
            "declared covariant or contravariant. In the contravariant case the categorical "
            "dual requires positive co-effaceability and projective effacements."
        ),
        "evidence_labels": (
            "homology-lemma-finite-effaceability-universality;"
            "homology-lemma-right-satellites-injective-effacements;"
            "homology-lemma-graded-connecting-functor-dualities"
        ),
        "evidence": (
            "Official Part I SHA-256 "
            "5A8E5720BC2EF8905BF85F7919C65AC4A87A31CFC854BD77E6B5084C0D2DEBEF, "
            "printed p. 141, together with the preceding duality paragraph and the projective "
            "dual on printed p. 142. production/p141_fix1/check.json, 6579 bytes, SHA-256 "
            "E8936C2A0D376A2B8EC48EB3B1D70DA76927F59112548A168A5589311F2B3658, "
            "seals the variance-sensitive corrected source while preserving the diplomatic "
            "French. build/v068c3r12/build.json, 92774 bytes, SHA-256 "
            "D3E4CD6540E221EE0F6DEEB1E4E87BB4E572328EABA1681356AB71631894D4FD, "
            "and qa/v68r32/check.json, 10340 bytes, SHA-256 "
            "E34B9BB8180F5A359985A0CA408CC3F2E8B004C9FA6110D9D510F32C8EE91EF9, "
            "seal the reader successor and independent visual audit. sem/r14/manifest.json, "
            "6546 bytes, SHA-256 "
            "38CEF77FD45EB826F0E38C95194E37824FBFC99B28A14558E7A6490B7DFDF1DE, "
            "sem/r14/validation.json, 3918 bytes, SHA-256 "
            "F82C9C8C78F386BC1B7F702F37E19AE5EF27065123930FBA21EC76512CD282DE, "
            "and qa/v68r33/sem-check.json, 6707 bytes, SHA-256 "
            "93B3075BA187F92D9C6E2A09A91E0B8BCD09F3E8A995DD6D82FFA4643406DC38, "
            "seal occurrence tohoku:occ:p141:o003 with diplomatic, corrected-French, and "
            "English segment hashes FB74732C022BB575D0C18C3A290D011A7F25B4816D261FFB25F3C04E8685E7B7, "
            "25C4E4FCE69BA7010D18B00ADBA1E9E6A4C1BE47E82F6636A57C5C4A1BAF0164, "
            "and 862EF7EB7B57062D8035D66BA140E85D62E51761D4CB7C20F678646AEAF804CE."
        ),
        "control": (
            "Preserve the printed undifferentiated wording in diplomatic French. In corrected "
            "French, English, and the semantic graph, use effaceability with injective "
            "effacements in the covariant clause and co-effaceability with projective "
            "effacements in the contravariant clause, retaining the finite range 0<=i<=a. "
            "The sealed source, reader, semantic, and Stacks successors close only this "
            "variance issue through D000993."
        ),
        "resolution_decision": "D000993",
    },
]

SEMANTIC_SURFACE = (
    18,
    2022947,
    "853DB3E45B3CBC769C6A9D4010F4CBF0EF82FBDA607C096FE859B2BCBDC3C598",
)
EXPECTED_P141_TITLE = (
    "Proposition 2.2.1. --- Let C and C' be abelian categories and let T=(T i) "
    "0 i a be an exact -functor, covariant or contravariant, from C to C' , where "
    "a>0 . If T is covariant and T i is effaceable for i>0 , then T is a universal "
    "-functor. The converse holds if"
)

EXPECTED_SCAN_COUNTS = {
    "labels": 22038,
    "official_tags_joined": 21437,
    "tex_files": 119,
    "topic_candidates": 1254,
    "topic_coverage": {"direct": 13},
    "topics": 13,
}
EXPECTED_MAPPING_COUNTS = {
    "active_graph_corrections": 0,
    "active_source_issues": 0,
    "candidate_units": 0,
    "decided_units": 678,
    "decisions": 993,
    "dispositions": {
        "example_or_remark": 84,
        "existing_equivalent": 344,
        "existing_stronger": 38,
        "existing_weaker": 10,
        "extend_existing": 24,
        "historical_reference": 33,
        "new_section": 6,
        "new_statement": 25,
        "structural_only": 426,
    },
    "graph_corrections": 0,
    "review_units": 0,
    "source_issues": 27,
    "unit_candidates": 0,
    "units": 990,
}

STATUS_BYTES = (
    "# Tohoku Stacks mapping status\n\n"
    "- Semantic source: independently sealed local-unpublished `sem/r14`.\n"
    "- Stable source inventory: 990 units; all source locations advance from `sem/r13` to `sem/r14`, with only the corrected p. 141 title changing.\n"
    "- Append-only decision `D000993` binds corrected Proposition 2.2.1 to the independently audited finite effaceability criterion and its variance dual.\n"
    "- Append-only issue `I000027` records and resolves only the p. 141 variance repair against sealed source, reader, semantic, and Stacks evidence.\n"
    "- The pinned live Stacks index honestly includes both the D000993 labels and the later D000216 exactness-criterion labels; D000216 remains `new_statement` and unmapped in this successor.\n"
    "- All 27 recorded source issues are resolved; no active source issue remains.\n"
    "- 65 gap-class dispositions remain.\n"
    "- This local dossier makes no release, publication, remote-freshness, DOI, rights, or completion claim.\n"
).encode("utf-8")

PAYLOAD = {
    "cfg.json", "intake.json", "units.csv", "topics.csv", "dec.csv",
    "issues.csv", "check.json", "stx.csv", "tcand.csv", "tmap.csv",
    "map.csv", "ucand.csv", "mcheck.json", "STATUS.md",
}

EXPECTED_OUTPUTS = {
    "STATUS.md": (944, "96D99B083556C45119550F5C889CB9245E8F27EBC89066FBFCAF4B62F91980AA"),
    "cfg.json": (5193, "F8289A4EC117691E2C4C6DB68CCD9493E950DFBFBDEC479EF3755990174A4DF3"),
    "check.json": (75374, "5F685CF07655F115A7CE4A8D30C09BC4B7BEBFAC5C575FB372EAE269BA7F7BD0"),
    "dec.csv": (354048, "174F23735930287577C73163AFF6BE66C0C4690768C1266E58501E4C2759C5CE"),
    "intake.json": (1877, "019F18987B67A397CD74A9B48191F0F28428B0A578D14081E438503F0498C764"),
    "issues.csv": (25752, "841A47A0D1908B6FD5FC9DFC843F243B78D25B021A911D2D54D050FD4C6F173E"),
    "map.csv": (469125, "C38E75A15849A07C5B64421EA8C851A18C1037E39626DD1E04852D069A914191"),
    "mcheck.json": (65202, "918BC368D555AFCC89D6AD88244CEAAE12916432F0CCA8410B5D05B863640284"),
    "stx.csv": (5269821, "F60B9347A9F5668B7D98BC008EBBB8F5BB935E72CD403939D6822CB7CEF1B881"),
    "tcand.csv": (479604, "AB92928771F7C49FBF180913287AFC201C5704DA223EAC6D42E0EE4F19D32BA0"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (391679, "009A308042BE4978FF822700FA76AA11E74B0138F7CAADDCF348DFF74814D681"),
}
EXPECTED_OUTPUT_SURFACE = (
    14,
    7143616,
    "40113E77C632A092C99D7580D92417A619142B21B088DCE435A9D1D56C327DB2",
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def identity(path: Path) -> tuple[int, str]:
    data = path.read_bytes()
    return len(data), digest(data)


def record(path: Path, name: str | None = None) -> dict[str, object]:
    size, sha256 = identity(path)
    return {"name": name or path.name, "bytes": size, "sha256": sha256}


def constant_record(name: str, expected: tuple[int, str]) -> dict[str, object]:
    return {"name": Path(name).name, "bytes": expected[0], "sha256": expected[1]}


def aggregate(records: list[dict[str, object]]) -> str:
    data = b"".join(
        f"{item['name']}\0{item['bytes']}\0{item['sha256']}\n".encode("utf-8")
        for item in sorted(records, key=lambda value: str(value["name"]))
    )
    return digest(data)


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def no_duplicate_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    output: dict[str, object] = {}
    for key, value in pairs:
        if key in output:
            raise ValueError(f"Duplicate JSON key: {key}")
        output[key] = value
    return output


def strict_json(path: Path) -> dict:
    data = path.read_bytes()
    if b"\r" in data or not data.endswith(b"\n"):
        raise RuntimeError(f"Noncanonical JSON: {path}")
    value = json.loads(data.decode("utf-8"), object_pairs_hook=no_duplicate_pairs)
    if not isinstance(value, dict):
        raise RuntimeError(f"Expected JSON object: {path}")
    return value


def load_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    return load_csv_bytes(path.read_bytes(), str(path))


def load_csv_bytes(data: bytes, source: str = "memory") -> tuple[list[str], list[dict[str, str]]]:
    if b"\r" in data or not data.endswith(b"\n"):
        raise RuntimeError(f"Noncanonical CSV: {source}")
    reader = csv.DictReader(data.decode("utf-8-sig").splitlines())
    rows = list(reader)
    if reader.fieldnames is None or any(None in row or None in row.values() for row in rows):
        raise RuntimeError(f"Malformed CSV: {source}")
    return list(reader.fieldnames), rows


def csv_bytes(fields: list[str], rows: list[dict[str, str]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def exclusive_write(path: Path, data: bytes) -> None:
    with path.open("xb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())
    if path.read_bytes() != data:
        raise RuntimeError(f"Write readback mismatch: {path}")


def is_reparse(path: Path) -> bool:
    return bool(path.stat(follow_symlinks=False).st_file_attributes & 0x400)


def require_plain_file(path: Path) -> None:
    if not path.is_file() or path.is_symlink() or is_reparse(path):
        raise RuntimeError(f"Expected plain file: {path}")


def require_plain_directory(path: Path) -> None:
    if not path.is_dir() or path.is_symlink() or is_reparse(path):
        raise RuntimeError(f"Expected plain directory: {path}")


def require_identity(path: Path, expected: tuple[int, str]) -> None:
    require_plain_file(path)
    if identity(path) != expected:
        raise RuntimeError(f"Input identity drift: {path}")


@contextlib.contextmanager
def deny_write_delete(paths: list[Path]) -> Iterator[None]:
    """Hold Windows read handles that deny write and delete."""
    if os.name != "nt":
        raise RuntimeError("This transaction requires Windows file locks")
    import ctypes
    from ctypes import wintypes

    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    create_file = kernel32.CreateFileW
    create_file.argtypes = [
        wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD, wintypes.LPVOID,
        wintypes.DWORD, wintypes.DWORD, wintypes.HANDLE,
    ]
    create_file.restype = wintypes.HANDLE
    close_handle = kernel32.CloseHandle
    close_handle.argtypes = [wintypes.HANDLE]
    close_handle.restype = wintypes.BOOL
    handles: list[object] = []
    invalid = ctypes.c_void_p(-1).value
    try:
        for path in sorted(set(paths), key=lambda item: str(item).casefold()):
            require_plain_file(path)
            handle = create_file(
                str(path), 0x80000000, 0x00000001, None, 3, 0x00000080, None
            )
            if handle in (None, invalid):
                raise OSError(ctypes.get_last_error(), f"Cannot lock {path}")
            handles.append(handle)
        yield
    finally:
        for handle in reversed(handles):
            close_handle(handle)


@contextlib.contextmanager
def single_writer_mutex() -> Iterator[None]:
    if os.name != "nt":
        raise RuntimeError("This transaction requires a Windows mutex")
    import ctypes
    from ctypes import wintypes

    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    create_mutex = kernel32.CreateMutexW
    create_mutex.argtypes = [wintypes.LPVOID, wintypes.BOOL, wintypes.LPCWSTR]
    create_mutex.restype = wintypes.HANDLE
    close_handle = kernel32.CloseHandle
    close_handle.argtypes = [wintypes.HANDLE]
    close_handle.restype = wintypes.BOOL
    handle = create_mutex(None, False, r"Local\FAC-Tohoku-r39-mapping")
    if not handle:
        raise OSError(ctypes.get_last_error(), "Cannot create Tohoku r39 mutex")
    if ctypes.get_last_error() == 183:
        close_handle(handle)
        raise RuntimeError("Another Tohoku r39 transaction is active")
    try:
        yield
    finally:
        close_handle(handle)


def sem_records() -> list[dict[str, object]]:
    check = strict_json(SEM_QA / "sem-check.json")
    surface = check.get("semantic_surface")
    if not isinstance(surface, dict) or (
        surface.get("file_count"), surface.get("bytes"), surface.get("aggregate_sha256")
    ) != SEMANTIC_SURFACE:
        raise RuntimeError("Semantic surface receipt drift")
    records = surface.get("files")
    if not isinstance(records, list) or len(records) != 18:
        raise RuntimeError("Semantic file records are malformed")
    return records


def expected_tex_hashes() -> dict[str, str]:
    hashes = dict(strict_json(SOURCE / "check.json")["tex_sha256"])
    if len(hashes) != 119:
        raise RuntimeError("Predecessor TeX manifest drift")
    hashes["homology.tex"] = EXPECTED_ARTIFACTS["homology.tex"][1]
    return hashes


def lock_paths(fresh: bool) -> list[Path]:
    semantic = [SEM / str(item["name"]) for item in sem_records()]
    paths = [
        Path(__file__), ROOT / "srcmap" / "start_build_tohoku_r39.py",
        ROOT / "srcmap" / "start_build_tohoku_r39.ps1",
        *[SOURCE / name for name in EXPECTED_SOURCE],
        *[SEM_QA / name for name in EXPECTED_SEM_QA],
        *[item[0] for item in EXPECTED_REPAIR_RECEIPTS.values()],
        *[AUTHORITY / name for name in EXPECTED_AUTHORITY],
        *semantic,
    ]
    if fresh:
        paths.extend(ROOT / name for name in EXPECTED_TOOLS)
        paths.extend(ROOT / name for name in expected_tex_hashes())
        paths.extend(ROOT / name for name in EXPECTED_ARTIFACTS)
    elif TARGET.exists():
        paths.extend(path for path in TARGET.iterdir() if path.is_file())
    return paths


def verify_execution_attestation() -> dict[str, object]:
    attestation = globals().get("EXECUTION_ATTESTATION")
    if not isinstance(attestation, dict) or set(attestation) != {"bootstrap", "builder"}:
        raise RuntimeError("Run through start_build_tohoku_r39.py")
    bootstrap = attestation.get("bootstrap")
    if bootstrap != {
        "path": "srcmap/start_build_tohoku_r39.py",
        "contract": "read_once_then_execute_builder_same_bytes",
    }:
        raise RuntimeError("Bootstrap attestation drift")
    builder = attestation.get("builder")
    if not isinstance(builder, dict) or set(builder) != {
        "path", "bytes", "sha256", "contract"
    }:
        raise RuntimeError("Builder attestation shape drift")
    if (
        builder.get("path") != "srcmap/build_tohoku_r39.py"
        or builder.get("contract") != "read_hash_compile_and_exec_same_payload"
        or identity(Path(__file__)) != (builder.get("bytes"), builder.get("sha256"))
    ):
        raise RuntimeError("Same-bytes builder attestation drift")
    return attestation


def verify_semantic_and_repair_chain() -> None:
    sem_check = strict_json(SEM_QA / "sem-check.json")
    if (
        sem_check.get("status") != "PASS"
        or sem_check.get("errors") != []
        or sem_check.get("semantic_root") != "sem/r14"
        or sem_check.get("input_manifest") != {
            "name": "qa/v68r33/sem-input.json",
            "bytes": EXPECTED_SEM_QA["sem-input.json"][0],
            "sha256": EXPECTED_SEM_QA["sem-input.json"][1],
        }
    ):
        raise RuntimeError("Semantic check chain drift")
    if sem_check.get("manifest") != {
        "name": "sem/r14/manifest.json",
        "bytes": 6546,
        "sha256": "38CEF77FD45EB826F0E38C95194E37824FBFC99B28A14558E7A6490B7DFDF1DE",
    } or sem_check.get("validation") != {
        "name": "sem/r14/validation.json",
        "bytes": 3918,
        "sha256": "F82C9C8C78F386BC1B7F702F37E19AE5EF27065123930FBA21EC76512CD282DE",
    }:
        raise RuntimeError("Semantic manifest/validation receipt drift")
    validation = strict_json(SEM / "validation.json")
    if validation.get("status") != "PASS" or validation.get("errors") != []:
        raise RuntimeError("Semantic validation is not PASS")

    source = strict_json(P141_SOURCE)
    if (
        source.get("status") != "PASS"
        or source.get("errors") != []
        or source.get("mapping_plan", {}).get("issue") != "I000027"
        or source.get("exact_source_delta", {}).get("selected_reading") != {
            "covariant": "positive components are effaceable; the converse assumes injective effacements",
            "contravariant": "positive components are co-effaceable; the converse assumes projective effacements",
        }
    ):
        raise RuntimeError("p. 141 source-admission chain drift")
    reader = strict_json(READER_QA)
    if (
        reader.get("status") != "PASS"
        or reader.get("errors") != []
        or reader.get("conclusion", {}).get("reader_successor_accepted") is not True
        or reader.get("conclusion", {}).get("blockers") != []
        or reader.get("identities", {}).get("source_admission") != {
            "path": "production/p141_fix1/check.json",
            "bytes": 6579,
            "sha256": "E8936C2A0D376A2B8EC48EB3B1D70DA76927F59112548A168A5589311F2B3658",
        }
    ):
        raise RuntimeError("p. 141 reader-audit chain drift")
    build = strict_json(READER_BUILD)
    if build.get("status") != "PASS" or build.get("errors") != []:
        raise RuntimeError("Reader build receipt is not PASS")

    _, occurrences = load_csv(SEM / "occ.csv")
    occurrence = [row for row in occurrences if row["occurrence_id"] == "tohoku:occ:p141:o003"]
    if occurrence != [{
        **occurrence[0],
        "decision_path": "production/p141_fix1/decisions.jsonl",
        "dip_sha256": "FB74732C022BB575D0C18C3A290D011A7F25B4816D261FFB25F3C04E8685E7B7",
        "fr_sha256": "25C4E4FCE69BA7010D18B00ADBA1E9E6A4C1BE47E82F6636A57C5C4A1BAF0164",
        "en_sha256": "862EF7EB7B57062D8035D66BA140E85D62E51761D4CB7C20F678646AEAF804CE",
        "parity_state": "PASS",
    }]:
        raise RuntimeError("p. 141 semantic occurrence drift")


def verify_inputs(fresh: bool) -> tuple[dict[str, object], bytes]:
    require_plain_directory(SOURCE)
    source_names = {path.name for path in SOURCE.iterdir() if path.is_file()}
    if source_names != set(EXPECTED_SOURCE) or any(path.is_dir() for path in SOURCE.iterdir()):
        raise RuntimeError("Predecessor dossier surface drift")
    for name, expected in EXPECTED_SOURCE.items():
        require_identity(SOURCE / name, expected)
    source_records_now = [record(SOURCE / name) for name in sorted(EXPECTED_SOURCE)]
    if (
        len(source_records_now),
        sum(int(item["bytes"]) for item in source_records_now),
        aggregate(source_records_now),
    ) != EXPECTED_SOURCE_SURFACE:
        raise RuntimeError("Predecessor dossier aggregate drift")
    predecessor = strict_json(SOURCE / "r38-check.json")
    if predecessor.get("status") != "PASS" or predecessor.get("errors") != []:
        raise RuntimeError("Predecessor receipt is not PASS")

    for name, expected in EXPECTED_SEM_QA.items():
        require_identity(SEM_QA / name, expected)
    for path, size, sha256 in EXPECTED_REPAIR_RECEIPTS.values():
        require_identity(path, (size, sha256))
    for name, expected in EXPECTED_AUTHORITY.items():
        require_identity(AUTHORITY / name, expected)

    semantic = sem_records()
    if {path.name for path in SEM.iterdir() if path.is_file()} != {
        str(item["name"]) for item in semantic
    } or any(path.is_dir() for path in SEM.iterdir()):
        raise RuntimeError("Semantic directory surface drift")
    current_semantic: list[dict[str, object]] = []
    for item in semantic:
        path = SEM / str(item["name"])
        require_identity(path, (int(item["bytes"]), str(item["sha256"])))
        current_semantic.append(record(path))
    if aggregate(current_semantic) != SEMANTIC_SURFACE[2]:
        raise RuntimeError("Semantic aggregate drift")
    verify_semantic_and_repair_chain()

    if fresh:
        for name, expected in EXPECTED_TOOLS.items():
            require_identity(ROOT / name, expected)
        for name, expected in EXPECTED_ARTIFACTS.items():
            require_identity(ROOT / name, expected)
        tex_hashes = expected_tex_hashes()
        live_names = {path.name for path in ROOT.glob("*.tex")}
        if live_names != set(tex_hashes):
            raise RuntimeError("Live TeX filename surface differs from the frozen 119-file manifest")
        for name, sha256 in tex_hashes.items():
            require_plain_file(ROOT / name)
            if identity(ROOT / name)[1] != sha256:
                raise RuntimeError(f"Live TeX identity drift: {name}")
        if sys.version_info[:3] != (3, 13, 9) or sys.implementation.cache_tag != "cpython-313":
            raise RuntimeError("Python runtime drift")
    return dict(EXPECTED_GIT_NONCLAIM), b""


def make_config() -> dict:
    cfg = strict_json(SOURCE / "cfg.json")
    cfg["dossier_id"] = "tohoku_r39"
    cfg["inputs"]["primary"] = {
        **record(SEM / "nodes.csv", "nodes.csv"),
        "filename": "nodes.csv",
        "source_file": "sem/r14/nodes.csv",
    }
    for key, filename in (
        ("edges", "edges.csv"),
        ("terms", "terms.csv"),
        ("stacks", "stacks.csv"),
    ):
        cfg["inputs"][key] = {
            **record(SEM / filename, filename),
            "filename": filename,
        }
    cfg["inputs"]["sem_manifest"] = {
        **record(SEM / "manifest.json", "sem/r14 manifest"),
        "filename": "manifest.json",
    }
    cfg["inputs"]["sem_validation"] = {
        **record(SEM / "validation.json", "sem/r14 validation"),
        "filename": "validation.json",
    }
    cfg["inputs"]["sem_input"] = {
        **record(SEM_QA / "sem-input.json", "v68r33 sem input"),
        "filename": "sem-input.json",
    }
    cfg["inputs"]["sem_check"] = {
        **record(SEM_QA / "sem-check.json", "v68r33 sem check"),
        "filename": "sem-check.json",
    }
    cfg["semantic_successor"] = {
        "generation": "sem/r14",
        "surface_files": SEMANTIC_SURFACE[0],
        "surface_bytes": SEMANTIC_SURFACE[1],
        "surface_sha256": SEMANTIC_SURFACE[2],
        "receipt": record(SEM_QA / "sem-check.json", "qa/v68r33/sem-check.json"),
    }
    return cfg


def make_decisions() -> bytes:
    fields, rows = load_csv(SOURCE / "dec.csv")
    if [row["decision_id"] for row in rows] != [
        f"D{number:06d}" for number in range(1, 993)
    ] or rows[-1]["decision_id"] != "D000992":
        raise RuntimeError("Predecessor decision sequence drift")
    prior = [row for row in rows if row["unit_id"] == "tohoku:prop:2.2.1"][-1]
    if prior["decision_id"] != "D000731" or prior["disposition"] != "existing_weaker":
        raise RuntimeError("D000993 predecessor decision drift")
    appended = csv_bytes(fields, DECISION_ROWS)
    return (SOURCE / "dec.csv").read_bytes() + appended[appended.index(b"\n") + 1 :]


def make_issues() -> bytes:
    fields, rows = load_csv(SOURCE / "issues.csv")
    if [row["issue_id"] for row in rows] != [
        f"I{number:06d}" for number in range(1, 27)
    ] or any(row["status"] != "resolved" for row in rows):
        raise RuntimeError("Predecessor source-issue sequence drift")
    appended = csv_bytes(fields, ISSUE_ROWS)
    return (SOURCE / "issues.csv").read_bytes() + appended[appended.index(b"\n") + 1 :]


def run_tool(name: str, *args: str) -> None:
    relative = f"srcmap/{name}"
    require_identity(ROOT / relative, EXPECTED_TOOLS[relative])
    subprocess.run(
        [sys.executable, "-I", "-B", str(ROOT / relative), *args],
        cwd=ROOT,
        check=True,
    )
    require_identity(ROOT / relative, EXPECTED_TOOLS[relative])


def intake_args() -> list[str]:
    specs = [
        ("part_i", AUTHORITY / "jstage_part_I_9_2_119.pdf"),
        ("part_ii", AUTHORITY / "jstage_part_II_9_3_185.pdf"),
        ("edges", SEM / "edges.csv"),
        ("terms", SEM / "terms.csv"),
        ("stacks", SEM / "stacks.csv"),
        ("sem_manifest", SEM / "manifest.json"),
        ("sem_validation", SEM / "validation.json"),
        ("sem_input", SEM_QA / "sem-input.json"),
        ("sem_check", SEM_QA / "sem-check.json"),
    ]
    output: list[str] = []
    for key, path in specs:
        output += ["--extra", f"{key}={path}"]
    return output


def expected_build_receipt() -> dict[str, object]:
    builds: dict[str, object] = {}
    for chapter, spec in BUILD_SPECS.items():
        build: dict[str, object] = {
            "tex": constant_record(f"{chapter}.tex", EXPECTED_ARTIFACTS[f"{chapter}.tex"]),
            "log": constant_record(f"{chapter}.log", EXPECTED_ARTIFACTS[f"{chapter}.log"]),
            "pdf": constant_record(f"{chapter}.pdf", EXPECTED_ARTIFACTS[f"{chapter}.pdf"]),
            "pdf_pages": spec["pdf_pages"],
            "undefined_references": 0,
            "undefined_citations": 0,
            "rerun_notices": 0,
            "new_block_overfull_boxes": 0,
            "visual_reviewed_pages": spec["visual_reviewed_pages"],
        }
        if chapter == "homology":
            build["aux"] = constant_record("homology.aux", EXPECTED_ARTIFACTS["homology.aux"])
        builds[chapter] = build
    return builds


def verify_builds() -> dict[str, object]:
    forbidden = [
        r"(?m)^!", r"(?m)^LaTeX Warning:", r"(?m)^Package .* Warning:",
        r"undefined references", r"undefined citations",
        r"Rerun to get cross-references right", r"Label\(s\) may have changed",
    ]
    for name, expected in EXPECTED_ARTIFACTS.items():
        require_identity(ROOT / name, expected)
    for chapter, spec in BUILD_SPECS.items():
        text = (ROOT / f"{chapter}.log").read_text(encoding="utf-8", errors="replace")
        hits = [pattern for pattern in forbidden if re.search(pattern, text)]
        if hits:
            raise RuntimeError(f"{chapter} build diagnostics failed: {hits}")
        output = re.findall(
            rf"Output written on {re.escape(chapter)}\.pdf \(([0-9]+) pages?, ([0-9]+) bytes\)\.",
            text,
        )
        if output != [(str(spec["pdf_pages"]), str(EXPECTED_ARTIFACTS[f"{chapter}.pdf"][0]))]:
            raise RuntimeError(f"{chapter} output-page receipt drift: {output}")
    aux_lines = set((ROOT / "homology.aux").read_text(encoding="utf-8").splitlines())
    if any(line not in aux_lines for line in EXPECTED_AUX_LABEL_LINES):
        raise RuntimeError("Pinned Homology AUX label/page evidence drift")
    return expected_build_receipt()


def expected_intake_receipt(root: Path) -> dict[str, object]:
    return {
        "schema": "historical-source-intake-v1",
        "corpus": "Tohoku",
        "adapter": "tohoku_nodes",
        "status": "PASS",
        "errors": [],
        "inputs": [
            record(SEM / "nodes.csv"),
            record(AUTHORITY / "jstage_part_I_9_2_119.pdf"),
            record(AUTHORITY / "jstage_part_II_9_3_185.pdf"),
            record(SEM / "edges.csv"),
            record(SEM / "terms.csv"),
            record(SEM / "stacks.csv"),
            record(SEM / "manifest.json"),
            record(SEM / "validation.json"),
            record(SEM_QA / "sem-input.json"),
            record(SEM_QA / "sem-check.json"),
        ],
        "counts": {"units": 990, "units_with_topics": 491},
        "outputs": {
            "units.csv": {
                "bytes": identity(root / "units.csv")[0],
                "sha256": identity(root / "units.csv")[1],
            }
        },
    }


def expected_scan_warnings() -> list[str]:
    old = strict_json(SOURCE / "check.json")["warnings"]
    if len(old) < 9 or any(
        not value.startswith("generated book label is outside chapter TeX:")
        for value in old[:9]
    ):
        raise RuntimeError("Predecessor warning prefix drift")
    additions = [
        f"TeX label has no official tag in this snapshot: {label}"
        for label in NEW_LOCAL_LABELS
    ]
    return [*old[:9], *sorted([*old[9:], *additions])]


def verify_deltas(root: Path) -> dict[str, object]:
    intake = strict_json(root / "intake.json")
    check = strict_json(root / "check.json")
    mcheck = strict_json(root / "mcheck.json")
    for name, receipt in (("intake", intake), ("scan", check), ("map", mcheck)):
        if receipt.get("status") != "PASS" or receipt.get("errors") != []:
            raise RuntimeError(f"{name} receipt is not PASS")
    if mcheck.get("outputs_promoted") is not True:
        raise RuntimeError("Mapping outputs were not promoted")
    actual_outputs = {name: identity(root / name) for name in sorted(PAYLOAD)}
    if actual_outputs != EXPECTED_OUTPUTS:
        raise RuntimeError(f"Canonical output identity drift: {actual_outputs}")
    output_surface = [record(root / name) for name in sorted(PAYLOAD)]
    if (
        len(output_surface),
        sum(int(item["bytes"]) for item in output_surface),
        aggregate(output_surface),
    ) != EXPECTED_OUTPUT_SURFACE:
        raise RuntimeError("Canonical output aggregate drift")
    if strict_json(root / "cfg.json") != make_config():
        raise RuntimeError("Configuration does not exactly bind sem/r14")
    if intake != expected_intake_receipt(root):
        raise RuntimeError("Intake receipt differs from the exact sem/r14 successor")
    if (root / "STATUS.md").read_bytes() != STATUS_BYTES:
        raise RuntimeError("Status bytes drift")
    for name in ("topics.csv", "tmap.csv", "ucand.csv"):
        if (root / name).read_bytes() != (SOURCE / name).read_bytes():
            raise RuntimeError(f"Unexpected byte drift: {name}")

    old_unit_fields, old_units = load_csv(SOURCE / "units.csv")
    new_unit_fields, new_units = load_csv(root / "units.csv")
    if old_unit_fields != new_unit_fields or len(new_units) != 990:
        raise RuntimeError("Unit field/count surface drift")
    if [row["id"] for row in new_units] != [row["id"] for row in old_units]:
        raise RuntimeError("Unit ID/order drift")
    title_changes: list[dict[str, str]] = []
    source_file_transitions = 0
    for old_row, new_row in zip(old_units, new_units, strict=True):
        changed = {field for field in old_row if old_row[field] != new_row[field]}
        expected = {"source_file"}
        if new_row["id"] == "tohoku:prop:2.2.1":
            expected.add("title_en")
            if new_row["title_en"] != EXPECTED_P141_TITLE:
                raise RuntimeError("Corrected p. 141 generated title drift")
            title_changes.append({
                "unit_id": new_row["id"],
                "old_title_en": old_row["title_en"],
                "new_title_en": new_row["title_en"],
            })
        if changed != expected:
            raise RuntimeError(f"Unexpected unit delta {new_row['id']}: {sorted(changed)}")
        if old_row["source_file"] != "sem/r13/nodes.csv" or new_row["source_file"] != "sem/r14/nodes.csv":
            raise RuntimeError(f"Unexpected semantic source transition: {new_row['id']}")
        source_file_transitions += 1
    if len(title_changes) != 1 or source_file_transitions != 990:
        raise RuntimeError("Semantic unit-transition cardinality drift")

    old_dec = (SOURCE / "dec.csv").read_bytes()
    new_dec = (root / "dec.csv").read_bytes()
    if not new_dec.startswith(old_dec) or new_dec != make_decisions():
        raise RuntimeError("Decision ledger is not the exact append-only successor")
    _, decisions = load_csv(root / "dec.csv")
    if [row["decision_id"] for row in decisions] != [
        f"D{number:06d}" for number in range(1, 994)
    ] or decisions[-1:] != DECISION_ROWS:
        raise RuntimeError("D000993 decision sequence/row drift")

    old_issues = (SOURCE / "issues.csv").read_bytes()
    new_issues = (root / "issues.csv").read_bytes()
    if not new_issues.startswith(old_issues) or new_issues != make_issues():
        raise RuntimeError("Source-issue ledger is not the exact append-only successor")
    _, issues = load_csv(root / "issues.csv")
    if [row["issue_id"] for row in issues] != [
        f"I{number:06d}" for number in range(1, 28)
    ] or issues[-1:] != ISSUE_ROWS:
        raise RuntimeError("I000027 issue sequence/row drift")
    active_issues = [row["issue_id"] for row in issues if row["status"] != "resolved"]
    if active_issues:
        raise RuntimeError(f"Unexpected active source issues: {active_issues}")

    if check.get("counts") != EXPECTED_SCAN_COUNTS:
        raise RuntimeError(f"Scan counts drift: {check.get('counts')}")
    if check.get("tex_sha256") != expected_tex_hashes():
        raise RuntimeError("TeX hash dictionary drift")
    if check.get("sha256", {}).get("tags/tags") != EXPECTED_TOOLS["tags/tags"][1]:
        raise RuntimeError("Tags hash drift in scan receipt")
    old_check = strict_json(SOURCE / "check.json")
    expected_check = json.loads(json.dumps(old_check))
    expected_check["counts"] = EXPECTED_SCAN_COUNTS
    expected_check["warnings"] = expected_scan_warnings()
    expected_check["tex_sha256"] = expected_tex_hashes()
    expected_check["sha256"] = {
        key.replace("tohoku_r38/", "tohoku_r39/"): value
        for key, value in old_check["sha256"].items()
    }
    for name in ("topics.csv", "stx.csv", "tcand.csv", "tmap.csv"):
        expected_check["sha256"][f"tohoku_r39/{name}"] = identity(root / name)[1]
    if check != expected_check:
        raise RuntimeError("Scan receipt is not the exact bounded four-label successor")

    _, old_stx = load_csv(SOURCE / "stx.csv")
    _, new_stx = load_csv(root / "stx.csv")
    old_stx_by_label = {row["full_label"]: row for row in old_stx}
    new_stx_by_label = {row["full_label"]: row for row in new_stx}
    if len(old_stx_by_label) != len(old_stx) or len(new_stx_by_label) != len(new_stx):
        raise RuntimeError("Stacks index full-label uniqueness drift")
    if tuple(sorted(set(new_stx_by_label) - set(old_stx_by_label))) != NEW_LOCAL_LABELS:
        raise RuntimeError("Stacks index added-label surface drift")
    if set(old_stx_by_label) - set(new_stx_by_label):
        raise RuntimeError("Stacks index unexpectedly dropped labels")
    for label, expected in EXPECTED_NEW_LABEL_ROWS.items():
        row = new_stx_by_label[label]
        if (
            row["tag"] != ""
            or row["chapter"] != "Homological Algebra"
            or row["section_title"] != "Cohomological delta-functors"
            or any(row[field] != value for field, value in expected.items())
        ):
            raise RuntimeError(f"New Stacks index row drift: {label}")
    index_line_shifts: list[str] = []
    for label in sorted(set(old_stx_by_label) & set(new_stx_by_label)):
        old_row = old_stx_by_label[label]
        new_row = new_stx_by_label[label]
        changed = {field for field in old_row if old_row[field] != new_row[field]}
        if changed:
            if changed != {"line"} or int(new_row["line"]) - int(old_row["line"]) != 577:
                raise RuntimeError(f"Unexpected Stacks index row shift: {label}")
            index_line_shifts.append(label)
    if len(index_line_shifts) != 168:
        raise RuntimeError(f"Stacks index line-shift count drift: {len(index_line_shifts)}")

    _, old_tcand = load_csv(SOURCE / "tcand.csv")
    _, new_tcand = load_csv(root / "tcand.csv")
    old_tcand_by_key = {(row["topic_id"], row["full_label"]): row for row in old_tcand}
    new_tcand_by_key = {(row["topic_id"], row["full_label"]): row for row in new_tcand}
    if len(old_tcand_by_key) != len(old_tcand) or len(new_tcand_by_key) != len(new_tcand):
        raise RuntimeError("Topic-candidate key uniqueness drift")
    candidate_added = tuple(sorted(set(new_tcand_by_key) - set(old_tcand_by_key)))
    candidate_dropped = tuple(sorted(set(old_tcand_by_key) - set(new_tcand_by_key)))
    if candidate_added != EXPECTED_TOPIC_CANDIDATE_ADDED or candidate_dropped:
        raise RuntimeError(f"Topic-candidate churn drift: {candidate_added}, {candidate_dropped}")
    for key in candidate_added:
        row = new_tcand_by_key[key]
        label = key[1]
        if (
            row["score"] != "71"
            or row["hit_fields"] != "section"
            or row["tag"] != ""
            or row["file"] != "homology.tex"
            or row["line"] != EXPECTED_NEW_LABEL_ROWS[label]["line"]
            or row["kind"] != EXPECTED_NEW_LABEL_ROWS[label]["kind"]
            or row["section_title"] != "Cohomological delta-functors"
            or row["status"] != "lexical_candidate_only"
        ):
            raise RuntimeError(f"Added topic-candidate row drift: {key}")
    candidate_line_shifts: list[tuple[str, str]] = []
    for key in sorted(set(old_tcand_by_key) & set(new_tcand_by_key)):
        old_row = old_tcand_by_key[key]
        new_row = new_tcand_by_key[key]
        changed = {field for field in old_row if old_row[field] != new_row[field]}
        if changed:
            if changed != {"line"} or int(new_row["line"]) - int(old_row["line"]) != 577:
                raise RuntimeError(f"Unexpected topic-candidate row shift: {key}")
            candidate_line_shifts.append(key)
    if len(candidate_line_shifts) != 89:
        raise RuntimeError(f"Topic-candidate line-shift count drift: {len(candidate_line_shifts)}")

    old_map_fields, old_map = load_csv(SOURCE / "map.csv")
    new_map_fields, new_map = load_csv(root / "map.csv")
    if old_map_fields != new_map_fields or [row["unit_id"] for row in new_map] != [
        row["unit_id"] for row in old_map
    ]:
        raise RuntimeError("Map field/unit surface drift")
    decision = DECISION_ROWS[0]
    substantive: list[str] = []
    source_loc_transitions = 0
    for old_row, new_row in zip(old_map, new_map, strict=True):
        changed = {field for field in old_row if old_row[field] != new_row[field]}
        expected_changed = {"source_loc"}
        if new_row["unit_id"] == decision["unit_id"]:
            expected_changed |= {
                "decision_id", "disposition", "review_state", "stacks_labels",
                "stacks_tags", "rationale",
            }
            expected_values = {
                "decision_id": decision["decision_id"],
                "disposition": decision["disposition"],
                "review_state": decision["review_state"],
                "stacks_labels": decision["stacks_labels"],
                "stacks_tags": "",
                "rationale": decision["rationale"],
            }
            if any(new_row[field] != value for field, value in expected_values.items()):
                raise RuntimeError("Map row does not exactly realize D000993")
            substantive.append(new_row["unit_id"])
        if changed != expected_changed:
            raise RuntimeError(f"Unexpected map delta {new_row['unit_id']}: {sorted(changed)}")
        if not old_row["source_loc"].startswith("sem/r13/nodes.csv:") or not new_row[
            "source_loc"
        ].startswith("sem/r14/nodes.csv:"):
            raise RuntimeError(f"Unexpected map source-location transition: {new_row['unit_id']}")
        if old_row["source_loc"].split(":")[-1] != new_row["source_loc"].split(":")[-1]:
            raise RuntimeError(f"Semantic line-number transition drift: {new_row['unit_id']}")
        source_loc_transitions += 1
    if substantive != ["tohoku:prop:2.2.1"] or source_loc_transitions != 990:
        raise RuntimeError("Substantive/source-location map delta cardinality drift")
    d216 = [row for row in new_map if row["unit_id"] == "tohoku:thm:2.2.2:p2"]
    if len(d216) != 1 or any(
        d216[0][field] != value for field, value in {
            "decision_id": "D000216",
            "disposition": "new_statement",
            "review_state": "reviewed_new_statement",
            "stacks_labels": "",
            "stacks_tags": "",
            "rationale": (
                "The half-exactness plus nested-subobject kernel criterion for exactness of "
                "the satellite delta-functor is not stated in local Stacks TeX."
            ),
        }.items()
    ):
        raise RuntimeError("D000216 must remain the exact unmapped new_statement row")

    if mcheck.get("counts") != EXPECTED_MAPPING_COUNTS:
        raise RuntimeError(f"Mapping counts drift: {mcheck.get('counts')}")
    if mcheck.get("warnings") != check.get("warnings"):
        raise RuntimeError("Mapping warning surface differs from scan warnings")
    old_mcheck = strict_json(SOURCE / "mcheck.json")
    expected_mcheck = json.loads(json.dumps(old_mcheck))
    expected_mcheck["counts"] = EXPECTED_MAPPING_COUNTS
    expected_mcheck["warnings"] = expected_scan_warnings()
    expected_mcheck["sha256"] = {
        key.replace("tohoku_r38/", "tohoku_r39/"): value
        for key, value in old_mcheck["sha256"].items()
    }
    for name in (
        "cfg.json", "dec.csv", "intake.json", "issues.csv", "map.csv",
        "ucand.csv", "units.csv",
    ):
        expected_mcheck["sha256"][f"tohoku_r39/{name}"] = identity(root / name)[1]
    if mcheck != expected_mcheck:
        raise RuntimeError("Mapping receipt is not the exact bounded successor")
    _, undecided = load_csv(root / "ucand.csv")
    if undecided:
        raise RuntimeError("Unexpected undecided unit candidates")
    gap_count = sum(
        EXPECTED_MAPPING_COUNTS["dispositions"][name]
        for name in ("existing_weaker", "extend_existing", "new_statement", "new_section")
    )
    if gap_count != 65:
        raise RuntimeError(f"Gap-class arithmetic drift: {gap_count}")

    return {
        "decisions": DECISION_ROWS,
        "resolved_source_issues": ISSUE_ROWS,
        "active_source_issues": active_issues,
        "semantic_title_changes": title_changes,
        "semantic_source_file_transitions": {
            "count": source_file_transitions,
            "from": "sem/r13/nodes.csv",
            "to": "sem/r14/nodes.csv",
        },
        "scan_counts": check["counts"],
        "mapping_counts": mcheck["counts"],
        "substantive_map_changes": substantive,
        "stacks_index_added_labels": list(NEW_LOCAL_LABELS),
        "stacks_index_line_shifts": {"count": len(index_line_shifts), "delta": 577},
        "topic_candidate_churn": {
            "added": [list(key) for key in candidate_added],
            "dropped": [],
            "line_only_shifts": len(candidate_line_shifts),
            "line_delta": 577,
        },
        "unmapped_live_stacks_work": {
            "decision_id": "D000216",
            "unit_id": "tohoku:thm:2.2.2:p2",
            "disposition": "new_statement",
            "labels_present_but_not_mapped": [
                "homology-lemma-right-satellites-exactness-criterion",
                "homology-equation-right-satellites-nested-subobjects",
            ],
        },
        "remaining_gap_class_dispositions": gap_count,
    }


def output_records(root: Path) -> list[dict[str, object]]:
    return [record(root / name) for name in sorted(PAYLOAD)]


def source_records() -> list[dict[str, object]]:
    return [record(SOURCE / name) for name in sorted(EXPECTED_SOURCE)]


def repair_receipt_records() -> list[dict[str, object]]:
    return [
        record(path, name)
        for name, (path, _, _) in sorted(EXPECTED_REPAIR_RECEIPTS.items())
    ]


def execution_receipt(attestation: dict[str, object]) -> dict[str, object]:
    return {
        "attestation": attestation,
        "bootstrap": record(ROOT / "srcmap" / "start_build_tohoku_r39.py"),
        "powershell_envelope": record(ROOT / "srcmap" / "start_build_tohoku_r39.ps1"),
        "dependencies": {
            name: constant_record(name, expected)
            for name, expected in sorted(EXPECTED_TOOLS.items())
        },
        "contract": (
            "same_bytes_bootstrap; exact_inputs_locked_against_write_delete_through_"
            "generation_replay_and_promotion"
        ),
    }


def receipt_payload(
    root: Path,
    git: dict[str, object],
    attestation: dict[str, object],
    deltas: dict[str, object],
    builds: dict[str, object] | None = None,
    execution: dict[str, object] | None = None,
) -> dict[str, object]:
    sources = source_records()
    semantic = [record(SEM / str(item["name"])) for item in sem_records()]
    repairs = repair_receipt_records()
    return {
        "schema": "tohoku-stacks-mapping-successor-r39-v1",
        "status": "PASS",
        "errors": [],
        "predecessor_dossier": {
            "name": "tohoku_r38",
            "files": sources,
            "file_count": len(sources),
            "bytes": sum(int(item["bytes"]) for item in sources),
            "aggregate_sha256": aggregate(sources),
        },
        "semantic_source": {
            "generation": "sem/r14",
            "files": semantic,
            "file_count": len(semantic),
            "bytes": sum(int(item["bytes"]) for item in semantic),
            "aggregate_sha256": aggregate(semantic),
            "sem_input": record(SEM_QA / "sem-input.json", "qa/v68r33/sem-input.json"),
            "sem_check": record(SEM_QA / "sem-check.json", "qa/v68r33/sem-check.json"),
        },
        "p141_variance_repair": {
            "receipts": repairs,
            "file_count": len(repairs),
            "bytes": sum(int(item["bytes"]) for item in repairs),
            "aggregate_sha256": aggregate(repairs),
            "issue_id": "I000027",
            "resolution_decision": "D000993",
        },
        "execution": execution if execution is not None else execution_receipt(attestation),
        "git": git,
        "builds": verify_builds() if builds is None else builds,
        "deltas": deltas,
        "files": output_records(root),
        "nonclaims": [
            "No Git command is executed by this mapping successor.",
            "No Git commit or push is made by this receipt.",
            "No remote-server freshness check is performed.",
            "The Stacks scanner is confined to the exact 119 top-level TeX filenames inherited from the sealed r38 manifest; it performs no recursive workspace scan.",
            "Existing-target replay treats the live Stacks TeX and build artifacts as creation-time evidence bound by the receipt; it does not assert that those external files remain byte-identical later.",
            "The outer-envelope sentinel prevents accidental direct-bootstrap use but is not cryptographic provenance against a same-user forged invocation.",
            "The Stacks scan binds the exact live integrated worktree, not the frozen HEAD tree.",
            "The transaction denies write/delete access to every existing consumed file; hostile same-user mutation of directory namespaces is outside this lock contract.",
            "D000216 remains new_statement and unmapped even though its two live Homology labels are honestly indexed as lexical candidates.",
            "No release, publication, upload, DOI, Zenodo, rights, or whole-paper gate is closed.",
            "65 Tohoku gap-class dispositions remain after D000993.",
            "All 27 recorded source issues are resolved; no active source issue remains.",
        ],
    }


def verify_existing(
    git: dict[str, object], attestation: dict[str, object]
) -> dict[str, object]:
    require_plain_directory(TARGET)
    names = {path.name for path in TARGET.iterdir() if path.is_file()}
    if names != PAYLOAD | {"r39-check.json"} or any(path.is_dir() for path in TARGET.iterdir()):
        raise RuntimeError("Existing r39 dossier surface drift")
    deltas = verify_deltas(TARGET)
    receipt = strict_json(TARGET / "r39-check.json")
    if receipt.get("git") != EXPECTED_GIT_NONCLAIM:
        raise RuntimeError("Existing receipt Git nonclaim drift")
    builds = receipt.get("builds")
    if builds != expected_build_receipt():
        raise RuntimeError("Existing builds receipt drift")
    execution = receipt.get("execution")
    if execution != execution_receipt(attestation):
        raise RuntimeError("Existing execution receipt drift")
    expected = receipt_payload(
        TARGET, receipt["git"], attestation, deltas, builds, execution
    )
    if receipt != expected:
        raise RuntimeError("Existing r39 receipt replay mismatch")
    return receipt


def main_locked(attestation: dict[str, object]) -> int:
    target_entry = os.path.lexists(TARGET)
    stage_entry = os.path.lexists(STAGE)
    if target_entry and stage_entry:
        raise RuntimeError("Target and unresolved transaction coexist")
    if stage_entry:
        raise FileExistsError(f"Unresolved transaction exists: {STAGE}")
    fresh = not target_entry
    with deny_write_delete(lock_paths(fresh)):
        git, _ = verify_inputs(fresh)
        if target_entry:
            receipt = verify_existing(git, attestation)
            print(json.dumps(receipt, ensure_ascii=False, indent=2))
            return 0
        STAGE.mkdir()
        exclusive_write(STAGE / "cfg.json", json_bytes(make_config()))
        exclusive_write(STAGE / "topics.csv", (SOURCE / "topics.csv").read_bytes())
        exclusive_write(STAGE / "dec.csv", make_decisions())
        exclusive_write(STAGE / "issues.csv", make_issues())
        run_tool("intake.py", str(STAGE), str(SEM / "nodes.csv"), *intake_args())
        run_tool("scan.py", str(STAGE))
        run_tool("map.py", str(STAGE))
        exclusive_write(STAGE / "STATUS.md", STATUS_BYTES)
        deltas = verify_deltas(STAGE)
        receipt = receipt_payload(STAGE, git, attestation, deltas)
        exclusive_write(STAGE / "r39-check.json", json_bytes(receipt))
        if (
            {path.name for path in STAGE.iterdir() if path.is_file()}
            != PAYLOAD | {"r39-check.json"}
            or any(path.is_dir() for path in STAGE.iterdir())
        ):
            raise RuntimeError("Staged dossier surface mismatch")
        verify_inputs(True)
        os.rename(STAGE, TARGET)
        with deny_write_delete([path for path in TARGET.iterdir() if path.is_file()]):
            final = verify_existing(git, attestation)
        print(json.dumps(final, ensure_ascii=False, indent=2))
        return 0


def main() -> int:
    attestation = verify_execution_attestation()
    with single_writer_mutex():
        return main_locked(attestation)


if __name__ == "__main__":
    raise SystemExit(main())
