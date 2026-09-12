#!/usr/bin/env python3
"""Package the exact R48 36-chapter build for GitHub; no build or publication.

Only approved PDF bytes and allowlisted human metadata enter the ZIP. Raw build,
environment, and process receipts remain outside the assets. The existing direct
release validator still governs A/B, visual QA, CI, and anonymous publication.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import sys
import zipfile

from pypdf import PdfReader

from validate_direct_successor_release import (
    AUTHORITY, AUTHORITY_TREE, Objects, REPOSITORY, SCHEMA as DIRECT_SCHEMA,
    check_build_shape, check_zip_pdfs, identity, parse_json, require, safe_path,
)
from validate_unified_repository import validate_machine_wide_tex_mutex


PACKAGE_SCHEMA = "unofficial-stacks-project-ai-drafts-r48-pdf-package/v1"
INVENTORY_SCHEMA = "unofficial-stacks-project-ai-drafts-r48-pdf-package-inventory/v1"
R48 = "stacks-errata-a04446e-r48"
R48_STEMS = (
    "sets", "categories", "topology", "sheaves", "sites", "algebra", "fields",
    "artin", "brauer", "derived", "simplicial", "homology", "more-algebra",
    "smoothing", "modules", "sites-modules", "schemes", "properties", "morphisms",
    "more-morphisms", "spaces-morphisms", "crystalline", "spaces-cohomology",
    "spaces-duality", "stacks-limits", "injectives", "cohomology", "sites-cohomology",
    "gaga", "moduli", "descent", "perfect", "topologies", "groupoids",
    "more-groupoids", "spaces-perfect",
)
DIRECT_PDFS = ("groupoids", "spaces-perfect")
ZIP_NAME = "stacks-ai-drafts-r48-pdfs.zip"
MANIFEST_NAME = "source-build-manifest.json"
INVENTORY_NAME = "package-inventory.json"
ZIP_TIME = (1980, 1, 1, 0, 0, 0)
ZIP_MODE = 0o100644 << 16


def canonical_json(document):
    return (json.dumps(document, sort_keys=True, indent=2, ensure_ascii=True,
                       allow_nan=False) + "\n").encode("utf-8")


def check_pdf(raw, expected, label):
    require(len(raw) == expected["bytes"], "PDF byte count mismatch: " + label)
    require(hashlib.sha256(raw).hexdigest().upper() == expected["sha256"],
            "PDF SHA-256 mismatch: " + label)
    require(raw.startswith(b"%PDF-") and raw.rstrip().endswith(b"%%EOF"),
            "invalid PDF header/trailer: " + label)
    reader = PdfReader(io.BytesIO(raw), strict=True)
    require(not reader.is_encrypted, "encrypted PDF is not a directly readable asset: " + label)
    require(len(reader.pages) == expected["pages"], "PDF page count mismatch: " + label)
    return raw


def build_inputs(receipt_raw, public_receipt_path):
    receipt = parse_json(receipt_raw)
    safe_path(public_receipt_path)
    require(re.fullmatch(r"validation/direct-successor-[A-Za-z0-9._-]+\.json", public_receipt_path)
            and public_receipt_path != "validation/direct-successor-current.json",
            "build receipt must have an explicit public validation path")
    binding = receipt.get("composition")
    require(isinstance(binding, dict) and binding.get("schema") == DIRECT_SCHEMA,
            "R48 package requires the direct successor composition")
    require(binding.get("authority_commit") == AUTHORITY
            and binding.get("authority_tree") == AUTHORITY_TREE, "wrong pinned authority")
    require(binding.get("new_overlay_ids") == [R48]
            and binding.get("last_admitted_overlay") == R48,
            "package scope must be exactly the R48 incremental successor")
    require(binding.get("required_build_stems") == list(R48_STEMS)
            and binding.get("affected_source_stems") == sorted(DIRECT_PDFS),
            "wrong R48 chapter profile")
    artifacts = check_build_shape(receipt, binding, R48_STEMS, validate_machine_wide_tex_mutex)
    source = receipt.get("source")
    require(isinstance(source, dict) and set(source) == {"commit", "tree"}
            and all(isinstance(value, str) and re.fullmatch(r"[0-9a-f]{40}", value)
                    for value in source.values()), "invalid build source identity")
    for key in ("composition_source_commit", "registry_cutoff_commit"):
        require(isinstance(binding.get(key), str) and re.fullmatch(r"[0-9a-f]{40}", binding[key]),
                "invalid direct composition commit: " + key)
    return receipt, binding, artifacts


def public_manifest(receipt_raw, receipt, binding, artifacts, public_receipt_path, content_commit):
    source = dict(receipt["source"])
    source["url"] = f"https://github.com/{REPOSITORY}/tree/{source['commit']}"
    receipt_identity = {"path": public_receipt_path, **identity(receipt_raw),
                        "commit": content_commit,
                        "url": f"https://github.com/{REPOSITORY}/blob/{content_commit}/{public_receipt_path}"}
    return {
        "schema": PACKAGE_SCHEMA,
        "status": "VERIFIED_PACKAGE_INPUTS",
        "title": "Unofficial Stacks Project AI Drafts - R48 chapter PDFs",
        "repository": REPOSITORY,
        "source": source,
        "build_receipt": receipt_identity,
        "composition": {"schema": DIRECT_SCHEMA, "new_overlay_ids": [R48],
                        "composition_source_commit": binding["composition_source_commit"],
                        "registry_cutoff_commit": binding["registry_cutoff_commit"]},
        "scope": {"chapter_count": 36, "affected_chapters": list(DIRECT_PDFS),
                  "total_pages": sum(row["pages"] for row in artifacts),
                  "total_pdf_bytes": sum(row["bytes"] for row in artifacts),
                  "artifact_tuple_set_sha256": receipt["build"]["artifact_tuple_set_sha256"]},
        "pdfs": [{"stem": row["stem"], "member": f"pdf/{row['stem']}.pdf",
                  **{key: row[key] for key in ("pages", "bytes", "sha256")}}
                 for row in sorted(artifacts, key=lambda item: item["stem"])],
        "packaging": {"zip_compression": "stored", "zip_timestamp": "1980-01-01T00:00:00",
                      "member_order": "ASCII lexicographic", "regular_file_mode": "0644",
                      "raw_logs_or_environment_included": False},
        "limitations": ["Unofficial AI draft; not an official Stacks Project release or endorsement.",
                        "Package integrity does not establish mathematical correctness or proof-assistant verification.",
                        "Cross-chapter links may require other PDFs in this collection.",
                        "A/B build, visual QA, CI, and public readback are validated separately before release."]}


def readme(manifest):
    rows = ["# Unofficial Stacks Project AI Drafts - R48\n",
            "This collection makes the current draft chapters easy to read and compare with their source. "
            "It is an unofficial AI draft, not an official Stacks Project release or endorsement.\n",
            "R48 carries corrections in **Groupoid Schemes** and **Derived Categories of Spaces**. "
            "The complete 36-chapter build is included so that this increment can be read together "
            "with the previously integrated material. It is not a PDF of the entire Stacks Project.\n",
            "## Start reading\n",
            "For immediate reading, `groupoids.pdf` (Groupoid Schemes) and `spaces-perfect.pdf` "
            "(Derived Categories of Spaces) are supplied as individual release downloads.\n",
            f"Download `{ZIP_NAME}` for all 36 PDFs. After extraction, start with "
            "[Groupoid Schemes](pdf/groupoids.pdf) or [Derived Categories of Spaces](pdf/spaces-perfect.pdf). "
            "The chapter links below refer to the extracted archive. No PDF bytes were changed during packaging.\n",
            "## Source and validation\n",
            f"- [Exact source used for this build]({manifest['source']['url']})\n"
            f"- [Matching build receipt]({manifest['build_receipt']['url']})\n"
            f"- [Per-PDF sizes, page counts and SHA-256 hashes]({MANIFEST_NAME})\n",
            "The matching build receipt is linked at the later commit that actually contains it; "
            "the source link identifies the earlier build input. The package check verifies byte "
            "identity and PDF page counts. Independent build comparison, visual QA and public "
            "release verification remain separate checks. Mechanical validation is not a claim "
            "that every mathematical statement has been independently verified.\n",
            "## Included chapters\n",
            "| PDF | Pages |\n| --- | ---: |"]
    rows.extend(f"| [{row['stem']}]({row['member']}) | {row['pages']} |" for row in manifest["pdfs"])
    rows.extend(["", "The source repository retains the upstream provenance and applicable licensing information. "
                 "This package does not relicense the underlying work.", ""])
    return ("\n".join(rows)).encode("utf-8")


def write_zip(path, members):
    with zipfile.ZipFile(path, mode="x", compression=zipfile.ZIP_STORED, allowZip64=True) as archive:
        archive.comment = b""
        for name in sorted(members):
            safe_path(name)
            info = zipfile.ZipInfo(name, date_time=ZIP_TIME)
            info.create_system, info.external_attr = 3, ZIP_MODE
            info.create_version, info.extract_version, info.internal_attr = 20, 20, 0
            info.compress_type, info.extra, info.comment = zipfile.ZIP_STORED, b"", b""
            archive.writestr(info, members[name])


def verify_zip(path, members, pdf_members, by_stem):
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        require([info.filename for info in infos] == sorted(members),
                "ZIP has missing, duplicate, unsorted or unexpected members")
        require(not archive.comment, "unexpected ZIP archive comment")
        for info in infos:
            require(info.date_time == ZIP_TIME and info.create_system == 3
                    and info.external_attr == ZIP_MODE and info.compress_type == zipfile.ZIP_STORED
                    and info.create_version == 20 and info.extract_version == 20
                    and info.internal_attr == 0 and not info.extra and not info.comment
                    and info.flag_bits == 0,
                    "ZIP metadata is not deterministic")
            actual = archive.read(info)
            require(identity(actual) == identity(members[info.filename]),
                    "reopened ZIP member identity mismatch: " + info.filename)
            if info.filename in pdf_members:
                check_pdf(actual, by_stem[pdf_members[info.filename]], info.filename)
    # Reuse the publication validator's exact PDF-member contract as well.
    check_zip_pdfs(path, pdf_members, by_stem)


def package(repository_root, build_root, build_receipt, output_dir, content_commit, public_receipt_path):
    output = Path(output_dir).resolve()
    require(not output.exists(), "output directory already exists; no package was overwritten")
    root = Path(build_root).resolve(strict=True)
    require(root.is_dir(), "build root is not a directory")
    raw = Path(build_receipt).read_bytes()
    receipt, binding, artifacts = build_inputs(raw, public_receipt_path)
    objects = Objects(repository_root)
    content_commit = objects.commit(content_commit)
    source_commit = objects.commit(receipt["source"]["commit"])
    objects.tree(source_commit, receipt["source"]["tree"])
    objects.raw("merge-base", "--is-ancestor", source_commit, content_commit)
    require(objects.blob(content_commit, public_receipt_path) == raw,
            "selected build receipt differs from its exact public-content Git blob")
    by_stem = {row["stem"]: row for row in artifacts}
    pdfs = {}
    for stem in R48_STEMS:
        path = root / f"{stem}.pdf"
        require(path.is_file() and not path.is_symlink()
                and path.resolve(strict=True).is_relative_to(root), "PDF path is missing or escapes build root")
        require(path.stat().st_size == by_stem[stem]["bytes"], "PDF file size mismatch: " + stem)
        pdfs[stem] = check_pdf(path.read_bytes(), by_stem[stem], stem)
    manifest = public_manifest(raw, receipt, binding, artifacts, public_receipt_path, content_commit)
    public_metadata = {MANIFEST_NAME: canonical_json(manifest), "README.md": readme(manifest)}
    members = {f"pdf/{stem}.pdf": data for stem, data in pdfs.items()}
    members.update(public_metadata)
    pdf_members = {f"pdf/{stem}.pdf": stem for stem in sorted(pdfs)}
    # All inputs are validated before claiming the exclusively new output path.
    output.mkdir(parents=False, exist_ok=False)
    zip_path = output / ZIP_NAME
    write_zip(zip_path, members)
    verify_zip(zip_path, members, pdf_members, by_stem)
    for stem in DIRECT_PDFS:
        with (output / f"{stem}.pdf").open("xb") as stream:
            stream.write(pdfs[stem])
        check_pdf((output / f"{stem}.pdf").read_bytes(), by_stem[stem], stem)
    for name, data in public_metadata.items():
        with (output / name).open("xb") as stream:
            stream.write(data)
        require((output / name).read_bytes() == data, "metadata readback mismatch")
    assets = []
    for name in sorted([ZIP_NAME, "groupoids.pdf", "spaces-perfect.pdf", *public_metadata]):
        data = (output / name).read_bytes()
        asset = {"name": name, "bytes": len(data),
                 "sha256": hashlib.sha256(data).hexdigest().upper()}
        if name == ZIP_NAME:
            asset["pdf_members"] = pdf_members
        elif name.endswith(".pdf"):
            asset["pdf_stem"] = name[:-4]
        assets.append(asset)
    inventory = {"schema": INVENTORY_SCHEMA, "status": "PASS_PACKAGE_BYTES",
                 "publication_completed": False, "repository": REPOSITORY,
                 "content_commit": content_commit, "build_source_commit": source_commit,
                 "build_receipt": {"path": public_receipt_path, **identity(raw)},
                 "upload_assets": assets, "upload_asset_count": len(assets),
                 "upload_total_bytes": sum(row["bytes"] for row in assets),
                 "zip_members_checked": len(members), "pdfs_checked": len(pdfs),
                 "note": "This inventory is a local transfer control file, not an upload asset. "
                         "Publish only upload_assets after the separate release gates pass."}
    with (output / INVENTORY_NAME).open("xb") as stream:
        stream.write(canonical_json(inventory))
    require(parse_json((output / INVENTORY_NAME).read_bytes()) == inventory,
            "final package inventory readback mismatch")
    return inventory


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--build-root", required=True, type=Path)
    parser.add_argument("--build-receipt", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--content-commit", required=True)
    parser.add_argument("--public-build-receipt-path", required=True)
    args = parser.parse_args(argv)
    result = package(args.repository_root, args.build_root, args.build_receipt,
                     args.output_dir, args.content_commit, args.public_build_receipt_path)
    print(json.dumps({"status": result["status"], "assets": result["upload_asset_count"],
                      "pdfs": result["pdfs_checked"], "bytes": result["upload_total_bytes"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
