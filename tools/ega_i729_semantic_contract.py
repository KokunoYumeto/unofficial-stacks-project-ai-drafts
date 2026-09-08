"""Exact EGA I7.2.8--7.2.9 evidence contracts, not a formal proof checker.

The immutable receipt seal protects reviewed metadata against self-rehashing.
Actual source/target/ledger objects are checked separately: a receipt copy is
not evidence that those bytes exist. Live source retrieval remains the bounded
raw-source replay tool's job; this offline checker does not claim to fetch it.
"""
import csv
import hashlib
import io
import json

RECEIPT_PATH = 'validation/ega-i-7.2.8-7.2.9-semantic-checkpoint-2026-09-08.json'
RECEIPT_BYTES = 78280
RECEIPT_SHA256 = 'FF484AB63BFCD5E67780C8A395309EAF0FB2A3F8C620D3123DA44D59F5243FE8'
CONTRACT_SHA256 = '57136680408C4205BF6B0ABE21EE8CC6CDE3B04B9146089576EC37A19001E79B'
SEMANTICS = {'absolute_domain': 'union of ordinary representative domains', 'relative_domain': 'union of S-morphism representative domains', 'I728_X_reduced': True, 'I728_Y_separated_over_S': True, 'I728_canonical_local_scheme_image': 'generalizations of x; contained in every neighbourhood of x', 'I728_local_scheme_is_open_neighbourhood': False, 'I728_dense_pullback_alternatives': 'integral X or locally Noetherian X', 'I728_representative_independence_uses_dense_agreement_pullback': True, 'I728_induced_map_preserves_base_S': True, 'I728_parent_induced_map_owned_separately_from_nested_proof': True, 'I7281_hypothesis': 'underlying topological space locally Noetherian', 'I7281_coordinate_rings_required_Noetherian': False, 'I7281_minimal_primes_correspond_both_directions': True, 'I7281_components_are_traces_of_global_components_through_x': True, 'I7281_generic_local_rings_identified_by_iterated_localization': True, 'I7281_density_equivalence': 'inverse image of W dense iff W meets every component through x', 'I7281_dense_W_implies_dense_pullback': True, 'I7281_finite_component_topology_retained': True, 'I729_S_locally_Noetherian': True, 'I729_X_reduced': True, 'I729_X_alternatives': 'irreducible or locally Noetherian', 'I729_Y_separated_over_S': True, 'I729_source_Y_finite_type': True, 'I729_valid_criterion': 'x in D_S iff induced rational S-map has an S-morphism representative on all L_x', 'I729_local_map_is_O_Ss_algebra_map': True, 'I729_necessity_restricts_to_canonical_local_scheme': True, 'I729_source_faithful_spreading_route': '01TX then0BX6(2a)', 'I729_generic_agreement_requires_local_morphisms_not_only_points': True, 'I729_integral_branch_uses_0BX6_1a_and_dense_agreement': True, 'I729_integral_X_required_Noetherian': False, 'I729_Noetherian_branch_removes_components_not_through_x': True, 'I729_Noetherian_branch_all_generic_local_maps_agree': True, 'I729_globalization_domain': 'Q=V union ((X minus closure V) intersect W)', 'I729_globalization_agreement': 'E union ((X minus closure V) intersect W) dense in X', 'I729_V_assumed_dense_in_X': False, 'I729_relative_maximal_gluing_uses_reduced_and_separated': True, 'I729_stronger_route_separate': '0BX6(2b,c): locally finite type Y/S and no locally Noetherian S hypothesis', 'I729_ordinary_local_morphism_suffices': False, 'adverse_seed_00PB_is_whole_counterexample': False, 'adverse_D': 'DVR of finite coefficient-field series over k^p in k[[z]]', 'adverse_q': 'sum t_i z^i not in F; q^p in D', 'adverse_C': 'D[q] finite one-dimensional Noetherian local domain', 'adverse_A': 'K intersect k[[z]] is DVR normalization of C; nonfinite by Nakayama', 'adverse_R': 'C[T_a,aT_a for a in A]', 'adverse_A_contained_in_R_p': True, 'adverse_A_contained_in_any_R_b_for_b_outside_p': False, 'adverse_specialization': 'T_a=1 on finite support J and T_a=0 outside J', 'adverse_finite_support_image_B_finite_over_C': True, 'adverse_S': 'Spec C glued to Spec A along common generic open Spec K; distinct closed points', 'adverse_S_locally_Noetherian': True, 'adverse_X_integral': True, 'adverse_Y_over_S': 'quasi-compact separated open immersion', 'adverse_01TT_proves': 'locally finite presentation only', 'adverse_global_finite_presentation_uses': 'quasi-compactness and quasi-separatedness from separatedness', 'adverse_f_on_Dz_is_S_morphism': True, 'adverse_local_h_is_ordinary_morphism': True, 'adverse_local_h_is_S_morphism': False, 'adverse_x_in_ordinary_domain': False, 'adverse_h_disagrees_with_structure_at_closed_base_points': True, 'target_0BX8_role': 'comparison only; not identical historical hypotheses or full proof', 'source_cross_reference_discrepancy': 'FR476:0.1.2.6 versus EN283:0.2.1.6; tokens unchanged', 'source_edition_mutated': False, 'printed_erratum_claimed': False, 'new_root_theorem': False, 'official_tags_assigned': 0, 'formal_proof_checking': False, 'complete_EGA_claimed': False}
UNITS = ['ega:I.7.2.8', 'ega:I.7.2.8.1', 'ega:I.7.2.9']
PROOFS = ['ega:I.7.2.8.1:proof', 'ega:I.7.2.9:proof']
UPSTREAM = 'a04446e57ec1fbc252a871afcec7752fb2807b14'
BASE = 'ded26271cc55edd554e5ddbd14787870386dbfe1'
DOSSIER = {'path': 'ega/i729.md', 'bytes': 15631, 'sha256': 'CF028E092E8AE86FD52B43125771819F8F8FD4011E97109D44FBDF9C0FB9AAC7'}


def digest(raw):
    return hashlib.sha256(raw).hexdigest().upper()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def dossier_errors(raw, expected):
    if (expected != DOSSIER or not isinstance(raw, bytes) or len(raw) != DOSSIER["bytes"]
            or digest(raw) != DOSSIER["sha256"]):
        return ["I7.2.9 independently reviewed derivation dossier changed"]
    return []


def receipt_errors(raw):
    if (not isinstance(raw, bytes) or len(raw) != RECEIPT_BYTES
            or digest(raw) != RECEIPT_SHA256):
        return ["I7.2.9 immutable semantic receipt bytes changed"]
    return []


def verify(checkpoint, scope, tables, discovery, target_loader, tag_map, raw_loader):
    """Fail closed on metadata damage, then independently verify actual objects.

    The complete canonical seal is intentionally independent of mutable fixture
    hashes. Explicit semantic expectations document what was mathematically
    reviewed. Neither a true flag nor a matching checksum proves mathematics.
    """
    if (not all(isinstance(x, dict) for x in (checkpoint, scope, tables, discovery, tag_map))
            or not callable(target_loader) or not callable(raw_loader)):
        return ["I7.2.9 inputs must be objects and byte loaders callable"]
    try:
        if digest(canonical(checkpoint)) != CONTRACT_SHA256:
            return ["I7.2.9 reviewed semantic/source/target/ledger contract changed"]
    except (TypeError, ValueError, OverflowError):
        return ["I7.2.9 checkpoint must contain exact serializable JSON metadata"]
    errors = []
    if canonical(checkpoint["semantic_contract"]) != canonical(SEMANTICS):
        errors.append("I7.2.9 hypotheses proof branches and adverse construction changed")
    if (checkpoint["source_units"] != UNITS or checkpoint["source_proof_units"] != PROOFS
            or checkpoint["owned_unnumbered_parts"] != {"ega:I.7.2.8:induced-map": "ega:I.7.2.8"}
            or checkpoint["next_semantic_cursor"] != "ega:I.7.3"
            or checkpoint["next_cursor_starts_with_numbered_environment"] is not False
            or checkpoint["starting_content_commit"] != BASE
            or checkpoint["stacks_upstream"] != UPSTREAM):
        errors.append("I7.2.9 exact source order parent ownership or base changed")
    reviewed = scope.get("reviewed_source_slices")
    if not isinstance(reviewed, dict):
        errors.append("I7.2.9 scope reviewed_source_slices must be an object")
    else:
        for unit, expected in checkpoint["french_authority"]["source_scopes"].items():
            if reviewed.get(unit) != expected:
                errors.append("I7.2.9 scope source ownership changed: " + unit)
    for key in ("statement_review_snapshot", "residual_snapshot"):
        if scope.get(key) != checkpoint[key]:
            errors.append("I7.2.9 live coverage snapshot changed: " + key)

    def read(loader, *args):
        try:
            raw = loader(*args)
            if not isinstance(raw, bytes):
                raise ValueError("expected raw bytes")
            return raw
        except (OSError, ValueError, TypeError, KeyError):
            errors.append("I7.2.9 byte object unavailable: " + str(args))
            return b""

    # Replay all eighteen official/current blocks, including unequal current
    # 00E3,0052,01JB bytes. A current block cannot stand in for its official one.
    cache = {}
    for target in checkpoint["targets"]:
        if tag_map.get(target["label"]) != target["tag"]:
            errors.append("I7.2.9 exact tag-label-file join changed: " + target["tag"])
        for edition, commit in (("official", UPSTREAM), ("integrated", BASE)):
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
                    or len(block) != span["bytes"] or digest(block) != span["sha256"]
                    or ("\\label{" + short + "}").encode() not in block):
                errors.append("I7.2.9 exact " + edition + " target bytes changed: " + target["tag"])

    unit_set = set(UNITS + PROOFS)
    for ledger in checkpoint["ledgers"]:
        path, key = ledger["path"], ledger["id_field"]
        rows = tables.get(path)
        if (not isinstance(rows, list) or any(not isinstance(r, dict)
                or any(not isinstance(k, str) or (v is not None and not isinstance(v, str))
                       for k, v in r.items()) for r in rows)):
            errors.append("I7.2.9 actual ledger must contain exact CSV text rows: " + path)
            continue
        ids = {r[key] for r in ledger["rows"]}
        if [r for r in rows if r.get(key) in ids] != ledger["rows"]:
            errors.append("I7.2.9 exact reviewed ledger rows changed: " + path)
        if path != "ega/agent.csv":
            source_key = "subject_id" if path == "ega/dec.csv" else "source_unit"
            if [r for r in rows if r.get(source_key) in unit_set] != ledger["rows"]:
                errors.append("I7.2.9 source-unit ledger closure changed: " + path)
        raw = read(raw_loader, path)
        if b"\r" in raw or not raw.endswith(b"\n"):
            errors.append("I7.2.9 ledger must have exact LF serialization: " + path)
        lines = [line + b"\n" for line in raw.split(b"\n")[:-1]]
        prefix = b"".join(lines[:ledger["prefix_rows"] + 1])
        append = b"".join(lines[ledger["prefix_rows"] + 1:ledger["final_rows"] + 1])
        for block, size, seal, part in ((prefix, ledger["prefix_bytes"], ledger["prefix_sha256"], "prior prefix"),
                (append, ledger["append_bytes"], ledger["append_sha256"], "reviewed append"),
                (raw, ledger["bytes"], ledger["sha256"], "current postimage")):
            if len(block) != size or digest(block) != seal:
                errors.append("I7.2.9 " + part + " changed: " + path)
        # Verify supplied runtime rows are the active view of the actual bytes.
        parsed = list(csv.DictReader(io.StringIO(raw.decode("utf-8", errors="replace"), newline="")))
        superseded = {r.get("supersedes") for r in parsed if r.get("supersedes")}
        active = [r for r in parsed if r.get(key) not in superseded]
        if rows != active:
            errors.append("I7.2.9 supplied table disagrees with actual active byte view: " + path)

    actual_gaps = [r for r in tables.get("ega/resid.csv", []) if isinstance(r, dict) and r.get("status") == "open_gap"] if isinstance(tables.get("ega/resid.csv"), list) else []
    if actual_gaps != checkpoint["preserved_open_gap_rows"] or len(actual_gaps) != 12:
        errors.append("I7.2.9 prior twelve open gaps changed or were falsely closed")
    expected_units = checkpoint["english_discovery"]["stable_units"]
    if len(expected_units) != 5 or {r["unit_id"] for r in expected_units} != unit_set:
        errors.append("I7.2.9 exact five discovery units changed")
    for row in expected_units:
        if discovery.get(row["unit_id"]) != row:
            errors.append("I7.2.9 discovery changed or promoted: " + row["unit_id"])
    # Supplied discovery dictionaries must be the exact live CSV view, not
    # five correct rows accompanied by an invented parent proof or prose unit.
    discovery_raw = read(raw_loader, "ega/units.csv")
    discovery_rows = list(csv.DictReader(io.StringIO(
        discovery_raw.decode("utf-8", errors="replace"), newline="")))
    parsed_discovery = {r.get("unit_id"): r for r in discovery_rows}
    if discovery != parsed_discovery or len(parsed_discovery) != len(discovery_rows):
        errors.append("I7.2.9 supplied discovery disagrees with exact live CSV inventory")
    for item in checkpoint["preserved_inputs"]:
        raw = read(raw_loader, item["path"])
        if len(raw) != item["bytes"] or digest(raw) != item["sha256"]:
            errors.append("I7.2.9 preserved input changed: " + item["path"])
    errors.extend(dossier_errors(read(raw_loader, DOSSIER["path"]), checkpoint["derivation_dossier"]))
    return errors
