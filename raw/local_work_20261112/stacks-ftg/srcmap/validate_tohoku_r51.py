#!/usr/bin/env python3
"""Independent bounded validator for the frozen no-overwrite Tohoku r51 successor."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import io
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "tohoku_r50"
TARGET = ROOT / "tohoku_r51"
STAGE = ROOT / ".tohoku-r51-txn"
PROJECT = Path(
    r"user\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\03_working_translations"
    r"\tohoku_bilingual_canonical_stacks_20260804_r1"
)
SEM = PROJECT / "sem" / "r18"
AUTHORITY = PROJECT / "authority_snapshot"
BASE_VALIDATOR = ROOT / "srcmap" / "validate_tohoku_r50.py"
BASE_BUILDER = ROOT / "srcmap" / "build_tohoku_r50.py"
EXPECTED_BASE_VALIDATOR = (
    68151,
    "78666A756C7DE8FD64D53200267B0A00359D75C4FD5C0D3056B9ECA9857E1410",
)
EXPECTED_BASE_BUILDER = (
    20043,
    "7FEF70C6EC4EB63E23B30B78B60AE74A7D5312350C0C714BB2197900CB106251",
)
EXPECTED_PYTHON = Path(r"user\miniconda3\python.exe")
EXPECTED_PYTHON_IDENTITY = (
    104264,
    "7679E53FA969789309E81FDAD0D52B8CDA5F83C9ABF7CB31A3C58BF24B31E264",
)

PAYLOAD = {
    "cfg.json", "intake.json", "units.csv", "topics.csv", "dec.csv",
    "issues.csv", "check.json", "stx.csv", "tcand.csv", "tmap.csv",
    "map.csv", "ucand.csv", "mcheck.json", "STATUS.md",
}

EXECUTION_ROLES = {
    "driver": ("srcmap/start_build_tohoku_r51.ps1", "self_read_hash_then_one_shot_bootstrap_envelope"),
    "bootstrap": ("srcmap/start_build_tohoku_r51.py", "one_read_hash_compile_exec_builder_and_pin_validator"),
    "builder": ("srcmap/build_tohoku_r51.py", "read_hash_compile_and_exec_same_payload"),
    "validator": ("srcmap/validate_tohoku_r51.py", "independent_same_bytes_stage_and_receipt_replay"),
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def identity(path: Path) -> tuple[int, str]:
    data = path.read_bytes()
    return len(data), digest(data)


def record(path: Path, name: str | None = None) -> dict[str, object]:
    size, sha256 = identity(path)
    return {"name": name or path.name, "bytes": size, "sha256": sha256}


def aggregate(records: list[dict[str, object]]) -> str:
    data = b"".join(
        f"{item['name']}\0{item['bytes']}\0{item['sha256']}\n".encode("utf-8")
        for item in sorted(records, key=lambda value: str(value["name"]))
    )
    return digest(data)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def is_reparse(path: Path) -> bool:
    return os.name == "nt" and bool(path.stat(follow_symlinks=False).st_file_attributes & 0x400)


def require_plain_file(path: Path) -> None:
    require(path.is_file() and not path.is_symlink() and not is_reparse(path), f"Expected plain file: {path}")


def require_plain_directory(path: Path) -> None:
    require(path.is_dir() and not path.is_symlink() and not is_reparse(path), f"Expected plain directory: {path}")


def require_identity(path: Path, expected: tuple[int, str]) -> None:
    require_plain_file(path)
    require(identity(path) == expected, f"Identity drift: {path}")


def expected_execution_attestation() -> dict[str, dict[str, object]]:
    result: dict[str, dict[str, object]] = {}
    for role, (relative, contract) in EXECUTION_ROLES.items():
        path = ROOT / relative
        require_plain_file(path)
        size, sha256 = identity(path)
        result[role] = {
            "path": relative,
            "bytes": size,
            "sha256": sha256,
            "contract": contract,
        }
    return result


def strict_json(path: Path) -> dict:
    data = path.read_bytes()
    require(b"\r" not in data and data.endswith(b"\n"), f"Noncanonical JSON: {path}")

    def no_duplicates(values: list[tuple[str, object]]) -> dict:
        output: dict[str, object] = {}
        for key, value in values:
            require(key not in output, f"Duplicate JSON key {key}: {path}")
            output[key] = value
        return output

    value = json.loads(data.decode("utf-8"), object_pairs_hook=no_duplicates)
    require(isinstance(value, dict), f"Expected JSON object: {path}")
    return value


def load_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    data = path.read_bytes()
    require(b"\r" not in data and data.endswith(b"\n"), f"Noncanonical CSV: {path}")
    reader = csv.DictReader(data.decode("utf-8-sig").splitlines())
    rows = list(reader)
    require(reader.fieldnames is not None, f"Missing CSV header: {path}")
    require(all(None not in row and None not in row.values() for row in rows), f"Malformed CSV: {path}")
    return list(reader.fieldnames), rows


def csv_bytes(fields: list[str], rows: list[dict[str, str]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, f"Cannot load pinned module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_base_validator():
    require_identity(BASE_VALIDATOR, EXPECTED_BASE_VALIDATOR)
    module = load_module(BASE_VALIDATOR, "tohoku_r51_pinned_r50_validator")
    require_identity(BASE_VALIDATOR, EXPECTED_BASE_VALIDATOR)
    return module


BASE = load_base_validator()


def index_csv_bytes(rows: list[dict[str, str]]) -> bytes:
    fields = [
        "tag", "full_label", "file", "line", "kind", "short_label",
        "chapter", "section_label", "section_title", "text_sha256",
    ]
    return csv_bytes(fields, [{field: row.get(field, "") for field in fields} for row in rows])


def candidate_csv_bytes(rows: list[dict[str, str]]) -> bytes:
    fields = [
        "topic_id", "score", "hit_fields", "tag", "full_label", "file",
        "line", "kind", "section_title", "snippet", "status",
    ]
    return csv_bytes(fields, [{field: row.get(field, "") for field in fields} for row in rows])


def topic_map_csv_bytes(rows: list[dict[str, str]]) -> bytes:
    fields = [
        "topic_id", "label", "coverage", "confidence", "evidence_labels",
        "evidence_tags", "rationale", "review_state",
    ]
    return csv_bytes(fields, [{field: row.get(field, "") for field in fields} for row in rows])


EXPECTED_SOURCE = {
    "STATUS.md": (1510, "2DD206FA249898B9874DEE034A8989EBE6BE0C4E5F7CF134CE33E2353B5594C0"),
    "cfg.json": (5151, "548B310BB355667A7D491A0227DC11D991E85CC37D707FAE66364E33D2CAC3E9"),
    "check.json": (77961, "4064B5D27C17CD702754616EEC4CA8B11D778004068E04B1119360EE3DA10D16"),
    "dec.csv": (368636, "783BAB72C7EEE92D23343F4430D5402781F368F98E4CF559D43B8A902DBC5914"),
    "intake.json": (1578, "8279157B8AA7F6AA006E2C434C34D2A7988836D63C25B3465B93896D62E22801"),
    "issues.csv": (29535, "3439D68823BF69087F025976FB0AC41C2C4D93B8BFB4E63D6FD3267DB6AC178A"),
    "map.csv": (477114, "55307B995E0118F98439B433B60226C02C0C6A961800E269CBC0B29C40631BF4"),
    "mcheck.json": (67789, "FF50E24A0E4B57025837FFAE2F8AAFBC7D0278DDF3C7F2164A3D5C3F6B762740"),
    "r50-check.json": (39748, "C4FA11E0607FC05FBB54FB91FAA1B9C40E1708161078A0F9B9B71431F9AE401C"),
    "stx.csv": (5276137, "C508EA79EB23A25D2911E3174A76AA7ED790947C8876F73817EEE1FEFF99B6BF"),
    "tcand.csv": (485239, "62ABF592201379300DA78F98C91644A4E6747F27F392C9C31AE00FC7AB29361B"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (392568, "3AB04435EEDD9DE59E61DF2443812C2F555DD6CA85542DC7F9C6BBE59DB03081"),
}
EXPECTED_SOURCE_PAYLOAD_SURFACE = (
    14,
    7188215,
    "FF23DDD7812138514D5B8E9E7C59D805ED20852FD70A3BA6055AEA75CBDB49AD",
)
EXPECTED_SOURCE_SURFACE = (
    15,
    7227963,
    "EAA6EC6B54D7B1033629AC9A374E15B5E4F9C96F31B7AF251AEED369EBAE37C8",
)

EXPECTED_SEM = {
    "README.md": (2585, "66D4CF92728AF7FF10E82CDFD97AFCD9D26B55CE9FBC985932FFBCD597DD64B4"),
    "bib.csv": (10422, "93F5A934ADDE0CD92BBB21AF70EFD81BA128CCD2EDF51EB19428B83437EC3516"),
    "catalog.csv": (772, "12C8C0D5EB10157AB1DBCD170AFF2147103AB848A3D28A8CA9EDF1C15186540A"),
    "edges.csv": (260944, "F1607445D52F28DA2F3FE93D8F47D7959C35ECFFBC167B5AB0E787A91264C719"),
    "idmap.csv": (473, "977D4A8F59A9642D58926DED8BB600079863AE6AF3F1F532806E83A9AB645BEA"),
    "manifest.json": (38138, "40596FD03A707CF8AC3C1D825D0FEAD4447663F6A57E7BD16735021F14B520AB"),
    "nodes.csv": (585012, "3A3C9B6C22B0FA5E16466C264205D97CCA6041FF785F555A4C28F9639A50550D"),
    "objects.csv": (106319, "82FF34C19C6D17D80DC3A617FD106ED324099CC9D0F2FE752757D0642ED31999"),
    "occ.csv": (515084, "54E545121F4D108E5C88B7039C39E3814F71F03332592C3F3965BD49B7FACED5"),
    "pages.csv": (23686, "E813C410B0A2AE53B4A787FD6C66A74225021E3A0FE22AD10CA2ED0C29807B0D"),
    "refdec.csv": (2313, "6AC5E23C3D4ADA0ABB1427E0533C3033E13B63C28A654A9C7E74A057A045FFA2"),
    "refs.csv": (159815, "995C9526CEC36FB6B437D7C688E4D40547BFC050949E3819A607FEEF53EA1162"),
    "resid.csv": (6415, "DDF53E58E21C7A5BF60C54ADC5EB9EB420B717246F1C69F294BBA5E358A38430"),
    "stacks.csv": (11777, "E13EFA405B525D69BFF38256601E4AF64D22FA3075F3A95AB3DFB78C15CFD060"),
    "subjects.csv": (2133, "A77A81831F752BA21701B150C13C51325E511B2FD5DFC76EED135FE3EDEEB026"),
    "terms.csv": (325587, "6D93CBBD2D6CF3E354FE90DC51605ACD9C7B0932CEF216FB9D606AD97D666E5D"),
    "validation.json": (6102, "2972E56494357AD0ABDB765057E20CA99777E6A6AA73B5AF7571EA1F715AA3D4"),
    "xwork.csv": (2446, "7BC42D7026C34AD8B1A111353E0810378F1DB9D1284BAD4C5C34D509D57B9EBB"),
}
EXPECTED_SEM_SURFACE = (18, 2060023, "76B6EBA7042FCFF59306E6178AC702BFDEDA392D2ADD754DDE932EBFAA6E6302")
EXPECTED_SEM_PAYLOAD_SURFACE = (16, 2015783, "71906EBD41B1777C661B904510BAC999FB5827E018CD1C606CE5007DFD0B9EB7")

D1008_AUDIT = ROOT / "D1008_CHECK.json"
EXPECTED_D1008_AUDIT = (
    17532,
    "BD044C06451F0C9634331F5925630735D66C1DE357B303A2035E1E62A19B3039",
)

COHOMOLOGY_ARTIFACTS = {
    "cohomology.tex": (859582, "A7421C2A20D1D2E9DEE9CB85D7EEA352CE72A22FC87D1CB0AE2DAE95EB6F087D"),
    "cohomology.aux": (52735, "C79B4B893964006BD4D0925BEED17647FF45E24385352124BC872AC3398275B8"),
    "cohomology.log": (47357, "72BB25C32FF9ADF9495726C10B148589089B5B0BC1CC84F3B421E4F327CE7947"),
    "cohomology.pdf": (1894087, "FEC0804EAEAE6AB3243EA1D7CB32EB0A791D05C4EE4A786A39B647D2951B2CAF"),
}

P214_SOURCE_ARTIFACTS = {
    "admission": (PROJECT / "production" / "p214_fix1" / "check.json", 5865, "516012842CD8F6026ABE418370229A1AAB91C6087DDC6C921931DF0716122B1B"),
    "decisions": (PROJECT / "production" / "p214_fix1" / "decisions.jsonl", 4708, "7E077B3C73B3FFEBA178F24E82495FC8FEEFE686136C401A67129BF9AD94636D"),
    "targets": (PROJECT / "production" / "p214_fix1" / "targets.csv", 962, "A2544B6A2E1E219B0F93F2CBAC892762EDE5EC7F01EA4B3FA2971534BF6EFE52"),
    "reuse": (PROJECT / "production" / "p214_fix1" / "reuse.txt", 46, "FD198429609353509A64055B73D7BCC6BA648602D827C7C6084C445ECB5DA4BB"),
    "english": (PROJECT / "production" / "p214_fix1" / "tex" / "en" / "p214.tex", 4011, "8CFFB05104DA4BB64C1AE7340C36D3FAC977A459C4BF8A8DFD6EFB1461B539F1"),
    "corrected_french": (PROJECT / "production" / "p214_fix1" / "tex" / "fr_corrected" / "p214.tex", 4215, "90416161FE153DE6E14DDF9F854AB9EDA38292BB8158A6318D410498D8068CC9"),
    "diplomatic_french": (PROJECT / "production" / "p214_fix1" / "tex" / "fr_diplomatic" / "p214.tex", 4198, "94A45ECBA2E990F4D84C60A662219B35AD483F8B4EAC3A8E6ACDAA3B013D72D7"),
}

READER_ARTIFACTS = {
    "build_receipt": (PROJECT / "build" / "v068c3r17" / "build.json", 30957, "6A7E647F3BEDCBAC4E7538D56F83830CB2BC134F124AC257D9E64662A8D0C380"),
    "english_build_pdf": (PROJECT / "build" / "v068c3r17" / "en" / "main-en.pdf", 1380477, "4E692072301E46CF910FA2C73C6B4B9FB594895B73305F4368298A34D75BAE24"),
    "french_build_pdf": (PROJECT / "build" / "v068c3r17" / "fr" / "main-fr.pdf", 1415621, "914EA7C087A07727D2F0C24A8CB646378A3B714C8CFADDF4FDF7854733BFB51E"),
    "english_output_pdf": (PROJECT / "output" / "pdf" / "en-p119-221-v068c3r17.pdf", 1380477, "4E692072301E46CF910FA2C73C6B4B9FB594895B73305F4368298A34D75BAE24"),
    "french_output_pdf": (PROJECT / "output" / "pdf" / "fr-p119-221-v068c3r17.pdf", 1415621, "914EA7C087A07727D2F0C24A8CB646378A3B714C8CFADDF4FDF7854733BFB51E"),
    "english_aux": (PROJECT / "build" / "v068c3r17" / "en" / "main-en.aux", 3222, "D7ACF7D64E2CC77E80BD7847D615B70D6383D280948C72BF338F1BD1491EBE06"),
    "english_log": (PROJECT / "build" / "v068c3r17" / "en" / "main-en.log", 34932, "2547B7616FDEDD25374A123903D15D392210B54C85060712087C95CC67FE669D"),
    "french_aux": (PROJECT / "build" / "v068c3r17" / "fr" / "main-fr.aux", 3413, "ED459F78C2E9D0EC5B8248638BF1B94E3164711271B2468A53060E39DB4157D0"),
    "french_log": (PROJECT / "build" / "v068c3r17" / "fr" / "main-fr.log", 35057, "800179E31647DE1F5E317B96346EACD9EDFDBC42DB8953CE503F7EB1ABA44D00"),
    "english_p214": (PROJECT / "build" / "v068c3r17" / "src" / "en" / "p214.tex", 4011, "8CFFB05104DA4BB64C1AE7340C36D3FAC977A459C4BF8A8DFD6EFB1461B539F1"),
    "english_p215": (PROJECT / "build" / "v068c3r17" / "src" / "en" / "p215.tex", 4468, "0DA8E1C00F154542963645DC1EDB339ED5E35A14B3B1ABFAFE44DFA478AF1852"),
    "french_p214": (PROJECT / "build" / "v068c3r17" / "src" / "fr" / "p214.tex", 4215, "90416161FE153DE6E14DDF9F854AB9EDA38292BB8158A6318D410498D8068CC9"),
    "french_p215": (PROJECT / "build" / "v068c3r17" / "src" / "fr" / "p215.tex", 4669, "A361CDE261DDA6A09E8EC24E5A73BB5E643944AB3AC43ECAC2AE01C54500FD13"),
}

READER_QA_ARTIFACTS = {
    "check": (PROJECT / "qa" / "v68r39" / "check.json", 4928, "8257A31037F1A6B38F4EACD52CF2AF1E0A0685542D90B61FF34D3B30DE6B9C08"),
    "page_inventory": (PROJECT / "qa" / "v68r39" / "page-inventory.csv", 28157, "D2BAA767743D678D677808A5ACC5576AF2070EC0AB0033F0ADCB2952C1023FD9"),
    "structural": (PROJECT / "qa" / "v68r39" / "structural.json", 7308, "9F82C5C75CC4F173B91F7CD001368AB7CF4BB27A4C697862E71BA0D97ECB55DC"),
    "english_predecessor": (PROJECT / "qa" / "v68r39" / "p214-en-r16.png", 479274, "B07CA9C0518BBFE41815613820C75A32279598C870F3D18C77808C27493438EC"),
    "english_successor": (PROJECT / "qa" / "v68r39" / "p214-en-r17.png", 480402, "07FCC7879109581F7D1AC727F0E24D91F52CB0C25530C291CF1A3CBACCC64739"),
    "french_predecessor": (PROJECT / "qa" / "v68r39" / "p214-fr-r16.png", 83674, "762E67C0C7A0DE000FA664A4771EC11329B527B3FB14D603DA63A0F8671923B8"),
    "french_successor": (PROJECT / "qa" / "v68r39" / "p214-fr-r17.png", 82901, "D9A39EAA0310532E35B5AC2B1017AA8F1E01695745EA919B83F556598AEAF792"),
    "french_context": (PROJECT / "qa" / "v68r39" / "p214-fr-r17-page-85.png", 442445, "580DD4669D7AD26E62233BA9AFC75C26D660750DCE124C88C1E7FACD76FC86F4"),
}

NEW_REPAIRS = {
    "SOURCE_CORRECTIONS.jsonl": (208551, "2D99ED4D9F4697A6991405BEFFA5EF755F58F42AFAA17FB4198DA30D806AEF90"),
    "production/p214_fix1/check.json": (5865, "516012842CD8F6026ABE418370229A1AAB91C6087DDC6C921931DF0716122B1B"),
    "production/p214_fix1/decisions.jsonl": (4708, "7E077B3C73B3FFEBA178F24E82495FC8FEEFE686136C401A67129BF9AD94636D"),
    "production/p214_fix1/targets.csv": (962, "A2544B6A2E1E219B0F93F2CBAC892762EDE5EC7F01EA4B3FA2971534BF6EFE52"),
    "production/p214_fix1/reuse.txt": (46, "FD198429609353509A64055B73D7BCC6BA648602D827C7C6084C445ECB5DA4BB"),
    "production/p214_fix1/tex/en/p214.tex": (4011, "8CFFB05104DA4BB64C1AE7340C36D3FAC977A459C4BF8A8DFD6EFB1461B539F1"),
    "production/p214_fix1/tex/fr_corrected/p214.tex": (4215, "90416161FE153DE6E14DDF9F854AB9EDA38292BB8158A6318D410498D8068CC9"),
    "production/p214_fix1/tex/fr_diplomatic/p214.tex": (4198, "94A45ECBA2E990F4D84C60A662219B35AD483F8B4EAC3A8E6ACDAA3B013D72D7"),
    "production/p214_fix1/qa/p214-en.tex": (633, "0AA26AC145CCEE074CFF9A4DB583A7E4566936EE04C3683D92B6A4DFF57419BC"),
    "production/p214_fix1/qa/p214-en.log": (28897, "21B7BF1439BE1BB087CBC153C086D1B976055884965383399B94497568DAD463"),
    "production/p214_fix1/qa/p214-en.pdf": (164248, "8B3BA006E800A5C0EEEA70D824DDB287B4C64E86BFE318CB4239E0C3EAA42ED7"),
    "production/p214_fix1/qa/p214-en-render-1.png": (326867, "63B8ED0D7D0D3DF3DBBF8CF4D3A58F204B0FC4F65AA4AE13932C7EE35791E40F"),
    "production/p214_fix1/qa/p214-fr.tex": (661, "0F22C9249F47C9160B31C6E78A92068CAD1EFD4D391078E4D8F05D07BCF2FB05"),
    "production/p214_fix1/qa/p214-fr.log": (28912, "D826EF561E4729891179A8EB7E0EFF2490D3FF1A38D2CEEF37DF0F96633B8CDC"),
    "production/p214_fix1/qa/p214-fr.pdf": (166777, "94ABCAACD192995DEBEBF4429AF2E61FDD5B44BBAAD0BADCA47BAC31DEA4AF8E"),
    "production/p214_fix1/qa/p214-fr-render-1.png": (298611, "86998530ACE60CB1754BB07E69EF5D493FCD58FD7355F38E7D5B4F404BE75DA1"),
    "production/p214_fix1/qa/p214-fr-render-2.png": (54279, "04D660456CCFC370084F2CF7134E69BC8380E477AB1F97FE02DB1EEFAB0712AE"),
    "build/v068c3r17/build.json": (30957, "6A7E647F3BEDCBAC4E7538D56F83830CB2BC134F124AC257D9E64662A8D0C380"),
    "build/v068c3r17/en/main-en.pdf": (1380477, "4E692072301E46CF910FA2C73C6B4B9FB594895B73305F4368298A34D75BAE24"),
    "build/v068c3r17/fr/main-fr.pdf": (1415621, "914EA7C087A07727D2F0C24A8CB646378A3B714C8CFADDF4FDF7854733BFB51E"),
    "build/v068c3r17/src/en/p214.tex": (4011, "8CFFB05104DA4BB64C1AE7340C36D3FAC977A459C4BF8A8DFD6EFB1461B539F1"),
    "build/v068c3r17/src/en/p215.tex": (4468, "0DA8E1C00F154542963645DC1EDB339ED5E35A14B3B1ABFAFE44DFA478AF1852"),
    "build/v068c3r17/src/fr/p214.tex": (4215, "90416161FE153DE6E14DDF9F854AB9EDA38292BB8158A6318D410498D8068CC9"),
    "build/v068c3r17/src/fr/p215.tex": (4669, "A361CDE261DDA6A09E8EC24E5A73BB5E643944AB3AC43ECAC2AE01C54500FD13"),
    "output/pdf/en-p119-221-v068c3r17.pdf": (1380477, "4E692072301E46CF910FA2C73C6B4B9FB594895B73305F4368298A34D75BAE24"),
    "output/pdf/fr-p119-221-v068c3r17.pdf": (1415621, "914EA7C087A07727D2F0C24A8CB646378A3B714C8CFADDF4FDF7854733BFB51E"),
    "qa/v68r39/check.json": (4928, "8257A31037F1A6B38F4EACD52CF2AF1E0A0685542D90B61FF34D3B30DE6B9C08"),
    "qa/v68r39/page-inventory.csv": (28157, "D2BAA767743D678D677808A5ACC5576AF2070EC0AB0033F0ADCB2952C1023FD9"),
    "qa/v68r39/structural.json": (7308, "9F82C5C75CC4F173B91F7CD001368AB7CF4BB27A4C697862E71BA0D97ECB55DC"),
    "qa/v68r39/p214-en-r16.png": (479274, "B07CA9C0518BBFE41815613820C75A32279598C870F3D18C77808C27493438EC"),
    "qa/v68r39/p214-en-r17.png": (480402, "07FCC7879109581F7D1AC727F0E24D91F52CB0C25530C291CF1A3CBACCC64739"),
    "qa/v68r39/p214-fr-r16.png": (83674, "762E67C0C7A0DE000FA664A4771EC11329B527B3FB14D603DA63A0F8671923B8"),
    "qa/v68r39/p214-fr-r17.png": (82901, "D9A39EAA0310532E35B5AC2B1017AA8F1E01695745EA919B83F556598AEAF792"),
    "qa/v68r39/p214-fr-r17-page-85.png": (442445, "580DD4669D7AD26E62233BA9AFC75C26D660750DCE124C88C1E7FACD76FC86F4"),
}

DECISION_ROWS = [
    {
        "decision_id": "D001017",
        "unit_id": "tohoku:comparison:equivariant-hom-stalk-to-fiber",
        "action": "replace",
        "disposition": "existing_stronger",
        "stacks_labels": "cohomology-lemma-equivariant-hom-injective-stalk",
        "rationale": "Stacks now proves the natural fixed-point stalk comparison in a stronger pointwise local form for a discontinuous action and a possibly noncommutative equivariant ring sheaf: local finite presentation of A near x identifies the stalk at y of invariant direct-image internal Hom with Hom over the skew stabilizer ring R_x crossed with G_x. The same theorem proves injectivity of equivariant-injective stalks under a local left-coherence image condition and left Noetherianity of the single stalk. The comparison is only asserted as an isomorphism of abelian groups, and no module structure on noncommutative internal Hom, right-module analogue, averaging argument, or unrestricted preservation of injectives by stalks is claimed.",
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000570",
    },
    {
        "decision_id": "D001018",
        "unit_id": "tohoku:comparison:equivariant-ext-stalk-to-fiber",
        "action": "replace",
        "disposition": "existing_stronger",
        "stacks_labels": "cohomology-lemma-equivariant-ext-stalk",
        "rationale": "Stacks now proves for every n at a fixed orbit point that the stalk of the derived abelian-sheaf-valued equivariant Hom functor is canonically Ext over the skew stabilizer ring, under local finite-presentation, local left-coherence, and pointwise left-Noetherian hypotheses. In the commutative case it identifies this derived sheaf with the underlying abelian sheaf of the existing equivariant SheafExt construction. This pointwise theorem covers the source's coherent and Noetherian setting without claiming a noncommutative module structure on internal Hom, a right-sided variant, or any comparison outside the stated hypotheses.",
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000569",
    },
]

EXPECTED_MAPPING_COUNTS = {
    "active_graph_corrections": 0,
    "active_source_issues": 0,
    "candidate_units": 0,
    "decided_units": 679,
    "decisions": 1018,
    "dispositions": {
        "example_or_remark": 84,
        "existing_equivalent": 362,
        "existing_stronger": 41,
        "existing_weaker": 6,
        "extend_existing": 22,
        "historical_reference": 33,
        "new_section": 6,
        "new_statement": 13,
        "structural_only": 424,
    },
    "graph_corrections": 0,
    "review_units": 0,
    "source_issues": 29,
    "unit_candidates": 0,
    "units": 991,
}
EXPECTED_SCAN_COUNTS = {
    "labels": 22064,
    "official_tags_joined": 21437,
    "tex_files": 119,
    "topic_candidates": 1270,
    "topic_coverage": {"direct": 13},
    "topics": 13,
}
EXPECTED_SCAN_OUTPUTS = {
    "stx.csv": (5276647, "CF7E76DE52766F75E7174A1D6B56FC5466BA6D0521BAAC317856EDBF8047A1DB"),
    "tcand.csv": (485239, "2CA303980441ABDB51890EA1A2DA3544D604262589A546ACF2DE60F04391916E"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
}
NEW_LABEL_ROWS = {
    "cohomology-lemma-equivariant-hom-injective-stalk": {
        "tag": "",
        "full_label": "cohomology-lemma-equivariant-hom-injective-stalk",
        "file": "cohomology.tex",
        "line": "18452",
        "kind": "lemma",
        "short_label": "lemma-equivariant-hom-injective-stalk",
        "chapter": "Cohomology of Sheaves",
        "section_label": "section-cohomology-group-actions",
        "section_title": "Cohomology with group actions",
        "text_sha256": "C629C98FE2C45D09B6F3B1FFD03E1AD515B079B93BA495F93560C73ACF683D47",
    },
    "cohomology-lemma-equivariant-ext-stalk": {
        "tag": "",
        "full_label": "cohomology-lemma-equivariant-ext-stalk",
        "file": "cohomology.tex",
        "line": "18649",
        "kind": "lemma",
        "short_label": "lemma-equivariant-ext-stalk",
        "chapter": "Cohomology of Sheaves",
        "section_label": "section-cohomology-group-actions",
        "section_title": "Cohomology with group actions",
        "text_sha256": "95D4DEBCF70B94B6A3CC1A1C068FD5B2824569344777B531C19020FD296B9689",
    },
}

EXPECTED_AUTHORITY = {
    "jstage_part_I_9_2_119.pdf": (7305283, "5A8E5720BC2EF8905BF85F7919C65AC4A87A31CFC854BD77E6B5084C0D2DEBEF"),
    "jstage_part_II_9_3_185.pdf": (3984260, "8D632A04EE0FA987B40B721BEE6E64BB3E641D6A1CE02335556213F1564C9A53"),
}


def _valid_identity_pin(expected: tuple[int, str]) -> bool:
    return (
        isinstance(expected[0], int)
        and expected[0] > 0
        and isinstance(expected[1], str)
        and re.fullmatch(r"[0-9A-F]{64}", expected[1]) is not None
    )


def pending_semantic_pins() -> list[str]:
    pending = [
        f"sem/r18/{name}"
        for name, expected in EXPECTED_SEM.items()
        if not _valid_identity_pin(expected)
    ]
    if (
        EXPECTED_SEM_SURFACE[1] <= 0
        or re.fullmatch(r"[0-9A-F]{64}", EXPECTED_SEM_SURFACE[2]) is None
        or EXPECTED_SEM_PAYLOAD_SURFACE[1] <= 0
        or re.fullmatch(r"[0-9A-F]{64}", EXPECTED_SEM_PAYLOAD_SURFACE[2]) is None
    ):
        pending.append("sem/r18 aggregate surfaces")
    return pending


def require_semantic_frozen() -> None:
    pending = pending_semantic_pins()
    require(not pending, "r51 semantic pins remain pending: " + ", ".join(pending))


def require_d1008_frozen() -> None:
    pending = []
    if not _valid_identity_pin(EXPECTED_D1008_AUDIT):
        pending.append("D1008_CHECK.json")
    require(not pending, "r51 D1008 pins remain pending: " + ", ".join(pending))


def require_frozen_inputs() -> None:
    pending = [*pending_semantic_pins()]
    if not _valid_identity_pin(EXPECTED_D1008_AUDIT):
        pending.append("D1008_CHECK.json")
    require(not pending, "r51 is intentionally non-runnable; pending frozen pins: " + ", ".join(pending))


def expected_runtime() -> dict[str, tuple[int, str]]:
    return {
        **BASE.expected_runtime(),
        "srcmap/validate_tohoku_r50.py": EXPECTED_BASE_VALIDATOR,
        "srcmap/build_tohoku_r50.py": EXPECTED_BASE_BUILDER,
    }


def expected_repairs() -> dict[str, tuple[int, str]]:
    return {**BASE.expected_repairs(), **NEW_REPAIRS}


def expected_artifacts() -> dict[str, tuple[int, str]]:
    artifacts = dict(BASE.expected_artifacts())
    artifacts.update(COHOMOLOGY_ARTIFACTS)
    return artifacts


def expected_tex_hashes() -> dict[str, str]:
    hashes = dict(strict_json(SOURCE / "check.json")["tex_sha256"])
    require(len(hashes) == 119, "Predecessor TeX manifest is not 119 files")
    hashes["cohomology.tex"] = COHOMOLOGY_ARTIFACTS["cohomology.tex"][1]
    return hashes


def load_mkidx():
    return load_module(ROOT / "fga" / "mkidx.py", "tohoku_r51_pinned_mkidx")


def load_mkmap():
    return load_module(ROOT / "fga" / "mkmap.py", "tohoku_r51_pinned_mkmap")


def load_intake():
    return load_module(ROOT / "srcmap" / "intake.py", "tohoku_r51_pinned_intake")


def verify_semantic() -> dict[str, object]:
    require_semantic_frozen()
    require_plain_directory(SEM)
    entries = list(SEM.iterdir())
    require({path.name for path in entries if path.is_file()} == set(EXPECTED_SEM), "sem/r18 file surface drift")
    require(not any(path.is_dir() for path in entries), "Unexpected sem/r18 subdirectory")
    records = []
    for name, expected in sorted(EXPECTED_SEM.items()):
        require_identity(SEM / name, expected)
        records.append(record(SEM / name))
    surface = (len(records), sum(int(item["bytes"]) for item in records), aggregate(records))
    require(surface == EXPECTED_SEM_SURFACE, "sem/r18 complete surface aggregate drift")

    manifest = strict_json(SEM / "manifest.json")
    validation = strict_json(SEM / "validation.json")
    require(manifest.get("schema") == "tohoku-semantic-local-successor-manifest-v18", "sem/r18 manifest schema drift")
    require(manifest.get("errors") == [], "sem/r18 manifest errors")
    require(validation.get("schema") == "tohoku-semantic-local-successor-validation-v18", "sem/r18 validation schema drift")
    require(validation.get("status") == "PASS" and validation.get("errors") == [], "sem/r18 validation not PASS")
    require(validation.get("manifest_sha256") == EXPECTED_SEM["manifest.json"][1], "sem/r18 manifest-validation binding drift")
    file_surface = manifest.get("file_surface", {})
    require(
        (file_surface.get("records"), file_surface.get("bytes"), file_surface.get("aggregate_sha256"))
        == EXPECTED_SEM_PAYLOAD_SURFACE,
        "sem/r18 payload surface drift",
    )
    expected_payload = {
        name: {"name": name, "bytes": expected[0], "sha256": expected[1]}
        for name, expected in EXPECTED_SEM.items()
        if name not in {"manifest.json", "validation.json"}
    }
    actual_payload = {str(item.get("name")): item for item in manifest.get("files", [])}
    require(actual_payload == expected_payload, "sem/r18 manifest file records drift")

    oracle = manifest.get("table_delta_oracle", {})
    changed_tables = oracle.get("changed_tables", {})
    require(
        oracle.get("changed_table_count") == 3
        and set(changed_tables) == {"catalog.csv", "nodes.csv", "occ.csv"}
        and oracle.get("unchanged_table_count") == 12
        and oracle.get("unchanged_inherited_file_count") == 13
        and oracle.get("all_row_counts_invariant") is True
        and oracle.get("all_stable_ids_invariant") is True,
        "sem/r18 exact table-delta oracle drift",
    )
    require(
        validation.get("checks", {}).get("three_changed_tables_match_exact_eighteen_field_oracle") is True
        and validation.get("checks", {}).get("twelve_unaffected_tables_byte_identical") is True
        and validation.get("checks", {}).get("all_counts_invariant") is True,
        "sem/r18 independent validation oracle drift",
    )
    require_identity(
        PROJECT / "sem" / "r17" / "nodes.csv",
        BASE.EXPECTED_SEM["nodes.csv"],
    )
    _, nodes = load_csv(SEM / "nodes.csv")
    _, predecessor_nodes = load_csv(PROJECT / "sem" / "r17" / "nodes.csv")
    require(len(nodes) == 991 and len({row["node_id"] for row in nodes}) == 991, "sem/r18 node ID/count drift")
    require(
        {row["node_id"] for row in nodes} == {row["node_id"] for row in predecessor_nodes},
        "sem/r18 stable node-ID surface drift",
    )
    by_id = {row["node_id"]: row for row in nodes}
    require(
        {row["unit_id"] for row in DECISION_ROWS} <= set(by_id),
        "D1008 semantic units missing",
    )
    manifest_blob = json.dumps(manifest, ensure_ascii=True, sort_keys=True)
    require(
        "v068c3r17" in manifest_blob
        and "v68r39" in manifest_blob
        and READER_ARTIFACTS["build_receipt"][2] in manifest_blob
        and READER_QA_ARTIFACTS["check"][2] in manifest_blob,
        "sem/r18 reader binding drift",
    )
    return {
        "generation": "sem/r18",
        "files": records,
        "file_count": len(records),
        "bytes": sum(int(item["bytes"]) for item in records),
        "aggregate_sha256": aggregate(records),
        "manifest_payload_surface": {
            "file_count": EXPECTED_SEM_PAYLOAD_SURFACE[0],
            "bytes": EXPECTED_SEM_PAYLOAD_SURFACE[1],
            "aggregate_sha256": EXPECTED_SEM_PAYLOAD_SURFACE[2],
        },
        "validation_status": "PASS",
        "stable_node_ids": 991,
        "reader_r17_binding": "EXACT",
        "p214_semantic_replay": "EXACT",
    }


def verify_repairs() -> dict[str, object]:
    repairs = expected_repairs()
    records = []
    for relative, expected in sorted(repairs.items()):
        path = PROJECT / relative
        require_identity(path, expected)
        records.append(record(path, relative))
    for artifact_group in (P214_SOURCE_ARTIFACTS, READER_ARTIFACTS, READER_QA_ARTIFACTS):
        for path, size, sha256 in artifact_group.values():
            require_identity(path, (size, sha256))

    admission = strict_json(P214_SOURCE_ARTIFACTS["admission"][0])
    require(
        admission.get("schema") == "tohoku-p214-stabilizer-source-admission-v1"
        and admission.get("status") == "PASS"
        and admission.get("errors") == []
        and admission.get("source_state") == "admitted_no_overwrite_successor"
        and admission.get("mapping_state") == "UNCHANGED_R50"
        and admission.get("unit_id") == "tohoku:comparison:equivariant-hom-stalk-to-fiber"
        and admission.get("decision_id") == "TOH-SRC-P214-005",
        "p214 source admission drift",
    )
    require(
        admission.get("exact_source_delta", {}).get("diplomatic_french_changes") == 0
        and admission.get("exact_source_delta", {}).get("other_source_changes") == 0
        and admission.get("exact_source_delta", {}).get("predecessor_reconstruction_exact")
        == {"corrected_french": True, "english": True},
        "p214 exact source delta drift",
    )
    decisions_data = P214_SOURCE_ARTIFACTS["decisions"][0].read_bytes()
    require(b"\r" not in decisions_data and decisions_data.endswith(b"\n"), "Noncanonical p214 decision JSONL")
    decisions = [json.loads(line) for line in decisions_data.decode("utf-8").splitlines()]
    decision_ids = [row.get("decision_id") for row in decisions]
    require(
        len(decisions) == 8
        and len(set(decision_ids)) == 8
        and decision_ids[-1] == "TOH-P214-STABILIZER-MATH-001",
        "p214 decision ledger drift",
    )
    source_corrections = (PROJECT / "SOURCE_CORRECTIONS.jsonl").read_bytes()
    require(b"\r" not in source_corrections and source_corrections.endswith(b"\n"), "Noncanonical source-corrections JSONL")
    source_rows = [json.loads(line) for line in source_corrections.decode("utf-8").splitlines()]
    source_ids = [row.get("decision_id") for row in source_rows]
    require(
        len(source_rows) == 378
        and len(set(source_ids)) == 378
        and source_ids.count("TOH-SRC-P214-005") == 1,
        "source-corrections ledger drift",
    )

    build = strict_json(READER_ARTIFACTS["build_receipt"][0])
    require(
        build.get("schema") == "tohoku-v068-staged-successor-build-v1"
        and build.get("revision") == "v068c3r17"
        and build.get("predecessor_revision") == "v068c3r16"
        and build.get("status") == "PASS"
        and build.get("errors") == []
        and build.get("compile_order") == ["fr", "en"]
        and build.get("passes_per_language") == 2
        and build.get("shell") is False,
        "reader r17 build receipt drift",
    )
    require(
        build.get("staged_source_verification")
        == {
            "all_files_locked_against_write_and_delete": True,
            "bytes": 62845,
            "format": "canonical_json_array_utf8_sort_keys_compact over path, bytes, sha256",
            "rows": 543,
            "sha256": "AC993EDB2BB7A9673CD58936A80030818D1D2BB86235F35385CF701E53FB87FB",
            "total_file_bytes": 11854667,
            "verified_from_already_open_handles": True,
        },
        "reader r17 staged-source manifest drift",
    )
    require(
        build.get("revision_surface_contract", {}).get("replaced_staged_paths") == ["en/p214.tex", "fr/p214.tex"]
        and build.get("revision_surface_contract", {}).get("byte_identical_staged_files") == 541
        and build.get("revision_surface_contract", {}).get("other_staged_source_changes") == 0,
        "reader r17 source transition drift",
    )
    for language, artifact, output, name, pages in (
        ("en", "english_build_pdf", "english_output_pdf", "en-p119-221-v068c3r17.pdf", 90),
        ("fr", "french_build_pdf", "french_output_pdf", "fr-p119-221-v068c3r17.pdf", 93),
    ):
        pdf = build.get("pdfs", {}).get(language, {})
        expected = READER_ARTIFACTS[artifact]
        require(
            (pdf.get("name"), pdf.get("bytes"), pdf.get("sha256"), pdf.get("full_readback"))
            == (name, expected[1], expected[2], True)
            and pdf.get("strict_pdf_parse", {}).get("result") == "PASS"
            and pdf.get("strict_pdf_parse", {}).get("pages") == pages
            and pdf.get("strict_pdf_parse", {}).get("encrypted") is False
            and READER_ARTIFACTS[output][1:] == expected[1:],
            f"reader r17 {language} PDF evidence drift",
        )

    qa = strict_json(READER_QA_ARTIFACTS["check"][0])
    require(
        qa.get("schema") == "tohoku-v068-reader-independent-qa-v1"
        and qa.get("qa_revision") == "v68r39"
        and qa.get("reader_revision") == "v068c3r17"
        and qa.get("predecessor_revision") == "v068c3r16"
        and qa.get("stable_id") == "tohoku:reader-qa:v68r39:v068c3r17"
        and qa.get("status") == "PASS"
        and qa.get("errors") == [],
        "reader r39 independent QA drift",
    )
    require(
        qa.get("conclusion")
        == {
            "blockers": [],
            "page_inventory_complete": True,
            "pdf_pair_accepted": True,
            "reader_successor_accepted": True,
            "semantic_replay_claimed": False,
            "source_transition_exact": True,
            "visual_review_accepted": True,
        },
        "reader r39 conclusion drift",
    )
    require(
        qa.get("p214_visual_review", {}).get("status") == "PASS"
        and qa.get("p214_visual_review", {}).get("english", {}).get("correction_pdf_page") == 83
        and qa.get("p214_visual_review", {}).get("french", {}).get("correction_pdf_page") == 86,
        "reader r39 p214 visual audit drift",
    )
    return {
        "files": records,
        "file_count": len(records),
        "bytes": sum(int(item["bytes"]) for item in records),
        "aggregate_sha256": aggregate(records),
        "p214_source_repair": "SEALED_REPLAY_PASS",
        "reader_r17": "PASS",
        "reader_r17_independent_qa": "STRICT_PASS",
    }


def verify_d1008_audit() -> dict[str, object]:
    require_d1008_frozen()
    require_identity(D1008_AUDIT, EXPECTED_D1008_AUDIT)
    audit = strict_json(D1008_AUDIT)
    require(audit.get("schema") == "tohoku-stacks-d1008-audit-v1", "D1008 audit schema drift")
    require(audit.get("status") == "STRICT_PASS" and audit.get("errors") == [], "D1008 audit not STRICT_PASS")
    require(audit.get("formalization_id") == "D1008", "D1008 formalization ID drift")
    audit_blob = json.dumps(audit, ensure_ascii=True, sort_keys=True)
    for token in (
        "tohoku:comparison:equivariant-hom-stalk-to-fiber",
        "tohoku:comparison:equivariant-ext-stalk-to-fiber",
        "cohomology-lemma-equivariant-hom-injective-stalk",
        "cohomology-lemma-equivariant-ext-stalk",
        "D001017",
        "D001018",
        "v068c3r17",
        "v68r39",
        "sem/r18",
    ):
        require(token in audit_blob, f"D1008 audit binding missing: {token}")
    for name, expected in COHOMOLOGY_ARTIFACTS.items():
        require_identity(ROOT / name, expected)
        require(expected[1] in audit_blob, f"D1008 audit artifact binding drift: {name}")
    return {"receipt": record(D1008_AUDIT, "D1008_CHECK.json"), "status": "STRICT_PASS", "errors": []}


def verify_builds() -> dict[str, object]:
    artifacts = expected_artifacts()
    for name, expected in artifacts.items():
        require_identity(ROOT / name, expected)
    r43 = BASE.BASE.BASE.BASE.BASE.BASE.BASE.BASE
    legacy = r43.load_legacy_validator()
    specs = {
        **legacy.BUILD_SPECS,
        "derived": {"pages": 148, "visual": [72, 73, 74, 75, 76, 77]},
        "cohomology": {"pages": 225, "visual": [177, 178, 179, 180]},
        "injectives": {"pages": 40, "visual": [6, 7, 8]},
    }
    aux_lines = {**legacy.EXPECTED_AUX_LINES}
    aux_lines["derived.aux"] = (
        r"\newlabel{lemma-right-satellites-to-right-derived-functors}{{20.4}{72}{Comparison from satellites to right derived functors}{subsection.20.4}{}}",
        r"\newlabel{lemma-right-derived-functor-commutes-filtered-colimits}{{20.6}{74}{Filtered colimits of objects}{subsection.20.6}{}}",
        r"\newlabel{equation-filtered-colimit-right-derived-objects-1}{{20.6.1}{74}{Right derived functors and injective resolutions}{equation.20.6.1}{}}",
        r"\newlabel{equation-filtered-colimit-right-derived-objects-2}{{20.6.2}{74}{Right derived functors and injective resolutions}{equation.20.6.2}{}}",
        r"\newlabel{equation-filtered-colimit-right-derived-objects-3}{{20.6.3}{75}{Right derived functors and injective resolutions}{equation.20.6.3}{}}",
    )
    aux_lines["cohomology.aux"] = (
        r"\newlabel{lemma-crossed-homomorphism-torsor-obstruction}{{4.4}{5}{The torsor obstruction of a crossed homomorphism}{subsection.4.4}{}}",
        r"\newlabel{lemma-pointwise-flasque-envelope-groups}{{12.2}{22}{Pointwise flasque envelope}{subsection.12.2}{}}",
        r"\newlabel{lemma-flasque-group-torsors-trivial}{{12.3}{22}{}{subsection.12.3}{}}",
        r"\newlabel{lemma-pointwise-envelope-crossed-homomorphism}{{12.4}{23}{The crossed quotient of a pointwise envelope}{subsection.12.4}{}}",
        r"\newlabel{lemma-pointwise-envelope-torsor-bijection}{{12.5}{24}{Pointwise envelopes lift torsors uniquely}{subsection.12.5}{}}",
        r"\newlabel{lemma-pointwise-envelope-degree-two-boundary}{{12.8}{26}{The degree-two boundary of a pointwise envelope}{subsection.12.8}{}}",
        r"\newlabel{lemma-holomorphic-logarithmic-derivative-obstruction}{{12.9}{28}{The holomorphic logarithmic-derivative obstruction}{subsection.12.9}{}}",
        r"\newlabel{definition-fine-abelian-sheaf}{{22.6}{55}{Fine abelian sheaves}{subsection.22.6}{}}",
        r"\newlabel{lemma-fine-phi-soft-and-tensor}{{22.7}{55}{}{subsection.22.7}{}}",
        r"\newlabel{lemma-cartan-resolution-fine-torsion-free}{{22.16}{59}{Cartan resolution}{subsection.22.16}{}}",
        r"\newlabel{lemma-equivariant-hom-injective-stalk}{{45.51}{177}{Equivariant Hom and injective stalks}{subsection.45.51}{}}",
        r"\newlabel{lemma-equivariant-ext-stalk}{{45.52}{179}{Equivariant Ext at a stalk}{subsection.45.52}{}}",
    )
    aux_lines["injectives.aux"] = (
        r"\newlabel{lemma-injective-left-module-stalks}{{4.2}{6}{}{subsection.4.2}{}}",
        r"\newlabel{lemma-injective-module-stalks}{{4.3}{8}{}{subsection.4.3}{}}",
        r"\newlabel{theorem-injective-embedding-grothendieck}{{12.7}{23}{}{subsection.12.7}{}}",
        r"\newlabel{lemma-filtered-diagram-injective-resolutions}{{12.8}{24}{Compatible injective resolutions of filtered systems}{subsection.12.8}{}}",
        r"\newlabel{section-K-injective}{{13}{25}{K-injectives in Grothendieck categories}{section.13}{}}",
        r"\newlabel{lemma-surjection-bounded-size}{{13.1}{25}{}{subsection.13.1}{}}",
        r"\newlabel{lemma-characterize-K-injective}{{13.3}{26}{}{subsection.13.3}{}}",
    )
    forbidden = [
        r"(?m)^! (?:LaTeX|Package|Undefined|Emergency|File|Missing|Extra|Use of|Runaway|Paragraph)",
        r"(?m)^LaTeX Warning:", r"(?m)^Package .* Warning:",
        r"undefined references", r"undefined citations",
        r"Rerun to get cross-references right", r"Label\(s\) may have changed",
    ]
    builds: dict[str, object] = {}
    for chapter, spec in specs.items():
        log = (ROOT / f"{chapter}.log").read_text(encoding="utf-8", errors="replace")
        hits = [pattern for pattern in forbidden if re.search(pattern, log)]
        require(not hits, f"{chapter} build diagnostics: {hits}")
        output = re.findall(
            rf"Output written on {re.escape(chapter)}\.pdf \(([0-9]+) pages?, ([0-9]+) bytes\)\.",
            log,
        )
        require(output == [(str(spec["pages"]), str(artifacts[f"{chapter}.pdf"][0]))], f"{chapter} output receipt drift")
        lines = set((ROOT / f"{chapter}.aux").read_text(encoding="utf-8").splitlines())
        require(all(line in lines for line in aux_lines[f"{chapter}.aux"]), f"{chapter} AUX evidence drift")
        if chapter == "cohomology":
            box_ranges = [
                (int(start), int(end or start))
                for start, end in re.findall(r"Overfull \\hbox .*? at lines? ([0-9]+)(?:--([0-9]+))?", log)
            ]
            require(
                not any(start <= 18720 and end >= 18440 for start, end in box_ranges),
                "D1008 source block has an overfull box",
            )
        builds[chapter] = {
            "tex": record(ROOT / f"{chapter}.tex"),
            "aux": record(ROOT / f"{chapter}.aux"),
            "log": record(ROOT / f"{chapter}.log"),
            "pdf": record(ROOT / f"{chapter}.pdf"),
            "pdf_pages": spec["pages"],
            "visual_reviewed_pages": spec["visual"],
            "undefined_references": 0,
            "undefined_citations": 0,
            "rerun_notices": 0,
            "new_block_overfull_boxes": 0,
        }
    tex = (ROOT / "cohomology.tex").read_text(encoding="utf-8")
    for evidence in (
        r"\label{lemma-equivariant-hom-injective-stalk}",
        r"\label{lemma-equivariant-ext-stalk}",
        "rings are not required to be",
        "All modules are unital left modules",
        "but no module structure on this internal Hom is asserted",
        r"\mathop{\rm Hom}\nolimits_{\mathcal U_x}",
        r"\mathop{\rm Ext}\nolimits^n_{\mathcal U_x}",
        "orientation is right multiplication by the chosen generator",
        "The left Baer criterion",
        "underlying abelian sheaf",
    ):
        require(evidence in tex, f"D1008 source proof/nonclaim drift: {evidence}")
    inherited = strict_json(SOURCE / "r50-check.json").get("builds", {}).get("independent_audits", {})
    require(
        set(inherited) == {f"D{number:06d}" for number in range(996, 1017)},
        "r50 independent-audit inheritance drift",
    )
    d1008_receipt = record(D1008_AUDIT, "D1008_CHECK.json")
    builds["independent_audits"] = {
        **inherited,
        "D001017": {
            "status": "STRICT_PASS",
            "receipt": d1008_receipt,
            "scope": [
                "equivariant Hom fixed-point stalk comparison",
                "skew stabilizer ring and injective stalk theorem",
                "left-sided noncommutative orientation and explicit nonclaims",
                "225-page strict parse and pages 177-180 clean",
            ],
        },
        "D001018": {
            "status": "STRICT_PASS",
            "receipt": d1008_receipt,
            "scope": [
                "derived abelian-sheaf equivariant Ext comparison",
                "injective-resolution stalk computation",
                "commutative SheafExt identification",
                "225-page strict parse and pages 177-180 clean",
            ],
        },
    }
    return builds


def verify_scanner_oracle() -> dict[str, object]:
    mkidx = load_mkidx()
    index, errors, warnings, tex_hashes = mkidx.build_index()
    require(errors == [], f"Current bounded scanner errors: {errors}")
    require(tex_hashes == expected_tex_hashes(), "Current 119-file TeX hash oracle drift")
    require({path.name for path in ROOT.glob("*.tex")} == set(tex_hashes), "Live TeX filename surface drift")
    _, topics = load_csv(SOURCE / "topics.csv")
    candidates = mkidx.candidate_rows(index, topics)
    topic_map, map_errors, map_warnings = mkidx.topic_map_rows(index, topics)
    require(map_errors == [], f"Current topic-map errors: {map_errors}")
    warnings = [*warnings, *map_warnings]

    _, old_index = load_csv(SOURCE / "stx.csv")
    fields = list(old_index[0])
    old_by = {row["full_label"]: row for row in old_index}
    new_by = {row["full_label"]: {field: row[field] for field in fields} for row in index}
    require(set(old_by) <= set(new_by), "Scanner removed an existing label")
    require(set(new_by) - set(old_by) == set(NEW_LABEL_ROWS), "D1008 new-label set drift")
    for label, expected_row in NEW_LABEL_ROWS.items():
        require(new_by[label] == expected_row, f"D1008 new-label row drift: {label}")
    changed_labels = []
    for label in old_by:
        if old_by[label] != new_by[label]:
            require(
                all(old_by[label][field] == new_by[label][field] for field in fields if field != "line"),
                f"Existing label substantive metadata drift: {label}",
            )
            require(
                int(new_by[label]["line"]) - int(old_by[label]["line"]) == 271,
                f"Existing label line-shift drift: {label}",
            )
            changed_labels.append(label)
    require(
        Counter(old_by[label]["file"] for label in changed_labels) == Counter({"cohomology.tex": 109}),
        "Existing label line-only oracle drift",
    )

    _, old_candidates = load_csv(SOURCE / "tcand.csv")
    old_c = {(row["topic_id"], row["full_label"]): row for row in old_candidates}
    new_c = {(row["topic_id"], row["full_label"]): row for row in candidates}
    require(set(new_c) == set(old_c), "Candidate-key surface drift")
    changed_candidates = []
    for key in old_c:
        if old_c[key] != new_c[key]:
            require(
                all(old_c[key][field] == new_c[key][field] for field in old_c[key] if field != "line"),
                f"Existing candidate substantive metadata drift: {key}",
            )
            require(
                int(new_c[key]["line"]) - int(old_c[key]["line"]) == 271,
                f"Existing candidate line-shift drift: {key}",
            )
            changed_candidates.append(key)
    require(
        Counter(old_c[key]["file"] for key in changed_candidates) == Counter({"cohomology.tex": 16}),
        "Candidate line-only oracle drift",
    )
    require(len(index) == 22064 and len(candidates) == 1270 and len(topic_map) == 13, "Scanner count oracle drift")
    require(sum(1 for row in index if row["tag"]) == 21437, "Official-tag join count drift")
    require(len(warnings) == 636, "Scanner warning count drift")
    for label in NEW_LABEL_ROWS:
        require(
            f"TeX label has no official tag in this snapshot: {label}" in warnings,
            f"D1008 no-official-tag warning drift: {label}",
        )
    serialized = {
        "stx.csv": index_csv_bytes(index),
        "tcand.csv": candidate_csv_bytes(candidates),
        "tmap.csv": topic_map_csv_bytes(topic_map),
    }
    for name, data in serialized.items():
        require((len(data), digest(data)) == EXPECTED_SCAN_OUTPUTS[name], f"Scanner serialized identity drift: {name}")
    return {
        "index": index,
        "candidates": candidates,
        "topic_map": topic_map,
        "warnings": warnings,
        "tex_hashes": tex_hashes,
        "serialized": serialized,
        "counts": EXPECTED_SCAN_COUNTS,
        "delta": {
            "changed_tex_files": ["cohomology.tex"],
            "new_labels": 2,
            "new_label_values": sorted(NEW_LABEL_ROWS),
            "existing_rows_line_number_only": 109,
            "existing_text_hash_changes": 0,
            "existing_other_metadata_changes": 0,
            "official_tag_changes": 0,
            "candidate_count_delta": 0,
            "candidate_keys_added": 0,
            "candidate_keys_removed": 0,
            "existing_candidate_rows_line_number_only": 16,
            "line_shift": 271,
        },
    }


def verify_external() -> dict[str, object]:
    require_frozen_inputs()
    require_plain_directory(SOURCE)
    entries = list(SOURCE.iterdir())
    require({path.name for path in entries if path.is_file()} == set(EXPECTED_SOURCE), "r50 predecessor surface drift")
    require(not any(path.is_dir() for path in entries), "Unexpected r50 predecessor subdirectory")
    records = []
    for name, expected in sorted(EXPECTED_SOURCE.items()):
        require_identity(SOURCE / name, expected)
        records.append(record(SOURCE / name))
    require(
        (len(records), sum(int(item["bytes"]) for item in records), aggregate(records)) == EXPECTED_SOURCE_SURFACE,
        "r50 predecessor aggregate drift",
    )
    payload_records = [item for item in records if item["name"] != "r50-check.json"]
    require(
        (len(payload_records), sum(int(item["bytes"]) for item in payload_records), aggregate(payload_records))
        == EXPECTED_SOURCE_PAYLOAD_SURFACE,
        "r50 predecessor payload aggregate drift",
    )
    predecessor = strict_json(SOURCE / "r50-check.json")
    require(predecessor.get("schema") == "tohoku-stacks-mapping-successor-r50-v1", "r50 predecessor receipt schema drift")
    require(predecessor.get("status") == "PASS" and predecessor.get("errors") == [], "r50 predecessor receipt not PASS")
    require(predecessor.get("deltas", {}).get("decisions") == 1016, "r50 predecessor decision gate drift")
    require(
        predecessor.get("deltas", {}).get("mapping_counts", {}).get("dispositions", {}).get("new_statement") == 15,
        "r50 D1008 predecessor gap gate drift",
    )
    require(predecessor.get("deltas", {}).get("remaining_gap_class_dispositions") == 49, "r50 predecessor gap-count drift")
    for name, expected in expected_runtime().items():
        require_identity(ROOT / name, expected)
    for name, expected in EXPECTED_AUTHORITY.items():
        require_identity(AUTHORITY / name, expected)
    require(Path(sys.executable).resolve() == EXPECTED_PYTHON.resolve(), "Python executable path drift")
    require_identity(EXPECTED_PYTHON, EXPECTED_PYTHON_IDENTITY)
    require(sys.version_info[:3] == (3, 13, 9) and sys.implementation.cache_tag == "cpython-313", "Python runtime drift")
    semantic = verify_semantic()
    repairs = verify_repairs()
    d1008 = verify_d1008_audit()
    builds = verify_builds()
    scanner = verify_scanner_oracle()
    return {
        "predecessor": {
            "name": "tohoku_r50",
            "files": records,
            "file_count": len(records),
            "bytes": sum(int(item["bytes"]) for item in records),
            "aggregate_sha256": aggregate(records),
            "payload_file_count": len(payload_records),
            "payload_bytes": sum(int(item["bytes"]) for item in payload_records),
            "payload_aggregate_sha256": aggregate(payload_records),
        },
        "semantic": semantic,
        "repairs": repairs,
        "d1008_audit": d1008,
        "builds": builds,
        "scanner": scanner,
    }


def expected_units(cfg: dict) -> list[dict[str, str]]:
    _, nodes = load_csv(SEM / "nodes.csv")
    units = load_intake().tohoku_units(nodes, cfg)
    require(len(units) == 991, "Independent sem/r18 unit projection count drift")
    return units


def expected_map(cfg: dict, units: list[dict[str, str]], scanner: dict[str, object], decisions_path: Path) -> list[dict[str, str]]:
    topic_map = {row["topic_id"]: row for row in scanner["topic_map"]}
    structural = set(cfg.get("structural_types", []))
    embedded = set(cfg.get("embedded_types", []))
    historical = set(cfg.get("historical_types", []))
    mapped: list[dict[str, str]] = []
    for unit in units:
        topic_ids = [value for value in unit["topics"].split(";") if value]
        require(set(topic_ids) <= set(topic_map), f"Unknown topic in independent projection: {unit['id']}")
        labels = sorted({
            label
            for topic in topic_ids
            for label in topic_map[topic]["evidence_labels"].split(";")
            if label
        })
        tags = sorted({
            tag
            for topic in topic_ids
            for tag in topic_map[topic]["evidence_tags"].split(";")
            if tag
        })
        kind = unit["unit_type"]
        if kind in structural:
            disposition, state, rationale = (
                "structural_only",
                "classified",
                "Source structure; no independent Stacks object.",
            )
        elif kind in embedded:
            disposition, state, rationale = (
                "structural_only",
                "inherits_parent",
                "Embedded source component; inherit the parent disposition.",
            )
        elif kind in historical:
            disposition, state, rationale = (
                "historical_reference",
                "needs_link_review",
                "Historical or bibliographic unit requiring source linkage.",
            )
        else:
            disposition, state, rationale = (
                "needs_review",
                "generated_intake",
                "Requires statement-level mathematical comparison.",
            )
        mapped.append({
            "unit_id": unit["id"],
            "item": unit["item"],
            "unit_type": kind,
            "parent_id": unit["parent_id"],
            "source_start": unit["source_start"],
            "source_end": unit["source_end"],
            "source_loc": f"{unit['source_file']}:{unit['source_line']}",
            "authority_sha256": unit["authority_sha256"],
            "source_topics": ";".join(topic_ids),
            "topic_evidence_labels": ";".join(labels),
            "topic_evidence_tags": ";".join(tags),
            "decision_id": "",
            "disposition": disposition,
            "review_state": state,
            "stacks_labels": "",
            "stacks_tags": "",
            "rationale": rationale,
        })
    mkmap = load_mkmap()
    decisions, errors = mkmap.load_decisions(decisions_path, mapped, scanner["index"])
    require(errors == [], f"Independent decision replay errors: {errors}")
    mkmap.apply_decisions(mapped, decisions)
    return mapped


def verify_stage(root: Path, receipt_mode: bool) -> dict[str, object]:
    external = verify_external()
    require_plain_directory(root)
    entries = list(root.iterdir())
    expected_names = PAYLOAD | ({"r51-check.json"} if receipt_mode else set())
    require({path.name for path in entries if path.is_file()} == expected_names, "Stage/target file surface drift")
    require(not any(path.is_dir() for path in entries), "Unexpected stage/target subdirectory")

    cfg = strict_json(root / "cfg.json")
    require(cfg.get("dossier_id") == "tohoku_r51", "r51 cfg dossier ID drift")
    require(cfg.get("expected_units") == 991, "r51 cfg unit count drift")
    require(cfg.get("semantic_successor", {}).get("generation") == "sem/r18", "r51 cfg semantic generation drift")
    require(cfg.get("semantic_successor", {}).get("surface_files") == 18, "r51 cfg semantic file count drift")
    require(cfg.get("semantic_successor", {}).get("surface_bytes") == EXPECTED_SEM_SURFACE[1], "r51 cfg semantic bytes drift")
    require(cfg.get("semantic_successor", {}).get("surface_sha256") == EXPECTED_SEM_SURFACE[2], "r51 cfg semantic aggregate drift")
    primary = cfg.get("inputs", {}).get("primary", {})
    require(primary.get("source_file") == "sem/r18/nodes.csv", "r51 cfg primary source drift")
    require(primary.get("sha256") == EXPECTED_SEM["nodes.csv"][1], "r51 cfg node pin drift")
    require(cfg.get("inputs", {}).get("sem_manifest", {}).get("sha256") == EXPECTED_SEM["manifest.json"][1], "r51 cfg manifest pin drift")
    require(cfg.get("inputs", {}).get("sem_validation", {}).get("sha256") == EXPECTED_SEM["validation.json"][1], "r51 cfg validation pin drift")

    intake = strict_json(root / "intake.json")
    check = strict_json(root / "check.json")
    mcheck = strict_json(root / "mcheck.json")
    for name, value in (("intake", intake), ("scan", check), ("map", mcheck)):
        require(value.get("status") == "PASS" and value.get("errors") == [], f"{name} receipt not PASS")
    require(mcheck.get("outputs_promoted") is True, "Mapping outputs not promoted")
    for name in ("issues.csv", "topics.csv", "tmap.csv", "ucand.csv"):
        require((root / name).read_bytes() == (SOURCE / name).read_bytes(), f"{name} drift")

    scanner = external["scanner"]
    for name in ("stx.csv", "tcand.csv", "tmap.csv"):
        require((root / name).read_bytes() == scanner["serialized"][name], f"{name} does not match exact live oracle")
    require(check.get("counts") == EXPECTED_SCAN_COUNTS, "r51 scan counts drift")
    require(check.get("warnings") == scanner["warnings"], "r51 scan warnings drift")
    require(check.get("tex_sha256") == scanner["tex_hashes"], "r51 scan TeX hashes drift")
    runtime = expected_runtime()
    require(check.get("sha256", {}).get("tags/tags") == runtime["tags/tags"][1], "r51 scan tag hash drift")

    unit_fields, units = load_csv(root / "units.csv")
    projected_units = expected_units(cfg)
    r43 = BASE.BASE.BASE.BASE.BASE.BASE.BASE.BASE
    require(unit_fields == r43.load_intake().FIELDS, "r51 unit schema drift")
    require(units == projected_units, "r51 units differ from exact sem/r18 intake projection")
    require(intake.get("counts", {}).get("units") == 991, "r51 intake unit receipt drift")
    require(all(row["source_file"] == "sem/r18/nodes.csv" for row in units), "r51 unit semantic source path drift")
    _, old_units = load_csv(SOURCE / "units.csv")
    require(
        {row["id"] for row in units} == {row["id"] for row in old_units},
        "r51 stable unit-ID surface drift",
    )

    fields, old_decisions = load_csv(SOURCE / "dec.csv")
    new_fields, decisions = load_csv(root / "dec.csv")
    require(fields == new_fields, "Decision schema drift")
    require([row["decision_id"] for row in decisions] == [f"D{number:06d}" for number in range(1, 1019)], "Decision sequence drift")
    require(decisions[:1016] == old_decisions and decisions[1016:] == DECISION_ROWS, "Decision prefix/appended rows drift")
    require((root / "dec.csv").read_bytes().startswith((SOURCE / "dec.csv").read_bytes()), "Decision byte prefix drift")
    anchors = {
        "D000570": (DECISION_ROWS[0], "new_statement"),
        "D000569": (DECISION_ROWS[1], "new_statement"),
    }
    old_by_id = {row["decision_id"]: row for row in old_decisions}
    for decision_id, (successor, expected_disposition) in anchors.items():
        anchor = old_by_id.get(decision_id, {})
        require(anchor.get("unit_id") == successor["unit_id"], f"{decision_id} supersession unit drift")
        require(anchor.get("disposition") == expected_disposition, f"{decision_id} predecessor disposition drift")

    _, issues = load_csv(root / "issues.csv")
    require(len(issues) == 29 and all(row["status"] == "resolved" for row in issues), "r51 issue ledger drift")
    require(mcheck.get("counts") == EXPECTED_MAPPING_COUNTS, "r51 mapping counts drift")
    require(mcheck.get("warnings") == check.get("warnings"), "Map/scan warning mismatch")
    _, undecided = load_csv(root / "ucand.csv")
    require(undecided == [], "Unexpected undecided candidates")

    map_fields, mapped = load_csv(root / "map.csv")
    expected_fields = [
        "unit_id", "item", "unit_type", "parent_id", "source_start",
        "source_end", "source_loc", "authority_sha256", "source_topics",
        "topic_evidence_labels", "topic_evidence_tags", "decision_id",
        "disposition", "review_state", "stacks_labels", "stacks_tags",
        "rationale",
    ]
    require(map_fields == expected_fields, "r51 map schema drift")
    projected_map = expected_map(cfg, projected_units, scanner, root / "dec.csv")
    require(mapped == projected_map, "r51 map differs from independent sem/r18 + live scanner + ledger replay")
    _, old_map = load_csv(SOURCE / "map.csv")
    old_by = {row["unit_id"]: row for row in old_map}
    new_by = {row["unit_id"]: row for row in mapped}
    target_units = {row["unit_id"] for row in DECISION_ROWS}
    semantic_topic_unit = "tohoku:subitem:3.6.2:b"
    require(set(old_by) == set(new_by) and len(new_by) == 991, "Map stable-unit set drift")
    for unit_id in set(new_by) - target_units:
        changed_fields = {field for field in expected_fields if old_by[unit_id][field] != new_by[unit_id][field]}
        expected_changed_fields = (
            {"source_loc", "source_topics", "topic_evidence_labels", "topic_evidence_tags"}
            if unit_id == semantic_topic_unit
            else {"source_loc"}
        )
        require(changed_fields == expected_changed_fields, f"Unauthorized r51 map mutation: {unit_id}")
        require(
            new_by[unit_id]["source_loc"]
            == old_by[unit_id]["source_loc"].replace("sem/r17/", "sem/r18/"),
            f"Semantic source-location transition drift: {unit_id}",
        )
    require(
        (
            new_by[semantic_topic_unit]["source_topics"],
            new_by[semantic_topic_unit]["topic_evidence_labels"],
            new_by[semantic_topic_unit]["topic_evidence_tags"],
        )
        == (
            "derived-functor;grothendieck-category;injectives",
            "cohomology-section-derived-functors;derived-section-injective-resolutions;"
            "derived-section-right-derived-functor;homology-section-injectives;"
            "injectives-section-grothendieck-categories;injectives-section-grothendieck-conditions",
            "0134;013G;0156;05AB;0716;079A",
        ),
        "p169 semantic topic projection drift",
    )
    authorized_fields_by_decision = {
        "D001017": {"source_loc", "decision_id", "disposition", "review_state", "stacks_labels", "stacks_tags", "rationale"},
        "D001018": {"source_loc", "decision_id", "disposition", "review_state", "stacks_labels", "stacks_tags", "rationale"},
    }
    for decision in DECISION_ROWS:
        unit_id = decision["unit_id"]
        authorized_fields = authorized_fields_by_decision[decision["decision_id"]]
        changed_fields = {field for field in expected_fields if old_by[unit_id][field] != new_by[unit_id][field]}
        require(changed_fields == authorized_fields, f"{decision['decision_id']} map mutation field set drift")
        for field in ("decision_id", "disposition", "review_state", "stacks_labels", "rationale"):
            require(new_by[unit_id][field] == decision[field], f"{decision['decision_id']} mapped {field} drift")
        require(new_by[unit_id]["stacks_tags"] == "", f"{decision['decision_id']} unexpectedly claims an official tag")
        require(
            new_by[unit_id]["source_loc"]
            == old_by[unit_id]["source_loc"].replace("sem/r17/", "sem/r18/"),
            f"{decision['decision_id']} semantic source-location drift",
        )
    for decision_id, unit_id in (
        ("D001015", "tohoku:proposition:3.6.2"),
        ("D001016", "tohoku:proposition:4.1.2"),
    ):
        require(new_by[unit_id]["decision_id"] == decision_id, f"{decision_id} no longer selected")

    gap_count = sum(
        EXPECTED_MAPPING_COUNTS["dispositions"][name]
        for name in ("existing_weaker", "extend_existing", "new_statement", "new_section")
    )
    require(gap_count == 47, "Gap-class arithmetic drift")
    status = (root / "STATUS.md").read_text(encoding="utf-8")
    for token in (
        "sem/r18", "D001017", "D001018", "D000570", "D000569", "47 gap-class",
        "tohoku:comparison:equivariant-hom-stalk-to-fiber",
        "tohoku:comparison:equivariant-ext-stalk-to-fiber",
        "cohomology-lemma-equivariant-hom-injective-stalk",
        "cohomology-lemma-equivariant-ext-stalk",
        "existing_stronger", "skew stabilizer ring", "abelian groups",
    ):
        require(token in status, f"STATUS missing token: {token}")

    result = {
        "status": "PASS",
        "errors": [],
        "stable_units": 991,
        "decisions": 1018,
        "decisions_appended": DECISION_ROWS,
        "active_source_issues": [],
        "mapping_counts": EXPECTED_MAPPING_COUNTS,
        "scan_counts": EXPECTED_SCAN_COUNTS,
        "scanner_delta": scanner["delta"],
        "remaining_gap_class_dispositions": 47,
        "semantic_generation": "sem/r18",
        "authorized_map_mutations": {
            "decision_units": sorted(target_units),
            "semantic_source_location_units": 991,
            "semantic_topic_projection_units": [semantic_topic_unit],
            "fields_by_decision": {
                decision_id: sorted(fields)
                for decision_id, fields in sorted(authorized_fields_by_decision.items())
            },
            "nondecision_units_source_location_only": 988,
        },
        "byte_identical_payloads": ["issues.csv", "tmap.csv", "topics.csv", "ucand.csv"],
        "external_evidence": {
            "predecessor_aggregate_sha256": external["predecessor"]["aggregate_sha256"],
            "semantic_aggregate_sha256": external["semantic"]["aggregate_sha256"],
            "repair_aggregate_sha256": external["repairs"]["aggregate_sha256"],
            "d1008_audit_sha256": external["d1008_audit"]["receipt"]["sha256"],
        },
    }

    if receipt_mode:
        receipt = strict_json(root / "r51-check.json")
        require(receipt.get("schema") == "tohoku-stacks-mapping-successor-r51-v1", "r51 receipt schema drift")
        require(receipt.get("status") == "PASS" and receipt.get("errors") == [], "r51 receipt not PASS")
        require(receipt.get("deltas") == result, "r51 receipt delta replay mismatch")
        require(receipt.get("files") == [record(root / name) for name in sorted(PAYLOAD)], "r51 receipt output records drift")
        require(receipt.get("predecessor_dossier") == external["predecessor"], "r51 receipt predecessor evidence drift")
        require(receipt.get("semantic_source") == external["semantic"], "r51 receipt semantic evidence drift")
        require(receipt.get("source_repairs") == external["repairs"], "r51 receipt repair evidence drift")
        require(receipt.get("decision_audit") == external["d1008_audit"], "r51 receipt D1008 evidence drift")
        require(receipt.get("builds") == external["builds"], "r51 receipt build evidence drift")
        execution = receipt.get("execution", {})
        require(
            execution.get("contract")
            == "one_shot_self_attested_driver_bootstrap_builder_validator; exact_inputs_locked_through_atomic_no_overwrite_promotion_with_rollback",
            "r51 execution contract drift",
        )
        require(execution.get("attestation") == expected_execution_attestation(), "r51 execution attestation replay drift")
    return result


def verify_self_attestation() -> dict[str, object]:
    raw = os.environ.pop("TOHOKU_R51_VALIDATOR_EXPECTED", "")
    actual = identity(Path(__file__))
    if not raw:
        return {"mode": "independent_direct", "path": "srcmap/validate_tohoku_r51.py", "bytes": actual[0], "sha256": actual[1]}
    expected = json.loads(raw)
    require(expected == {"bytes": actual[0], "sha256": actual[1]}, "Validator same-bytes attestation drift")
    return {"mode": "builder_locked_subprocess", "path": "srcmap/validate_tohoku_r51.py", "bytes": actual[0], "sha256": actual[1]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--static", action="store_true")
    parser.add_argument("--stage", type=Path)
    parser.add_argument("--receipt", action="store_true")
    args = parser.parse_args()
    attestation = verify_self_attestation()
    require(args.static != (args.stage is not None), "Choose exactly one of --static or --stage")
    if args.static:
        require(not os.path.lexists(TARGET), f"No-overwrite r51 target already exists: {TARGET}")
        require(not os.path.lexists(STAGE), f"Unresolved r51 transaction exists: {STAGE}")
        external = verify_external()
        result = {
            "schema": "tohoku-r51-static-input-audit-v1",
            "status": "PASS",
            "errors": [],
            "attestation": attestation,
            "target_absent": True,
            "stage_absent": True,
            "predecessor_aggregate_sha256": external["predecessor"]["aggregate_sha256"],
            "predecessor_payload_aggregate_sha256": external["predecessor"]["payload_aggregate_sha256"],
            "semantic_aggregate_sha256": external["semantic"]["aggregate_sha256"],
            "d1008_audit": external["d1008_audit"],
            "scanner_delta": external["scanner"]["delta"],
            "builds": external["builds"],
            "projected_mapping_counts": EXPECTED_MAPPING_COUNTS,
            "launch_authorized": False,
        }
    else:
        result = {
            "schema": "tohoku-r51-stage-validation-v1",
            "attestation": attestation,
            **verify_stage(args.stage.resolve(), args.receipt),
        }
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
