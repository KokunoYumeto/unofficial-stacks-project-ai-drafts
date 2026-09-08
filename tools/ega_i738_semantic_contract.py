"""Exact EGA I7.3.8 evidence contracts, not a formal proof checker.

The immutable receipt seal protects reviewed metadata against self-rehashing.
Actual source/target/ledger objects are checked separately: a receipt copy is
not evidence that those bytes exist. Live source retrieval remains the bounded
raw-source replay tool's job; this offline checker does not claim to fetch it.
"""
import csv
import hashlib
import io
import json

RECEIPT_PATH = 'validation/ega-i-7.3.8-semantic-checkpoint-2026-09-08.json'
RECEIPT_BYTES = 161175
RECEIPT_SHA256 = 'A1CC828A3AA87E704EFE8D73CFB92972BAF859F98EDD6D68593FE922BF7593E6'
CONTRACT_SHA256 = '94A675C1C42FD94E176706AA2B0AE0899D4251A9CA05943C3A91A4FAA6C3DD25'
SEMANTICS = {'source_versions': ['old_fr', 'corrected_fr', 'en'], 'old_assertion': 'superseded false global isomorphism for finite-component generic-point surjection', 'replacement': 'integral schemes and dominant morphism; canonical map and generic-stalk isomorphism', 'english_role': 'follows authoritative replacement; not mistranslation of obsolete French', 'printed_authority': 'separate new direct binding; original visual reading attributed to root', 'historical_F37ZW_rewritten': False, 'R_definition': 'sheafification of dense-open regular functions', 'K_definition': 'regular-denominator meromorphic sheaf; not generally R', 'affine_map': 'A tensor_B L=S^-1 A into K with fixed generic-field embedding', 'gluing': 'common affine refinements of both source and target; affine intersections need not be affine', 'separatedness_required': False, 'finite_type_required': False, 'Noetherian_required': False, 'generic_stalk': 'K tensor_L L to K multiplication isomorphism', 'global_injectivity': 'independently derived on every stalk S^-1 A_p into K', 'arbitrary_pullback_exactness_used': False, 'isomorphism_iff': 'entire point-set generic fiber f^-1(eta_Y)={eta_X}', 'generic_point_set_bijection_suffices': False, 'criterion_proof': 'localization primes contract to zero; one-prime domain is field equal to K; converse on affine sections', 'birationality': 'sufficient not necessary; arbitrary field extensions allowed', 'old_counterexample': 'A1_k to Spec k has O_X to R_X missing1/t at(t)', 'old_proof_gap': 'constancy needs compatible R_X-module quasi-coherence; O_X example cannot invert t', 'finite_component_hypotheses': 'finitely many components; every source generic maps to target generic', 'finite_component_reducedness_required': False, 'target_generic_surjectivity_required': False, 'finite_component_map': 'dense representatives and dense agreement pull back densely; sheafify then multiply', 'finite_component_stalks': 'generic local rings not necessarily fields; tensor multiplication iso', 'finite_component_global_injection_claimed': False, 'embedded_torsion': 'k[t,e]/(e^2,te); e survives at(t,e), ann(e)=(t,e), killed generically', 'map_to_field': 'rational map has kernel; flat meromorphic pullback exists', 'map_to_affine_line': 'rational pullback iso; meromorphic pullback undefined since t becomes zero divisor', 'bridge_0EMF': ['every weakly associated point is component generic', 'every quasi-compact open has finitely many components'], 'proofs_complete': True, 'old_and_corrected_sources_conflated': False, 'source_edition_mutated': False, 'official_tags_assigned': 0, 'new_root_theorem': False, 'formal_proof_checking': False, 'complete_EGA_claimed': False}
UNITS = ['ega:I.7.3.8', 'ega:I.7.3.8.1']
PROOFS = ['ega:I.7.3.8:proof']
UPSTREAM = 'a04446e57ec1fbc252a871afcec7752fb2807b14'
BASE = '027e32195209a05d1b28a854e030d71600c9c76b'
TARGET_COMMIT = '027e32195209a05d1b28a854e030d71600c9c76b'
DOSSIER = {'path': 'ega/i738.md', 'bytes': 15134, 'sha256': '105555649407DA07C90400359A95A48935F906F7816EE5B8B8BFE8A29D574E39'}

AUTHORITY = {'path': 'validation/ega-i-7.3.8-printed-replacement-authority-2026-09-08.json', 'bytes': 6890, 'sha256': '59EE5247301B33877F46FAFF8CCD92382FF4CCDC74C8F825EA1361CF6DBB3487'}

def authority_errors(raw):
    if not isinstance(raw, bytes) or len(raw) != AUTHORITY["bytes"] or hashlib.sha256(raw).hexdigest().upper() != AUTHORITY["sha256"]:
        return ["I7.3.8 separately bound printed replacement authority changed"]
    return []


def digest(raw):
    return hashlib.sha256(raw).hexdigest().upper()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def dossier_errors(raw, expected):
    if (expected != DOSSIER or not isinstance(raw, bytes) or len(raw) != DOSSIER["bytes"]
            or digest(raw) != DOSSIER["sha256"]):
        return ["I7.3.8 independently reviewed derivation dossier changed"]
    return []


def receipt_errors(raw):
    if (not isinstance(raw, bytes) or len(raw) != RECEIPT_BYTES
            or digest(raw) != RECEIPT_SHA256):
        return ["I7.3.8 immutable semantic receipt bytes changed"]
    return []


def verify(checkpoint, scope, tables, discovery, target_loader, tag_map, raw_loader):
    """Fail closed on metadata damage, then independently verify actual objects.

    The complete canonical seal is intentionally independent of mutable fixture
    hashes. Explicit semantic expectations document what was mathematically
    reviewed. Neither a true flag nor a matching checksum proves mathematics.
    """
    if (not all(isinstance(x, dict) for x in (checkpoint, scope, tables, discovery, tag_map))
            or not callable(target_loader) or not callable(raw_loader)):
        return ["I7.3.8 inputs must be objects and byte loaders callable"]
    try:
        if digest(canonical(checkpoint)) != CONTRACT_SHA256:
            return ["I7.3.8 reviewed semantic/source/target/ledger contract changed"]
    except (TypeError, ValueError, OverflowError):
        return ["I7.3.8 checkpoint must contain exact serializable JSON metadata"]
    errors = []
    if canonical(checkpoint["semantic_contract"]) != canonical(SEMANTICS):
        errors.append("I7.3.8 dense-open sheaf hypotheses and adverse examples changed")
    if (checkpoint["source_units"] != UNITS or checkpoint["source_proof_units"] != PROOFS
            or checkpoint["owned_unnumbered_parts"] != {}
            or checkpoint["next_semantic_cursor"] != "ega:I.7.4.1"
            or checkpoint["next_cursor_starts_with_numbered_environment"] is not False
            or checkpoint["starting_content_commit"] != BASE
            or checkpoint["stacks_upstream"] != UPSTREAM):
        errors.append("I7.3.8 exact source order parent ownership or base changed")
    reviewed = scope.get("reviewed_source_slices")
    if not isinstance(reviewed, dict):
        errors.append("I7.3.8 scope reviewed_source_slices must be an object")
    else:
        for unit, expected in checkpoint["french_authority"]["source_scopes"].items():
            if reviewed.get(unit) != expected:
                errors.append("I7.3.8 scope source ownership changed: " + unit)
    for key in ("statement_review_snapshot", "residual_snapshot"):
        if scope.get(key) != checkpoint[key]:
            errors.append("I7.3.8 live coverage snapshot changed: " + key)

    def read(loader, *args):
        try:
            raw = loader(*args)
            if not isinstance(raw, bytes):
                raise ValueError("expected raw bytes")
            return raw
        except (OSError, ValueError, TypeError, KeyError):
            errors.append("I7.3.8 byte object unavailable: " + str(args))
            return b""

    # Replay all twelve paired statement/proof blocks.
    # Official and integrated evidence retain distinct identities.
    cache = {}
    for target in checkpoint["targets"]:
        if tag_map.get(target["label"]) != target["tag"]:
            errors.append("I7.3.8 exact tag-label-file join changed: " + target["tag"])
        for edition, commit in (("official", UPSTREAM), ("integrated", TARGET_COMMIT)):
            span = target[edition]
            cache_key = (commit, target["path"])
            if cache_key not in cache:
                cache[cache_key] = read(target_loader, *cache_key)
            raw = cache[cache_key]
            lines = [line + b"\n" for line in raw.split(b"\n")[:-1]]
            block = b"".join(lines[span["lf_line_start"] - 1:span["lf_line_end"]])
            prefix = target["path"][:-4] + "-"
            short = target["label"][len(prefix):]
            if (span["commit"] != commit or not target["label"].startswith(prefix)
                    or len(raw) != span["source_bytes"] or digest(raw) != span["source_sha256"]
                    or len(block) != span["bytes"] or digest(block) != span["sha256"]
                    or raw[span["byte_offset_start"]:span["byte_offset_end_exclusive"]] != block
                    or block != span["text"].encode("utf-8")
                    or ("\\label{" + short + "}").encode() not in block):
                errors.append("I7.3.8 exact " + edition + " target bytes changed: " + target["tag"])

    if scope.get("next_semantic_cursor") != "ega:I.7.4.1":
        errors.append("I7.3.8 live semantic cursor changed")
    for context in checkpoint["target_contexts"]:
        for edition, commit in (("official", UPSTREAM), ("integrated", TARGET_COMMIT)):
            span = context[edition]
            key = (commit, context["path"])
            if key not in cache:
                cache[key] = read(target_loader, *key)
            raw = cache[key]
            lines = [line + b"\n" for line in raw.split(b"\n")[:-1]]
            block = b"".join(lines[span["lf_line_start"] - 1:span["lf_line_end"]])
            if (span["commit"] != commit or len(block) != span["bytes"]
                    or digest(block) != span["sha256"] or block != span["text"].encode("utf-8")
                    or raw[span["byte_offset_start"]:span["byte_offset_end_exclusive"]] != block):
                errors.append("I7.3.8 actual target context changed: " + context["name"])
    from tools.check_ega_i738_source_boundaries import validate_artifact
    for language in ("old_fr", "corrected_fr", "en"):
        errors.extend(validate_artifact(checkpoint["languages"][language], language))

    for unit, expected in checkpoint["french_authority"]["reviewed_errata_scopes"].items():
        if not isinstance(scope.get("reviewed_errata_slices"), dict) or scope["reviewed_errata_slices"].get(unit) != expected:
            errors.append("I7.3.8 exact printed errata scope changed")
    errors.extend(authority_errors(read(raw_loader, AUTHORITY["path"])))
    if checkpoint["french_authority"]["primary_binding"] != AUTHORITY:
        errors.append("I7.3.8 printed authority identity changed")
    unit_set = set(UNITS + PROOFS)
    for ledger in checkpoint["ledgers"]:
        path, key = ledger["path"], ledger["id_field"]
        rows = tables.get(path)
        if (not isinstance(rows, list) or any(not isinstance(r, dict)
                or any(not isinstance(k, str) or (v is not None and not isinstance(v, str))
                       for k, v in r.items()) for r in rows)):
            errors.append("I7.3.8 actual ledger must contain exact CSV text rows: " + path)
            continue
        ids = {r[key] for r in ledger["rows"]}
        if [r for r in rows if r.get(key) in ids] != ledger["rows"]:
            errors.append("I7.3.8 exact reviewed ledger rows changed: " + path)
        if path != "ega/agent.csv":
            source_key = "subject_id" if path == "ega/dec.csv" else "source_unit"
            if [r for r in rows if r.get(source_key) in unit_set] != ledger["rows"]:
                errors.append("I7.3.8 source-unit ledger closure changed: " + path)
        raw = read(raw_loader, path)
        if b"\r" in raw or not raw.endswith(b"\n"):
            errors.append("I7.3.8 ledger must have exact LF serialization: " + path)
        lines = [line + b"\n" for line in raw.split(b"\n")[:-1]]
        prefix = b"".join(lines[:ledger["prefix_rows"] + 1])
        append = b"".join(lines[ledger["prefix_rows"] + 1:ledger["final_rows"] + 1])
        for block, size, seal, part in ((prefix, ledger["prefix_bytes"], ledger["prefix_sha256"], "prior prefix"),
                (append, ledger["append_bytes"], ledger["append_sha256"], "reviewed append"),
                (raw, ledger["bytes"], ledger["sha256"], "current postimage")):
            if len(block) != size or digest(block) != seal:
                errors.append("I7.3.8 " + part + " changed: " + path)
        # Verify supplied runtime rows are the active view of the actual bytes.
        parsed = list(csv.DictReader(io.StringIO(raw.decode("utf-8", errors="replace"), newline="")))
        superseded = {r.get("supersedes") for r in parsed if r.get("supersedes")}
        active = [r for r in parsed if r.get(key) not in superseded]
        if rows != active:
            errors.append("I7.3.8 supplied table disagrees with actual active byte view: " + path)

    actual_gaps = [r for r in tables.get("ega/resid.csv", []) if isinstance(r, dict) and r.get("status") == "open_gap"] if isinstance(tables.get("ega/resid.csv"), list) else []
    if actual_gaps != checkpoint["preserved_open_gap_rows"] or len(actual_gaps) != 12:
        errors.append("I7.3.8 prior twelve open gaps changed or were falsely closed")
    expected_units = checkpoint["english_discovery"]["stable_units"]
    if len(expected_units) != 3 or {r["unit_id"] for r in expected_units} != unit_set:
        errors.append("I7.3.8 exact three discovery units changed")
    for row in expected_units:
        if discovery.get(row["unit_id"]) != row:
            errors.append("I7.3.8 discovery changed or promoted: " + row["unit_id"])
    # Supplied discovery dictionaries must be the exact live CSV view, not
    # three correct rows accompanied by an invented741unit or earlier tail unit.
    discovery_raw = read(raw_loader, "ega/units.csv")
    discovery_rows = list(csv.DictReader(io.StringIO(
        discovery_raw.decode("utf-8", errors="replace"), newline="")))
    parsed_discovery = {r.get("unit_id"): r for r in discovery_rows}
    if discovery != parsed_discovery or len(parsed_discovery) != len(discovery_rows):
        errors.append("I7.3.8 supplied discovery disagrees with exact live CSV inventory")
    for item in checkpoint["preserved_inputs"] + checkpoint["reviewed_artifacts"]:
        raw = read(raw_loader, item["path"])
        if len(raw) != item["bytes"] or digest(raw) != item["sha256"]:
            errors.append("I7.3.8 preserved input changed: " + item["path"])
    errors.extend(dossier_errors(read(raw_loader, DOSSIER["path"]), checkpoint["derivation_dossier"]))
    return errors
