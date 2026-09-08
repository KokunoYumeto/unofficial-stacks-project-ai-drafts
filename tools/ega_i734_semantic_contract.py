"""Exact EGA I7.3.1--7.3.4 evidence contracts, not a formal proof checker.

The immutable receipt seal protects reviewed metadata against self-rehashing.
Actual source/target/ledger objects are checked separately: a receipt copy is
not evidence that those bytes exist. Live source retrieval remains the bounded
raw-source replay tool's job; this offline checker does not claim to fetch it.
"""
import csv
import hashlib
import io
import json

RECEIPT_PATH = 'validation/ega-i-7.3.1-7.3.4-semantic-checkpoint-2026-09-08.json'
RECEIPT_BYTES = 162185
RECEIPT_SHA256 = 'B9C0C421F58F12064B8F6B37FE5E45F111631510F396C24E0CEA26E88DE591A4'
CONTRACT_SHA256 = 'FF9C524D12011A5E4D81B01D13D6C6B99EA21CF51BAECF30BCF8D7BDA8BD9AAE'
SEMANTICS = json.loads(r'''{"rational_presheaf":"equivalence classes of regular functions on topologically dense opens","meromorphic_sheaf":"sheafification of localization at regular sections","R_equals_K_general_nonreduced":false,"I731_representative_independence_by_dense_intersections":true,"I731_restriction_scalar_map":"Gamma(U,O_X) to Gamma(V,O_X)","I731_identity_and_composition":true,"I731_reducedness_required":false,"I731_Noetherianity_required":false,"I732_ring_sheafification_and_O_X_algebra":true,"I732_structure_map_injective_claimed":false,"I732_open_restriction_tail":"same presheaf on V and cofinal neighbourhood germs; algebra-compatible sheaf identification","I733_hypothesis":"locally finite family of irreducible components","I733_topologically_locally_Noetherian_special_case":true,"I733_coordinate_rings_required_Noetherian":false,"I733_reducedness_required":false,"I733_section_formula_scope":"every open meeting finitely many components","I733_generic_factors":"generic local rings; not necessarily residue fields","I733_naturality":"generic germs; restriction is projection onto remaining generic coordinates","I733_arbitrary_infinite_cover_gluing":true,"I733_local_finite_not_global_finite":true,"I733_affine_module":"finite direct sum equals finite product of A_p over minimal primes","I733_localization_notin_prime":"unit leaves factor unchanged","I733_localization_in_prime":"individual image nilpotent; localized factor zero","I733_maximal_ideal_nilpotent_required":false,"I733_infinite_product_localization_interchanged":false,"I733_full_final_affine_argument":"principal-open modules and restrictions agree; basis gluing identifies associated sheaf; affine local cover gives quasi-coherence","I733_algebra_compatibility":true,"I733_generic_notation_replaced_by_reduced_component":false,"adverse_RK_ring":"k[t,e]/(e^2,te)","adverse_RK_e_nonzero":true,"adverse_RK_Dt_dense":true,"adverse_RK_t_nonzerodivisor":false,"adverse_RK_generic_local_ring":"k(t)","adverse_RK_O_to_R_kills_e":true,"adverse_RK_O_to_K_injective":true,"target_0EMF_extra_hypothesis":"every weakly associated point is generic","target_0EMF_extra_hypothesis_imported_into_EGA":false,"target_01X5_role":"integral specialization only","I734_X_reduced":true,"I734_global_finite_components":true,"I734_components":"unique reduced closed structures; integral","I734_decomposition":"finite product of h_i direct image of R_Xi as O_X algebras","I734_generic_fields_identified_after_reducedness":true,"I734_proof_printed":false,"I734_proof_supplied_independently":true,"I734_all_open_sections_restrictions_and_scalar_action_checked":true,"adverse_reducedness":"Spec k[e]/e^2 has R=k[e]/e^2 while its reduced component has R=k","empty_open_and_scheme":"empty product of rings is zero ring","source_section_heading_owned":true,"source_page_marker_owner":"ega:I.7.3.2","source_732_tail_owned":true,"source_733_entire_proof_owned":true,"source_735_excluded":true,"source_edition_mutated":false,"printed_erratum_claimed":false,"new_root_theorem":false,"official_tags_assigned":0,"formal_proof_checking":false,"complete_EGA_claimed":false}''')
UNITS = ["ega:I.7.3.1","ega:I.7.3.2","ega:I.7.3.3","ega:I.7.3.4"]
PROOFS = ["ega:I.7.3.3:proof"]
UPSTREAM = 'a04446e57ec1fbc252a871afcec7752fb2807b14'
BASE = 'dd42eef7f1542d3f2d5ff28299014c39ebe7f7d1'
TARGET_COMMIT = '1bed4dc0cb48717c476c7292b91b018743e9a530'
DOSSIER = {"path":"ega/i734.md","bytes":16660,"sha256":"D4F939E921750A907E0B335DB9D9DA9242EC407B90AD7561EA63C9682C5C3163"}


def digest(raw):
    return hashlib.sha256(raw).hexdigest().upper()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def dossier_errors(raw, expected):
    if (expected != DOSSIER or not isinstance(raw, bytes) or len(raw) != DOSSIER["bytes"]
            or digest(raw) != DOSSIER["sha256"]):
        return ["I7.3.4 independently reviewed derivation dossier changed"]
    return []


def receipt_errors(raw):
    if (not isinstance(raw, bytes) or len(raw) != RECEIPT_BYTES
            or digest(raw) != RECEIPT_SHA256):
        return ["I7.3.4 immutable semantic receipt bytes changed"]
    return []


def verify(checkpoint, scope, tables, discovery, target_loader, tag_map, raw_loader):
    """Fail closed on metadata damage, then independently verify actual objects.

    The complete canonical seal is intentionally independent of mutable fixture
    hashes. Explicit semantic expectations document what was mathematically
    reviewed. Neither a true flag nor a matching checksum proves mathematics.
    """
    if (not all(isinstance(x, dict) for x in (checkpoint, scope, tables, discovery, tag_map))
            or not callable(target_loader) or not callable(raw_loader)):
        return ["I7.3.4 inputs must be objects and byte loaders callable"]
    try:
        if digest(canonical(checkpoint)) != CONTRACT_SHA256:
            return ["I7.3.4 reviewed semantic/source/target/ledger contract changed"]
    except (TypeError, ValueError, OverflowError):
        return ["I7.3.4 checkpoint must contain exact serializable JSON metadata"]
    errors = []
    if canonical(checkpoint["semantic_contract"]) != canonical(SEMANTICS):
        errors.append("I7.3.4 dense-open sheaf hypotheses and adverse examples changed")
    if (checkpoint["source_units"] != UNITS or checkpoint["source_proof_units"] != PROOFS
            or checkpoint["owned_unnumbered_parts"] != {"ega:I.7.3.2:restriction-tail": "ega:I.7.3.2"}
            or checkpoint["next_semantic_cursor"] != "ega:I.7.3.5"
            or checkpoint["next_cursor_starts_with_numbered_environment"] is not True
            or checkpoint["starting_content_commit"] != BASE
            or checkpoint["stacks_upstream"] != UPSTREAM):
        errors.append("I7.3.4 exact source order parent ownership or base changed")
    reviewed = scope.get("reviewed_source_slices")
    if not isinstance(reviewed, dict):
        errors.append("I7.3.4 scope reviewed_source_slices must be an object")
    else:
        for unit, expected in checkpoint["french_authority"]["source_scopes"].items():
            if reviewed.get(unit) != expected:
                errors.append("I7.3.4 scope source ownership changed: " + unit)
    for key in ("statement_review_snapshot", "residual_snapshot"):
        if scope.get(key) != checkpoint[key]:
            errors.append("I7.3.4 live coverage snapshot changed: " + key)

    def read(loader, *args):
        try:
            raw = loader(*args)
            if not isinstance(raw, bytes):
                raise ValueError("expected raw bytes")
            return raw
        except (OSError, ValueError, TypeError, KeyError):
            errors.append("I7.3.4 byte object unavailable: " + str(args))
            return b""

    # Replay sixteen paired statement/proof blocks and three paired contexts.
    # Official and integrated evidence retain distinct identities.
    cache = {}
    for target in checkpoint["targets"]:
        if tag_map.get(target["label"]) != target["tag"]:
            errors.append("I7.3.4 exact tag-label-file join changed: " + target["tag"])
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
                errors.append("I7.3.4 exact " + edition + " target bytes changed: " + target["tag"])

    if scope.get("next_semantic_cursor") != "ega:I.7.3.5":
        errors.append("I7.3.4 live semantic cursor changed")
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
                errors.append("I7.3.4 actual target context changed: " + context["name"])
    from tools.check_ega_i734_source_boundaries import validate_artifact
    for language in ("fr", "en"):
        errors.extend(validate_artifact(checkpoint["languages"][language], language))

    unit_set = set(UNITS + PROOFS)
    for ledger in checkpoint["ledgers"]:
        path, key = ledger["path"], ledger["id_field"]
        rows = tables.get(path)
        if (not isinstance(rows, list) or any(not isinstance(r, dict)
                or any(not isinstance(k, str) or (v is not None and not isinstance(v, str))
                       for k, v in r.items()) for r in rows)):
            errors.append("I7.3.4 actual ledger must contain exact CSV text rows: " + path)
            continue
        ids = {r[key] for r in ledger["rows"]}
        if [r for r in rows if r.get(key) in ids] != ledger["rows"]:
            errors.append("I7.3.4 exact reviewed ledger rows changed: " + path)
        if path != "ega/agent.csv":
            source_key = "subject_id" if path == "ega/dec.csv" else "source_unit"
            if [r for r in rows if r.get(source_key) in unit_set] != ledger["rows"]:
                errors.append("I7.3.4 source-unit ledger closure changed: " + path)
        raw = read(raw_loader, path)
        if b"\r" in raw or not raw.endswith(b"\n"):
            errors.append("I7.3.4 ledger must have exact LF serialization: " + path)
        lines = [line + b"\n" for line in raw.split(b"\n")[:-1]]
        prefix = b"".join(lines[:ledger["prefix_rows"] + 1])
        append = b"".join(lines[ledger["prefix_rows"] + 1:ledger["final_rows"] + 1])
        for block, size, seal, part in ((prefix, ledger["prefix_bytes"], ledger["prefix_sha256"], "prior prefix"),
                (append, ledger["append_bytes"], ledger["append_sha256"], "reviewed append"),
                (raw, ledger["bytes"], ledger["sha256"], "current postimage")):
            if len(block) != size or digest(block) != seal:
                errors.append("I7.3.4 " + part + " changed: " + path)
        # Verify supplied runtime rows are the active view of the actual bytes.
        parsed = list(csv.DictReader(io.StringIO(raw.decode("utf-8", errors="replace"), newline="")))
        superseded = {r.get("supersedes") for r in parsed if r.get("supersedes")}
        active = [r for r in parsed if r.get(key) not in superseded]
        if rows != active:
            errors.append("I7.3.4 supplied table disagrees with actual active byte view: " + path)

    actual_gaps = [r for r in tables.get("ega/resid.csv", []) if isinstance(r, dict) and r.get("status") == "open_gap"] if isinstance(tables.get("ega/resid.csv"), list) else []
    if actual_gaps != checkpoint["preserved_open_gap_rows"] or len(actual_gaps) != 12:
        errors.append("I7.3.4 prior twelve open gaps changed or were falsely closed")
    expected_units = checkpoint["english_discovery"]["stable_units"]
    if len(expected_units) != 5 or {r["unit_id"] for r in expected_units} != unit_set:
        errors.append("I7.3.4 exact five discovery units changed")
    for row in expected_units:
        if discovery.get(row["unit_id"]) != row:
            errors.append("I7.3.4 discovery changed or promoted: " + row["unit_id"])
    # Supplied discovery dictionaries must be the exact live CSV view, not
    # five correct rows accompanied by an invented734proof or732tail unit.
    discovery_raw = read(raw_loader, "ega/units.csv")
    discovery_rows = list(csv.DictReader(io.StringIO(
        discovery_raw.decode("utf-8", errors="replace"), newline="")))
    parsed_discovery = {r.get("unit_id"): r for r in discovery_rows}
    if discovery != parsed_discovery or len(parsed_discovery) != len(discovery_rows):
        errors.append("I7.3.4 supplied discovery disagrees with exact live CSV inventory")
    for item in checkpoint["preserved_inputs"]:
        raw = read(raw_loader, item["path"])
        if len(raw) != item["bytes"] or digest(raw) != item["sha256"]:
            errors.append("I7.3.4 preserved input changed: " + item["path"])
    errors.extend(dossier_errors(read(raw_loader, DOSSIER["path"]), checkpoint["derivation_dossier"]))
    return errors
