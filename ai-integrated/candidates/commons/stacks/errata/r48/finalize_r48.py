"""Future R48 dynamic mechanical, snapshot, and sealing stages.

Run only after the root writer installs this file inside its issued candidate.
This script never supplies independent or visual verdicts, allocates IDs,
changes a registry, launches TeX, or publishes.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
AI = ROOT.parents[4]

def require(ok, reason):
    if not ok:
        raise ValueError(reason)

def load(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()

def ev(path):
    return dict(path=path.relative_to(ROOT).as_posix(), bytes=path.stat().st_size, sha256=digest(path))

def bound(row):
    path = (ROOT / row["path"]).resolve()
    require(path.is_relative_to(ROOT) and path.is_file(), "Evidence escapes candidate")
    require(digest(path) == row["sha256"] and ("bytes" not in row or path.stat().st_size == row["bytes"]), "Evidence changed: " + row["path"])
    return path

def dump(path, value):
    require(path.resolve().is_relative_to(ROOT), "Write escapes candidate")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="") as stream:
        stream.write(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n")

def build_coverage_limits(config):
    path = ROOT / "replay/BUILD_EVIDENCE_LIMITATIONS.json"
    report = load(path)
    require(report["schema"] == "stacks-r48-imported-build-evidence-limitations/v1" and report["candidate_id"] == config["candidate_id"], "Build coverage adapter mismatch")
    audit = load(bound(report["original_build_review"]))
    require(audit["passed"] is True and audit["candidate_id"] == config["candidate_id"] and audit["failures"] == [], "Actual independent build review missing or adverse")
    require(report["coverage"] == audit["coverage"] and len(report["coverage"]) == 5, "Actual build coverage limits changed or omitted")
    require(all(row["area"] and row["verified"] and row["limit"] for row in report["coverage"]), "Empty build coverage disclosure")
    limitations = [row["area"] + ": " + row["limit"] for row in report["coverage"]]
    require(report["limitations_for_manifest"] == limitations, "Manifest limitations do not preserve actual review")
    require(report["candidate_build_bindings"], "Actual build artifact bindings missing")
    for row in report["candidate_build_bindings"]:
        bound(row)
    return ev(path), limitations

def mechanical(config):
    from pypdf import PdfReader
    review_path = ROOT / "replay/SOURCE_INDEPENDENT_VALIDATION.json"
    review = load(review_path)
    require(review["passed"] is True and review["candidate_id"] == config["candidate_id"], "Independent source review absent")
    require(review["semantic_units"] == config["accepted"] and review["operations"] == config["operation_count"], "Independent source review scope mismatch")
    for row in review["bound_evidence"]:
        bound(row)
    required_source = {"operation-spec.json", "stable-units.json", "source-map.jsonl", "decisions.jsonl", "formula-diagram-inventory.json"}
    required_source |= {f"{role}/{stem}.tex" for stem in config["stems"] for role in ("authority/source", "payload")}
    require(required_source.issubset({row["path"] for row in review["bound_evidence"]}), "Independent source evidence incomplete")
    spec = importlib.util.spec_from_file_location("r48_bound_build_checks", ROOT / "build-receipt.py")
    build_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(build_module)
    build = build_module.validate()
    mutex = build_module.validate_mutex()
    require(build["passed"] is True and {row["stem"] for row in build["chapters"]} == set(config["stems"]), "Incomplete chapter build gates")
    det = load(ROOT / "builds/deterministic-replay.json")
    require(det["passed"] is True and det["fresh_builds_compared"] == 2 and det["recorder_fls_closures_compared"] == 2 * len(config["stems"]), "Two full build comparisons missing")
    coverage_evidence, _ = build_coverage_limits(config)
    chapter_results = []
    for stem in config["stems"]:
        pdf = ROOT / f"builds/{stem}.pdf"
        reader = PdfReader(pdf)
        pages = len(reader.pages)
        visual_path = ROOT / f"replay/PAGE_COMPLETE_VISUAL_ADJUDICATION-{stem}.json"
        visual = load(visual_path)
        require(visual["passed"] is True and visual["candidate_id"] == config["candidate_id"] and visual["blocking_findings"] == [], "Actual visual PASS missing")
        require(visual["scope"]["covered_pages"] == list(range(1, pages + 1)) and visual["scope"]["unreviewed_pages"] == [], "Incomplete visual review")
        render = load(bound(visual["render_manifest"]))
        require(render["pdf"]["sha256"] == digest(pdf), "Visual PDF binding mismatch")
        require([row["page"] for row in render["pages"]] == list(range(1, pages + 1)), "Render pages incomplete")
        for image_row in render["pages"] + render["high_resolution_pages"] + render["contact_sheets"]:
            bound(image_row)
        require([row["page"] for row in visual["page_decisions"]] == list(range(1, pages + 1)), "Visual per-page decisions incomplete")
        for inspected, image in zip(visual["page_decisions"], render["pages"]):
            require(inspected["disposition"] == "PASS" and inspected["png_sha256"] == image["sha256"] and inspected["notes"], "Actual page decision/image binding missing")
        page_map_path = ROOT / f"builds/source-page-map-{stem}.json"
        page_map = load(page_map_path)
        require(page_map["stem"] == stem and page_map["candidate_id"] == config["candidate_id"], "Source page map stem mismatch")
        require(set(page_map["unique_pages"]).issubset(visual["scope"]["high_resolution_pages"]), "Sensitive pages not inspected at high resolution")
        require(page_map["auxiliary_build"]["candidate_pdf_sha256"] == digest(pdf), "SyncTeX bound to wrong PDF")
        bad_links = []
        for number, page in enumerate(reader.pages, 1):
            box = list(map(float, page.mediabox))
            for ref in page.get("/Annots", []):
                annotation = ref.get_object()
                if annotation.get("/Subtype") != "/Link":
                    continue
                rect = annotation.get("/Rect")
                if rect is None or len(rect) != 4:
                    bad_links.append(number)
                    continue
                x0, y0, x1, y1 = map(float, rect)
                if x0 > x1 or y0 > y1 or x0 < box[0] - .01 or y0 < box[1] - .01 or x1 > box[2] + .01 or y1 > box[3] + .01:
                    bad_links.append(number)
        require(not bad_links, "Invalid/out-of-page PDF links")
        chapter_results.append(dict(stem=stem, pdf=ev(pdf), pages=pages, page_map=ev(page_map_path), render_manifest=visual["render_manifest"], visual=ev(visual_path), tagged_pdf="/StructTreeRoot" in reader.trailer["/Root"], bad_link_rectangles=[]))
    result = dict(schema="stacks-r48-final-mechanical-validation/v1", candidate_id=config["candidate_id"], passed=True, independent_source_review=ev(review_path), build_receipt=ev(ROOT / "builds/build-receipt.json"), build_evidence_limits=coverage_evidence, deterministic_replay=ev(ROOT / "builds/deterministic-replay.json"), tex_mutex=mutex, chapters=chapter_results, visual_conclusions_created=False, independent_final_replay="not_performed", registry_admission="not_performed")
    dump(ROOT / "builds/FINAL_MECHANICAL_VALIDATION.json", result)
    return result

def prepare(config):
    require(load(ROOT / "builds/FINAL_MECHANICAL_VALIDATION.json")["passed"] is True, "Mechanical gate missing")
    excluded = {"candidate.manifest.json", "replay/FINAL_STAGE.json", "replay/FINAL_INDEPENDENT_REVIEW.json"}
    inventory = [ev(p) for p in sorted(ROOT.rglob("*")) if p.is_file() and p.relative_to(ROOT).as_posix() not in excluded and p.suffix != ".pyc" and "__pycache__" not in p.parts]
    result = dict(schema="stacks-r48-final-stage-snapshot/v1", candidate_id=config["candidate_id"], status="READY_FOR_FULL_INDEPENDENT_REVIEW_NOT_ADMITTED", snapshot_inventory=inventory, independent_final_replay="NOT_PERFORMED", registry_admission="NOT_PERFORMED")
    dump(ROOT / "replay/FINAL_STAGE.json", result)
    return result

def seal(config):
    from jsonschema import Draft202012Validator
    stage_path = ROOT / "replay/FINAL_STAGE.json"
    frozen_inventory = load(stage_path)["snapshot_inventory"]
    excluded = {"candidate.manifest.json", "replay/FINAL_STAGE.json", "replay/FINAL_INDEPENDENT_REVIEW.json"}
    current_files = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*") if p.is_file() and p.relative_to(ROOT).as_posix() not in excluded and p.suffix != ".pyc" and "__pycache__" not in p.parts}
    frozen_files = {row["path"] for row in frozen_inventory}
    require(len(frozen_files) == len(frozen_inventory) and current_files == frozen_files, "Candidate file set changed after frozen-stage review")
    for row in frozen_inventory:
        bound(row)
    review = load(ROOT / "replay/FINAL_INDEPENDENT_REVIEW.json")
    require(review["passed"] is True and review["candidate_id"] == config["candidate_id"] and review["final_stage_sha256"] == digest(stage_path), "Independent final replay not bound to frozen stage")
    limitations = list(config.get("documented_nonblocking_limitations", []))
    mechanical_report = load(ROOT / "builds/FINAL_MECHANICAL_VALIDATION.json")
    bound(mechanical_report["build_evidence_limits"])
    coverage_evidence, coverage_limits = build_coverage_limits(config)
    require(coverage_evidence == mechanical_report["build_evidence_limits"], "Build coverage changed after mechanical validation")
    limitations.extend(coverage_limits)
    build_report = load(ROOT / "builds/build-receipt.json")
    for chapter in mechanical_report["chapters"]:
        if not chapter["tagged_pdf"]:
            limitations.append(chapter["stem"] + ": the standalone validation PDF is untagged.")
    for chapter in build_report["chapters"]:
        summary = chapter["candidate_log_summary"]
        if summary["undefined_reference_targets"]:
            limitations.append(chapter["stem"] + ": isolated cross-chapter reference warnings remain; exact targets and configured deltas are preserved in the passing build receipt.")
        warnings = {key: summary[key] for key in ("overfull_hboxes", "underfull_hboxes", "overfull_vboxes", "underfull_vboxes") if summary[key]}
        if warnings:
            limitations.append(chapter["stem"] + ": nonblocking layout warnings retained after actual visual review: " + json.dumps(warnings, sort_keys=True))
    primary = dict(stable_unit_manifest="stable-units.json", source_map="source-map.jsonl", decision_ledger="decisions.jsonl", rejection_ledger="rejections.jsonl", formula_diagram_inventory="formula-diagram-inventory.json")
    authorities = sorted(p for p in (ROOT / "authority").rglob("*") if p.is_file())
    exclude = set(authorities) | {ROOT / p for p in primary.values()} | {ROOT / "candidate.manifest.json"}
    other = [p for p in sorted(ROOT.rglob("*")) if p.is_file() and p not in exclude and p.suffix != ".pyc" and "__pycache__" not in p.parts]
    result = dict(schema="mathematics-commons-stacks-candidate-manifest/v1", candidate_id=config["candidate_id"], lease_id=config["lease_id"], namespace=config["namespace"], writer_task=config["writer_task"], upstream=dict(lock="upstream/stacks.lock.json", commit=config["authority_commit"], tree=config["authority_tree"]), source_authorities=[ev(p) for p in authorities], source_closure=dict(enumerated=True, expected_units=config["accepted"], manifested_units=config["accepted"], complete=True), **{k: ev(ROOT / p) for k, p in primary.items()}, builds=[ev(p) for p in other], rights_state="Modified and upstream payload retain GNU FDL 1.2. This independent AI-produced correction overlay has no official Stacks Project endorsement.", review_state="performed", independent_replay="passed", unresolved_defects=limitations, stop_conditions=["Changed referenced bytes invalidate this manifest. Admission and cumulative composition remain separate transitions."], generated_at_utc=datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"))
    Draft202012Validator(load(AI / "schemas/candidate-manifest.schema.json")).validate(result)
    dump(ROOT / "candidate.manifest.json", result)
    return dict(manifest=ev(ROOT / "candidate.manifest.json"))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("stage", choices=("mechanical", "prepare", "seal"))
    args = parser.parse_args()
    require(ROOT.as_posix().endswith("/ai-integrated/candidates/commons/stacks/errata/r48"), "Run only from the actual issued candidate, never the proposal directory")
    config = load(ROOT / "candidate.config.json")
    result = dict(mechanical=mechanical, prepare=prepare, seal=seal)[args.stage](config)
    print(json.dumps(dict(stage=args.stage, passed=True, result=result.get("status", result.get("manifest", result.get("candidate_id"))))))

if __name__ == "__main__":
    main()
