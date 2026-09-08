"""Exact EGA I7.3.5--7.3.7 evidence contracts, not a formal proof checker.

The immutable receipt seal protects reviewed metadata against self-rehashing.
Actual source/target/ledger objects are checked separately: a receipt copy is
not evidence that those bytes exist. Live source retrieval remains the bounded
raw-source replay tool's job; this offline checker does not claim to fetch it.
"""
import csv
import hashlib
import io
import json

RECEIPT_PATH = 'validation/ega-i-7.3.5-7.3.7-semantic-checkpoint-2026-09-08.json'
RECEIPT_BYTES = 193957
RECEIPT_SHA256 = '891F0C7369DC5BFF1AC9378A1A860C714D38C9D66EF3193AA748B31DF3F9DCB0'
CONTRACT_SHA256 = 'A1B0349653308968AEA265817CBBDAA75D4CAF673B52D9D0591EBA16476AA4C1'
SEMANTICS = {'historical_simple': 'constant sheaf; not simple module', 'original_french_chapter0_visual_read': 'attributed to preflight source reviewer; no new implementation visual read', 'english_chapter0_in_french_repository': 'comparison only, not French authority', 'R_definition': 'sheafification of dense-open rational functions', 'R_equals_K_general_nonreduced': False, 'I735_X': 'nonempty irreducible scheme; no reducedness or Noetherianity required', 'I735_ring': 'R_X; generic local ring B=O_Xeta need not be a field', 'I735_sections': 'B on every nonempty open; identity restrictions', 'I735_presentation_indices': 'arbitrary sets; sheaf direct sums, not products', 'I735_french_parentheses_preserved': True, 'I735_english_missing_parentheses_preserved': True, 'I735_coproduct': 'constant B^(I) by stalkwise comparison', 'I735_matrix': 'column finite, not necessarily finite matrix', 'I735_cokernel': 'constant coker(u) by stalkwise exactness', 'global_sections_right_exactness_assumed': False, 'I735_gluing': 'canonical identity at eta on every nonempty overlap', 'I735_scalar_equivalence': 'R_X quasi-coherence iff underlying O_X quasi-coherence, on these schemes', 'I735_converse': 'local associated module; compatible B-action; arbitrary B-free presentation', 'general_ringed_space_arbitrary_sum_closure_claimed': False, 'I736_starting_ring': 'O_X', 'I736_tensor_presentation': 'right exact and commutes with arbitrary sums', 'I736_flatness_required': False, 'I736_identity_space_morphism': 'ringed spaces, not asserted locally ringed', 'I736_generic_fibre': 'F_eta tensor_B B canonically F_eta', 'I736_constancy': 'canonical constant F_eta', 'I736_free_case': 'X reduced and irreducible, hence integral; B field', 'I736_basis': 'possibly infinite, chosen; freeness isomorphism not canonical', 'I736_finite_rank_required': False, 'I736_printed_proof': 'one sentence for second assertion; first assertion supplied independently', 'I737_qcoherence_hypotheses': 'locally integral or locally Noetherian scheme', 'I737_locally_finite_components': 'more general sufficient hypothesis, not stronger premise', 'I737_coordinate_Noetherian_equated_with_topological': False, 'I737_global_finite_components_required': False, 'I737_injection': 'all reduced schemes, independent of component finiteness', 'I737_injection_argument': 'unchanged sheafification stalk; dense-open zero; D(a) empty; nilpotent; reduced gives zero', 'I737_X_separated_required': False, 'I737_locally_integral_implies_reduced': True, 'adverse_simple_module': 'k^2 over Spec k has proper nonzero submodule', 'adverse_qcoherence': 'closed-point K skyscraper on affine line has generic stalk zero', 'adverse_irreducibility': 'two-point quasi-coherent fibres k and0 are not constant or uniformly free', 'adverse_freeness': 'k over dual numbers is constant and nonfree', 'adverse_injection': 'k[t,e]/(e^2,te); dense D(t) kills nonzero e; regular denominators cannot', 'reducedness_necessary_for_injection': False, 'adverse_nonreduced_injection': 'one-point dual numbers have O_X=R_X', 'empty_case': 'zero sheaves, empty sum, no generic point', 'all_three_printed_proofs_owned': True, 'page_marker_owner': 'ega:I.7.3.7', 'section_heading_reowned': False, 'source_738_excluded': True, 'source_edition_mutated': False, 'new_root_theorem': False, 'official_tags_assigned': 0, 'formal_proof_checking': False, 'complete_EGA_claimed': False, 'adverse_skyscraper_scalar_action': 'S_x(U)=K if x in U and zero otherwise; identity or zero restrictions; O_Xx to K action, not a module pushforward from Spec kappa(x)'}
UNITS = ['ega:I.7.3.5', 'ega:I.7.3.6', 'ega:I.7.3.7']
PROOFS = ['ega:I.7.3.5:proof', 'ega:I.7.3.6:proof', 'ega:I.7.3.7:proof']
UPSTREAM = 'a04446e57ec1fbc252a871afcec7752fb2807b14'
BASE = '20307123eefacd21760bdf6f306774c09d4bab18'
TARGET_COMMIT = '1bed4dc0cb48717c476c7292b91b018743e9a530'
DOSSIER = {'path': 'ega/i737.md', 'bytes': 16406, 'sha256': '4AF5241FB491CAFDCD7484D359E2C06286BE5DC3AE4DAEE139B8643AD8FDCBB2'}


def digest(raw):
    return hashlib.sha256(raw).hexdigest().upper()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def dossier_errors(raw, expected):
    if (expected != DOSSIER or not isinstance(raw, bytes) or len(raw) != DOSSIER["bytes"]
            or digest(raw) != DOSSIER["sha256"]):
        return ["I7.3.7 independently reviewed derivation dossier changed"]
    return []


def receipt_errors(raw):
    if (not isinstance(raw, bytes) or len(raw) != RECEIPT_BYTES
            or digest(raw) != RECEIPT_SHA256):
        return ["I7.3.7 immutable semantic receipt bytes changed"]
    return []


def historical_inputs(checkpoint, scope, raw_loader):
    """Project sealed 737 prefixes without suppressing successor ledger rows.

    The immutable receipt is checked before accepting its projection bounds.
    The old full postimage remains exact; current snapshots/cursor belong to
    the successor contract and are not mistaken for 737's original frontier.
    """
    if digest(canonical(checkpoint)) != CONTRACT_SHA256:
        raise ValueError("I7.3.7 historical projection requires the sealed receipt")
    historical_raw, tables = {}, {}
    for ledger in checkpoint["ledgers"]:
        path = ledger["path"]
        raw = raw_loader(path)
        if not isinstance(raw, bytes) or b"\r" in raw or not raw.endswith(b"\n"):
            raise ValueError("I7.3.7 invalid live ledger serialization: " + path)
        lines = [line + b"\n" for line in raw.split(b"\n")[:-1]]
        frozen = b"".join(lines[:ledger["final_rows"] + 1])
        if len(frozen) != ledger["bytes"] or digest(frozen) != ledger["sha256"]:
            raise ValueError("I7.3.7 historical ledger prefix changed: " + path)
        historical_raw[path] = frozen
        rows = list(csv.DictReader(io.StringIO(frozen.decode("utf-8"), newline="")))
        superseded = {r.get("supersedes") for r in rows if r.get("supersedes")}
        tables[path] = [r for r in rows if r[ledger["id_field"]] not in superseded]
    historical_scope = dict(scope,
        statement_review_snapshot=checkpoint["statement_review_snapshot"],
        residual_snapshot=checkpoint["residual_snapshot"],
        next_semantic_cursor=checkpoint["next_semantic_cursor"])
    return historical_scope, tables, lambda path: historical_raw[path] if path in historical_raw else raw_loader(path)


def verify(checkpoint, scope, tables, discovery, target_loader, tag_map, raw_loader):
    """Fail closed on metadata damage, then independently verify actual objects.

    The complete canonical seal is intentionally independent of mutable fixture
    hashes. Explicit semantic expectations document what was mathematically
    reviewed. Neither a true flag nor a matching checksum proves mathematics.
    """
    if (not all(isinstance(x, dict) for x in (checkpoint, scope, tables, discovery, tag_map))
            or not callable(target_loader) or not callable(raw_loader)):
        return ["I7.3.7 inputs must be objects and byte loaders callable"]
    try:
        if digest(canonical(checkpoint)) != CONTRACT_SHA256:
            return ["I7.3.7 reviewed semantic/source/target/ledger contract changed"]
    except (TypeError, ValueError, OverflowError):
        return ["I7.3.7 checkpoint must contain exact serializable JSON metadata"]
    errors = []
    if canonical(checkpoint["semantic_contract"]) != canonical(SEMANTICS):
        errors.append("I7.3.7 dense-open sheaf hypotheses and adverse examples changed")
    if (checkpoint["source_units"] != UNITS or checkpoint["source_proof_units"] != PROOFS
            or checkpoint["owned_unnumbered_parts"] != {}
            or checkpoint["next_semantic_cursor"] != "ega:I.7.3.8"
            or checkpoint["next_cursor_starts_with_numbered_environment"] is not True
            or checkpoint["starting_content_commit"] != BASE
            or checkpoint["stacks_upstream"] != UPSTREAM):
        errors.append("I7.3.7 exact source order parent ownership or base changed")
    reviewed = scope.get("reviewed_source_slices")
    if not isinstance(reviewed, dict):
        errors.append("I7.3.7 scope reviewed_source_slices must be an object")
    else:
        for unit, expected in checkpoint["french_authority"]["source_scopes"].items():
            if reviewed.get(unit) != expected:
                errors.append("I7.3.7 scope source ownership changed: " + unit)
    for key in ("statement_review_snapshot", "residual_snapshot"):
        if scope.get(key) != checkpoint[key]:
            errors.append("I7.3.7 live coverage snapshot changed: " + key)

    def read(loader, *args):
        try:
            raw = loader(*args)
            if not isinstance(raw, bytes):
                raise ValueError("expected raw bytes")
            return raw
        except (OSError, ValueError, TypeError, KeyError):
            errors.append("I7.3.7 byte object unavailable: " + str(args))
            return b""

    # Replay all eighteen paired statement/proof blocks.
    # Official and integrated evidence retain distinct identities.
    cache = {}
    for target in checkpoint["targets"]:
        if tag_map.get(target["label"]) != target["tag"]:
            errors.append("I7.3.7 exact tag-label-file join changed: " + target["tag"])
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
                errors.append("I7.3.7 exact " + edition + " target bytes changed: " + target["tag"])

    if scope.get("next_semantic_cursor") != "ega:I.7.3.8":
        errors.append("I7.3.7 live semantic cursor changed")
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
                errors.append("I7.3.7 actual target context changed: " + context["name"])
    from tools.check_ega_i737_source_boundaries import validate_artifact
    for language in ("fr", "en"):
        errors.extend(validate_artifact(checkpoint["languages"][language], language))

    unit_set = set(UNITS + PROOFS)
    for ledger in checkpoint["ledgers"]:
        path, key = ledger["path"], ledger["id_field"]
        rows = tables.get(path)
        if (not isinstance(rows, list) or any(not isinstance(r, dict)
                or any(not isinstance(k, str) or (v is not None and not isinstance(v, str))
                       for k, v in r.items()) for r in rows)):
            errors.append("I7.3.7 actual ledger must contain exact CSV text rows: " + path)
            continue
        ids = {r[key] for r in ledger["rows"]}
        if [r for r in rows if r.get(key) in ids] != ledger["rows"]:
            errors.append("I7.3.7 exact reviewed ledger rows changed: " + path)
        if path != "ega/agent.csv":
            source_key = "subject_id" if path == "ega/dec.csv" else "source_unit"
            if [r for r in rows if r.get(source_key) in unit_set] != ledger["rows"]:
                errors.append("I7.3.7 source-unit ledger closure changed: " + path)
        raw = read(raw_loader, path)
        if b"\r" in raw or not raw.endswith(b"\n"):
            errors.append("I7.3.7 ledger must have exact LF serialization: " + path)
        lines = [line + b"\n" for line in raw.split(b"\n")[:-1]]
        prefix = b"".join(lines[:ledger["prefix_rows"] + 1])
        append = b"".join(lines[ledger["prefix_rows"] + 1:ledger["final_rows"] + 1])
        for block, size, seal, part in ((prefix, ledger["prefix_bytes"], ledger["prefix_sha256"], "prior prefix"),
                (append, ledger["append_bytes"], ledger["append_sha256"], "reviewed append"),
                (raw, ledger["bytes"], ledger["sha256"], "current postimage")):
            if len(block) != size or digest(block) != seal:
                errors.append("I7.3.7 " + part + " changed: " + path)
        # Verify supplied runtime rows are the active view of the actual bytes.
        parsed = list(csv.DictReader(io.StringIO(raw.decode("utf-8", errors="replace"), newline="")))
        superseded = {r.get("supersedes") for r in parsed if r.get("supersedes")}
        active = [r for r in parsed if r.get(key) not in superseded]
        if rows != active:
            errors.append("I7.3.7 supplied table disagrees with actual active byte view: " + path)

    actual_gaps = [r for r in tables.get("ega/resid.csv", []) if isinstance(r, dict) and r.get("status") == "open_gap"] if isinstance(tables.get("ega/resid.csv"), list) else []
    if actual_gaps != checkpoint["preserved_open_gap_rows"] or len(actual_gaps) != 12:
        errors.append("I7.3.7 prior twelve open gaps changed or were falsely closed")
    expected_units = checkpoint["english_discovery"]["stable_units"]
    if len(expected_units) != 6 or {r["unit_id"] for r in expected_units} != unit_set:
        errors.append("I7.3.7 exact six discovery units changed")
    for row in expected_units:
        if discovery.get(row["unit_id"]) != row:
            errors.append("I7.3.7 discovery changed or promoted: " + row["unit_id"])
    # Supplied discovery dictionaries must be the exact live CSV view, not
    # six correct rows accompanied by an invented738unit or earlier tail unit.
    discovery_raw = read(raw_loader, "ega/units.csv")
    discovery_rows = list(csv.DictReader(io.StringIO(
        discovery_raw.decode("utf-8", errors="replace"), newline="")))
    parsed_discovery = {r.get("unit_id"): r for r in discovery_rows}
    if discovery != parsed_discovery or len(parsed_discovery) != len(discovery_rows):
        errors.append("I7.3.7 supplied discovery disagrees with exact live CSV inventory")
    for item in checkpoint["preserved_inputs"] + checkpoint["reviewed_artifacts"]:
        raw = read(raw_loader, item["path"])
        if len(raw) != item["bytes"] or digest(raw) != item["sha256"]:
            errors.append("I7.3.7 preserved input changed: " + item["path"])
    errors.extend(dossier_errors(read(raw_loader, DOSSIER["path"]), checkpoint["derivation_dossier"]))
    return errors
