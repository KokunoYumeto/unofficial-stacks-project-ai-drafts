"""Check this module's source and optional frozen inputs/build, without compiling."""
import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent


def sha(data):
    return hashlib.sha256(data).hexdigest().upper()


def identity(path, entry):
    data = path.read_bytes()
    if "bytes" in entry:
        assert len(data) == entry["bytes"], f"Size mismatch: {path.name}"
    assert sha(data) == entry["sha256"], f"Hash mismatch: {path.name}"
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", default="integration.json",
                        choices=("integration.json", "intervals-integration.json"))
    parser.add_argument("--authority", type=Path, help="Directory containing ps2.tex and LICENSE")
    parser.add_argument("--received", type=Path, help="Frozen received draft root")
    parser.add_argument("--build", type=Path, help="Completed build output directory")
    args = parser.parse_args()
    record = json.loads((ROOT / args.record).read_text(encoding="utf-8"))
    source = identity(ROOT / record["source"]["path"], record["source"]).decode("utf-8")
    mapping_raw = (ROOT / record.get("source_map_path", "source-map.json")).read_bytes()
    assert sha(mapping_raw) == record["source_map_sha256"]
    mapping = json.loads(mapping_raw)
    labels = re.findall(r"\\label\{([^}]+)\}", source)
    refs = re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", source)
    assert len(labels) == len(set(labels)) and labels == record["labels"]
    assert set(refs) <= set(labels) and len(refs) == record["internal_references"]
    units = sorted(set(re.findall(r"PSM-(?:DEF|LEM|PROP)-\d{4}", source)))
    assert units == record["mapped_source_ids"] == sorted(x["id"] for x in mapping["source_units"])
    statements = len(re.findall(r"\\begin\{(?:proposition|lemma)\}", source))
    assert statements == source.count(r"\begin{proof}") == record["proof_bearing_statements"]
    assert source.count(r"\begin{document}") == source.count(r"\end{document}") == 1
    assert not re.search(r"\\(?:input|include|includegraphics|bibliography)\b", source)
    assert record["whole_handoff_integrated"] is False
    assert record["new_official_stacks_tags"] == 0
    checks = ["source identity", "reference closure", f"{statements} statements and proofs", "source map", "standalone source"]
    if args.authority:
        for row in mapping["source_units"]:
            raw = (args.authority / row["source_file"]).read_bytes()
            assert sha(raw) == row["whole_file_sha256"]
            assert sha(raw[row["start_byte"]:row["end_byte_exclusive"]]) == row["span_sha256"]
        assert sha((args.authority / "LICENSE").read_bytes()) == mapping["authority_license_file_sha256"]
        checks.append(f"{len(units)} exact historical source spans and license identity")
    if args.received:
        inventory = json.loads((ROOT / "received-inventory.json").read_text(encoding="utf-8"))
        for row in inventory["files"]:
            identity(args.received / row["path"], row)
        assert len(inventory["local_result_ids"]) == 151
        assert len(set(inventory["local_result_ids"])) == 151
        checks.append("fourteen frozen received files and 151 unique local IDs")
    if args.build:
        receipt = json.loads((args.build / "BUILD_RECEIPT.json").read_text(encoding="utf-8"))
        assert receipt["status"] == "PASS_BUILD_VISUAL_PENDING"
        assert receipt["source"]["sha256"] == record["source"]["sha256"]
        assert receipt["fresh_builds"][0]["identities"] == receipt["fresh_builds"][1]["identities"]
        pdf_name = Path(record["source"]["path"]).with_suffix(".pdf").name
        identity(args.build / "a" / pdf_name, receipt["pdf"])
        identity(args.build / "b" / pdf_name, receipt["pdf"])
        if receipt["mutex"]["platform"] == "win32":
            assert "released_utc" in receipt["mutex"]
            for row in receipt["captures"]:
                identity(args.build / row["file"], row)
                capture = json.loads((args.build / row["file"]).read_text(encoding="utf-8"))
                assert capture["status"] == "PASS" and capture["observed_empty_tree"] is True
                assert capture["assigned_before_resume"] is True
        checks.append("two byte-identical fresh builds and process-tree closure")
    print(json.dumps({"status": "PASS", "checks": checks, "mathematical_certification": False}))


if __name__ == "__main__":
    main()
