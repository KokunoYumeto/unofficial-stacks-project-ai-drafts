#!/usr/bin/env python3
"""Verify every changed file of an immutable public GitHub commit.

The verifier is deliberately narrow and fail-closed:

* the base and head are full, locally present commit IDs and the base must be
  an ancestor of the head;
* the changed-path inventory comes only from a bounded
  ``git diff --name-status --no-renames BASE..HEAD``;
* only added or modified ordinary Git blobs are accepted (no deletions,
  renames, type changes, symlinks, or submodules);
* the anonymous GitHub API commit/tree identities must equal local Git; and
* every changed file is downloaded from ``raw.githubusercontent.com`` at the
  immutable head commit and matched by bytes, SHA-256, and Git blob ID.

No authentication material is read, accepted, transmitted, or written.  The
optional receipt contains public URLs and repository-relative paths only.  A
``--check-receipt`` path additionally requires a changed JSON receipt to be a
sanitized, passing object and records its schema without trusting its claims.
"""

from __future__ import annotations

import argparse
import hashlib
import http.client
import json
import math
import os
import re
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import Any, Mapping, Sequence


SCHEMA = "unofficial-ai-integrated-stacks-github-commit-readback/v1"
USER_AGENT = "unofficial-ai-stacks-commit-readback/1"
HEX40_RE = re.compile(r"[0-9a-fA-F]{40}")
HEX64_RE = re.compile(r"[0-9a-fA-F]{64}")
REPOSITORY_RE = re.compile(
    r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,38})/"
    r"[A-Za-z0-9](?:[A-Za-z0-9._-]{0,99})"
)
MAX_HTTP_ATTEMPTS = 2
MAX_API_BYTES = 4 * 1024 * 1024
MAX_RECEIPT_BYTES = 8 * 1024 * 1024
MAX_GIT_STDERR_BYTES = 1024 * 1024
MAX_GIT_PATH_BYTES = 4096
DOWNLOAD_CHUNK_BYTES = 1024 * 1024
DEFAULT_MAX_PATHS = 512
DEFAULT_MAX_FILE_BYTES = 128 * 1024 * 1024
DEFAULT_MAX_TOTAL_BYTES = 256 * 1024 * 1024
MAX_CONFIGURED_BYTES = 2 * 1024 * 1024 * 1024


class VerificationError(RuntimeError):
    """A required public or local invariant did not hold."""


class TransientNetworkError(RuntimeError):
    """A public request had a transport-level, potentially transient failure."""


def require(condition: Any, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def exact_commit(value: str, label: str) -> str:
    require(HEX40_RE.fullmatch(value) is not None, f"{label} must be a full commit ID")
    return value.lower()


def safe_repository(value: str) -> str:
    require(REPOSITORY_RE.fullmatch(value) is not None, "invalid GitHub owner/repository")
    owner, name = value.split("/", 1)
    require(not name.endswith(".git"), "repository must not use a .git suffix")
    return f"{owner}/{name}"


def safe_git_path(value: str) -> str:
    require(isinstance(value, str) and value != "", "empty Git path")
    require(len(value.encode("utf-8")) <= MAX_GIT_PATH_BYTES, "Git path is too long")
    pure = PurePosixPath(value)
    require(
        "\\" not in value
        and "\x00" not in value
        and "\r" not in value
        and "\n" not in value
        and "\t" not in value
        and not pure.is_absolute()
        and all(part not in {"", ".", ".."} for part in pure.parts)
        and (not pure.parts or re.match(r"^[A-Za-z]:", pure.parts[0]) is None)
        and pure.as_posix() == value,
        "unsafe repository-relative Git path",
    )
    return value


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest().upper()


def strict_json_object(raw: bytes, label: str) -> Mapping[str, Any]:
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as error:
        raise VerificationError(f"{label} is not UTF-8 JSON") from error

    def reject_constant(value: str) -> Any:
        raise VerificationError(f"{label} contains a non-finite JSON number: {value}")

    def finite_float(value: str) -> float:
        parsed = float(value)
        require(math.isfinite(parsed), f"{label} contains an overflowing JSON number")
        return parsed

    def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise VerificationError(f"{label} contains a duplicate JSON key")
            result[key] = value
        return result

    try:
        value = json.loads(
            text,
            object_pairs_hook=unique_object,
            parse_constant=reject_constant,
            parse_float=finite_float,
        )
    except (json.JSONDecodeError, ValueError) as error:
        raise VerificationError(f"{label} is malformed JSON") from error
    require(isinstance(value, Mapping), f"{label} JSON must be an object")
    return value


def git_blob_sha1(value: bytes) -> str:
    try:
        hasher = hashlib.sha1(usedforsecurity=False)
    except TypeError:  # pragma: no cover - older Python builds
        hasher = hashlib.sha1()
    hasher.update(f"blob {len(value)}\0".encode("ascii"))
    hasher.update(value)
    return hasher.hexdigest().lower()


def validate_public_url(url: str) -> None:
    try:
        parsed = urllib.parse.urlsplit(url)
        port = parsed.port
    except ValueError as error:
        raise VerificationError("malformed public GitHub URL") from error
    require(
        parsed.scheme == "https"
        and parsed.hostname is not None
        and parsed.username is None
        and parsed.password is None
        and port in (None, 443)
        and parsed.query == ""
        and parsed.fragment == "",
        "refusing a non-public or credential-bearing URL",
    )
    host = parsed.hostname.casefold()
    require(
        host in {
            "api.github.com",
            "github.com",
            "raw.githubusercontent.com",
            "objects.githubusercontent.com",
        }
        or host.endswith(".githubusercontent.com"),
        "refusing a URL outside the GitHub trust boundary",
    )


class RejectRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(
        self,
        req: urllib.request.Request,
        fp: Any,
        code: int,
        msg: str,
        headers: Any,
        newurl: str,
    ) -> urllib.request.Request | None:
        validate_public_url(newurl)
        # The exact REST and immutable raw endpoints used here normally return
        # 200 directly.  Rejecting redirects makes every opener call exactly
        # one HTTP attempt and prevents aliases from weakening identity checks.
        return None


# An empty proxy map prevents accidental use of credential-bearing proxy
# environment variables.  urllib does not consult netrc for these requests.
PUBLIC_OPENER = urllib.request.build_opener(
    urllib.request.ProxyHandler({}), RejectRedirectHandler()
)


def open_public_once(url: str, accept: str, timeout_seconds: int) -> Any:
    validate_public_url(url)
    headers = {"Accept": accept, "User-Agent": USER_AGENT}
    req = urllib.request.Request(url, headers=headers, method="GET")
    try:
        response = PUBLIC_OPENER.open(req, timeout=timeout_seconds)
    except urllib.error.HTTPError:
        raise
    except (urllib.error.URLError, TimeoutError, OSError, http.client.HTTPException) as error:
        raise TransientNetworkError("anonymous GitHub request failed") from error
    try:
        validate_public_url(response.geturl())
    except BaseException:
        response.close()
        raise
    if response.status != 200:
        response.close()
        raise VerificationError("unexpected anonymous GitHub HTTP status")
    return response


def read_response_limited(response: Any, maximum: int) -> bytes:
    declared = response.headers.get("Content-Length")
    if declared is not None:
        try:
            declared_bytes = int(declared)
        except ValueError as error:
            raise VerificationError("malformed public Content-Length") from error
        require(0 <= declared_bytes <= maximum, "public response exceeds its byte bound")
    try:
        raw = response.read(maximum + 1)
    except (OSError, http.client.HTTPException) as error:
        raise TransientNetworkError("public response could not be read") from error
    require(len(raw) <= maximum, "public response exceeds its byte bound")
    if declared is not None:
        require(len(raw) == declared_bytes, "public Content-Length mismatch")
    return raw


def request_json(url: str, timeout_seconds: int) -> Mapping[str, Any]:
    last_error: BaseException | None = None
    for attempt in range(1, MAX_HTTP_ATTEMPTS + 1):
        try:
            with open_public_once(
                url, "application/vnd.github+json", timeout_seconds
            ) as response:
                raw = read_response_limited(response, MAX_API_BYTES)
            return strict_json_object(raw, "GitHub response")
        except urllib.error.HTTPError as error:
            last_error = error
            transient = error.code in {429, 500, 502, 503, 504}
            if not transient or attempt == MAX_HTTP_ATTEMPTS:
                raise VerificationError(
                    f"anonymous GitHub request returned HTTP {error.code}"
                ) from error
        except TransientNetworkError as error:
            last_error = error
            if attempt == MAX_HTTP_ATTEMPTS:
                raise VerificationError("anonymous GitHub JSON read failed") from error
        if attempt < MAX_HTTP_ATTEMPTS:
            time.sleep(0.25)
    raise VerificationError("anonymous GitHub JSON read failed") from last_error


def run_git(
    repo_root: Path,
    arguments: Sequence[str],
    *,
    timeout_seconds: int,
    max_stdout_bytes: int,
    label: str,
    accepted_returncodes: frozenset[int] = frozenset({0}),
) -> tuple[int, bytes]:
    require(max_stdout_bytes >= 0, "invalid Git output bound")
    try:
        process = subprocess.Popen(
            ["git", "-C", os.fspath(repo_root), *arguments],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except OSError as error:
        raise VerificationError(f"could not start Git operation: {label}") from error

    buffers = {"stdout": bytearray(), "stderr": bytearray()}
    overrun: list[str] = []

    def reader(name: str, stream: Any, maximum: int) -> None:
        while True:
            chunk = stream.read(64 * 1024)
            if not chunk:
                return
            if len(buffers[name]) + len(chunk) > maximum:
                allowed = max(0, maximum - len(buffers[name]))
                buffers[name].extend(chunk[:allowed])
                overrun.append(name)
                try:
                    process.kill()
                except OSError:
                    pass
                return
            buffers[name].extend(chunk)

    assert process.stdout is not None and process.stderr is not None
    stdout_reader = threading.Thread(
        target=reader,
        args=("stdout", process.stdout, max_stdout_bytes),
        daemon=True,
    )
    stderr_reader = threading.Thread(
        target=reader,
        args=("stderr", process.stderr, MAX_GIT_STDERR_BYTES),
        daemon=True,
    )
    stdout_reader.start()
    stderr_reader.start()
    try:
        returncode = process.wait(timeout=timeout_seconds)
    except subprocess.TimeoutExpired as error:
        process.kill()
        process.wait()
        stdout_reader.join(timeout=5)
        stderr_reader.join(timeout=5)
        raise VerificationError(f"bounded Git operation timed out: {label}") from error
    stdout_reader.join(timeout=5)
    stderr_reader.join(timeout=5)
    require(not stdout_reader.is_alive() and not stderr_reader.is_alive(), "Git pipe reader did not terminate")
    if overrun:
        raise VerificationError(f"Git {overrun[0]} exceeded its bound: {label}")
    stdout = bytes(buffers["stdout"])
    stderr = bytes(buffers["stderr"])
    require(
        len(stdout) <= max_stdout_bytes,
        f"Git output exceeded its bound: {label}",
    )
    require(
        len(stderr) <= MAX_GIT_STDERR_BYTES,
        f"Git diagnostic output exceeded its bound: {label}",
    )
    require(
        returncode in accepted_returncodes,
        f"Git operation failed: {label}",
    )
    return returncode, stdout


def local_commit(
    repo_root: Path, commit_id: str, timeout_seconds: int
) -> tuple[str, str]:
    _, commit_raw = run_git(
        repo_root,
        ["rev-parse", "--verify", f"{commit_id}^{{commit}}"],
        timeout_seconds=timeout_seconds,
        max_stdout_bytes=128,
        label="resolve commit",
    )
    resolved = commit_raw.decode("ascii", "strict").strip().lower()
    require(resolved == commit_id, "local commit identity mismatch")
    _, tree_raw = run_git(
        repo_root,
        ["rev-parse", "--verify", f"{commit_id}^{{tree}}"],
        timeout_seconds=timeout_seconds,
        max_stdout_bytes=128,
        label="resolve commit tree",
    )
    tree = tree_raw.decode("ascii", "strict").strip().lower()
    require(HEX40_RE.fullmatch(tree) is not None, "local tree identity is malformed")
    return resolved, tree


def require_ancestor(repo_root: Path, base: str, head: str, timeout_seconds: int) -> None:
    result, _ = run_git(
        repo_root,
        ["merge-base", "--is-ancestor", base, head],
        timeout_seconds=timeout_seconds,
        max_stdout_bytes=0,
        label="verify base ancestry",
        accepted_returncodes=frozenset({0, 1}),
    )
    require(result == 0, "base commit is not an ancestor of head commit")


@dataclass(frozen=True)
class LocalLeaf:
    path: str
    status: str
    mode: str
    git_blob: str
    bytes: int
    sha256: str
    receipt_payload: bytes | None = None


def changed_path_rows(
    repo_root: Path,
    base: str,
    head: str,
    timeout_seconds: int,
    max_paths: int,
) -> list[tuple[str, str]]:
    maximum = (max_paths + 1) * (MAX_GIT_PATH_BYTES + 8)
    _, raw = run_git(
        repo_root,
        ["diff", "--name-status", "--no-renames", "-z", f"{base}..{head}", "--"],
        timeout_seconds=timeout_seconds,
        max_stdout_bytes=maximum,
        label="enumerate changed paths",
    )
    require(raw.endswith(b"\0"), "Git changed-path output is not NUL terminated")
    fields = raw[:-1].split(b"\0") if raw else []
    require(len(fields) % 2 == 0, "Git changed-path output is malformed")
    require(bool(fields), "base-to-head comparison has no changed paths")
    require(len(fields) // 2 <= max_paths, "changed-path count exceeds its bound")
    rows: list[tuple[str, str]] = []
    seen: set[str] = set()
    for offset in range(0, len(fields), 2):
        try:
            status = fields[offset].decode("ascii", "strict")
            path = fields[offset + 1].decode("utf-8", "strict")
        except UnicodeDecodeError as error:
            raise VerificationError("changed-path inventory is not safely decodable") from error
        path = safe_git_path(path)
        require(status in {"A", "M"}, f"unsupported changed-path status: {status}")
        require(path not in seen, "duplicate changed path")
        seen.add(path)
        rows.append((status, path))
    return sorted(rows, key=lambda row: row[1])


def ls_tree_leaf(
    repo_root: Path, head: str, path: str, timeout_seconds: int
) -> tuple[str, str]:
    _, raw = run_git(
        repo_root,
        ["ls-tree", "-z", "--full-tree", head, "--", path],
        timeout_seconds=timeout_seconds,
        max_stdout_bytes=MAX_GIT_PATH_BYTES + 256,
        label="resolve changed leaf",
    )
    require(raw.endswith(b"\0") and raw.count(b"\0") == 1, "changed path is not one Git leaf")
    record = raw[:-1]
    require(b"\t" in record, "Git leaf record is malformed")
    metadata, raw_path = record.split(b"\t", 1)
    try:
        returned_path = raw_path.decode("utf-8", "strict")
        mode, kind, object_id = metadata.decode("ascii", "strict").split(" ")
    except (UnicodeDecodeError, ValueError) as error:
        raise VerificationError("Git leaf record is malformed") from error
    require(returned_path == path, "Git leaf path identity mismatch")
    require(kind == "blob", "changed Git submodules are unsupported")
    require(mode in {"100644", "100755"}, "changed Git symlinks or special modes are unsupported")
    require(HEX40_RE.fullmatch(object_id) is not None, "Git blob identity is malformed")
    return mode, object_id.lower()


def local_leaf(
    repo_root: Path,
    head: str,
    status: str,
    path: str,
    timeout_seconds: int,
    max_file_bytes: int,
    capture_receipt: bool,
) -> LocalLeaf:
    mode, blob = ls_tree_leaf(repo_root, head, path, timeout_seconds)
    _, size_raw = run_git(
        repo_root,
        ["cat-file", "-s", blob],
        timeout_seconds=timeout_seconds,
        max_stdout_bytes=64,
        label="read changed blob size",
    )
    try:
        size = int(size_raw.decode("ascii", "strict").strip())
    except (UnicodeDecodeError, ValueError) as error:
        raise VerificationError("changed Git blob size is malformed") from error
    require(0 <= size <= max_file_bytes, "changed Git blob exceeds its per-file bound")
    if capture_receipt:
        require(size <= MAX_RECEIPT_BYTES, "checked receipt exceeds its JSON byte bound")
    _, payload = run_git(
        repo_root,
        ["cat-file", "blob", blob],
        timeout_seconds=timeout_seconds,
        max_stdout_bytes=size,
        label="read changed blob",
    )
    require(len(payload) == size, "local Git blob byte count mismatch")
    require(git_blob_sha1(payload) == blob, "local Git blob object identity mismatch")
    return LocalLeaf(
        path=path,
        status={"A": "added", "M": "modified"}[status],
        mode=mode,
        git_blob=blob,
        bytes=size,
        sha256=sha256_bytes(payload),
        receipt_payload=payload if capture_receipt else None,
    )


def local_changes(
    repo_root: Path,
    base: str,
    head: str,
    *,
    timeout_seconds: int,
    max_paths: int,
    max_file_bytes: int,
    max_total_bytes: int,
    check_receipt: str | None,
) -> list[LocalLeaf]:
    inventory = changed_path_rows(repo_root, base, head, timeout_seconds, max_paths)
    paths = {path for _, path in inventory}
    if check_receipt is not None:
        require(check_receipt in paths, "checked receipt is not a changed path")
    leaves: list[LocalLeaf] = []
    total = 0
    for status, path in inventory:
        leaf = local_leaf(
            repo_root,
            head,
            status,
            path,
            timeout_seconds,
            max_file_bytes,
            path == check_receipt,
        )
        total += leaf.bytes
        require(total <= max_total_bytes, "changed Git blobs exceed their aggregate byte bound")
        leaves.append(leaf)
    return leaves


def repository_api_url(repository: str) -> str:
    return f"https://api.github.com/repos/{repository}"


def commit_api_url(repository: str, commit_id: str) -> str:
    # The Git Database endpoint omits the potentially large changed-file and
    # patch inventory returned by /commits/{sha}; only commit/tree identity is
    # needed here, so its response stays predictably within MAX_API_BYTES.
    return f"{repository_api_url(repository)}/git/commits/{commit_id}"


def commit_html_url(repository: str, commit_id: str) -> str:
    return f"https://github.com/{repository}/commit/{commit_id}"


def raw_url(repository: str, commit_id: str, path: str) -> str:
    encoded_path = "/".join(urllib.parse.quote(part, safe="") for part in path.split("/"))
    url = f"https://raw.githubusercontent.com/{repository}/{commit_id}/{encoded_path}"
    validate_public_url(url)
    return url


def verify_repository_public(repository: str, timeout_seconds: int) -> dict[str, Any]:
    url = repository_api_url(repository)
    value = request_json(url, timeout_seconds)
    require(value.get("private") is False, "GitHub repository is not public")
    require(
        str(value.get("full_name", "")).casefold() == repository.casefold(),
        "GitHub repository identity mismatch",
    )
    visibility = value.get("visibility")
    require(visibility in (None, "public"), "GitHub repository visibility is not public")
    return {
        "owner_repo": repository,
        "public": True,
        "html_url": f"https://github.com/{repository}",
        "api_url": url,
    }


def verify_public_commit(
    repository: str,
    commit_id: str,
    local_tree: str,
    timeout_seconds: int,
) -> dict[str, Any]:
    url = commit_api_url(repository, commit_id)
    value = request_json(url, timeout_seconds)
    require(str(value.get("sha", "")).lower() == commit_id, "GitHub commit identity mismatch")
    tree = value.get("tree")
    require(isinstance(tree, Mapping), "GitHub commit tree link is malformed")
    public_tree = str(tree.get("sha", "")).lower()
    require(HEX40_RE.fullmatch(public_tree) is not None, "GitHub commit tree is malformed")
    require(public_tree == local_tree, "GitHub/local commit tree identity mismatch")
    return {
        "commit": commit_id,
        "tree": public_tree,
        "html_url": commit_html_url(repository, commit_id),
        "api_url": url,
        "api_identity_check": "PASS",
    }


def read_raw_leaf(
    repository: str,
    head: str,
    leaf: LocalLeaf,
    timeout_seconds: int,
    capture_payload: bool,
) -> tuple[dict[str, Any], bytes | None]:
    url = raw_url(repository, head, leaf.path)
    last_error: BaseException | None = None
    for attempt in range(1, MAX_HTTP_ATTEMPTS + 1):
        try:
            with open_public_once(url, "application/octet-stream", timeout_seconds) as response:
                declared = response.headers.get("Content-Length")
                if declared is not None:
                    try:
                        declared_bytes = int(declared)
                    except ValueError as error:
                        raise VerificationError("raw Content-Length is malformed") from error
                    require(declared_bytes == leaf.bytes, f"raw byte count mismatch: {leaf.path}")
                sha256 = hashlib.sha256()
                try:
                    git_sha1 = hashlib.sha1(usedforsecurity=False)
                except TypeError:  # pragma: no cover - older Python builds
                    git_sha1 = hashlib.sha1()
                git_sha1.update(f"blob {leaf.bytes}\0".encode("ascii"))
                total = 0
                captured = bytearray() if capture_payload else None
                while True:
                    chunk = response.read(DOWNLOAD_CHUNK_BYTES)
                    if not chunk:
                        break
                    total += len(chunk)
                    require(total <= leaf.bytes, f"raw response is oversized: {leaf.path}")
                    sha256.update(chunk)
                    git_sha1.update(chunk)
                    if captured is not None:
                        captured.extend(chunk)
                require(total == leaf.bytes, f"raw byte count mismatch: {leaf.path}")
                public_sha256 = sha256.hexdigest().upper()
                public_blob = git_sha1.hexdigest().lower()
                require(public_sha256 == leaf.sha256, f"raw SHA-256 mismatch: {leaf.path}")
                require(public_blob == leaf.git_blob, f"raw Git blob mismatch: {leaf.path}")
                payload = bytes(captured) if captured is not None else None
                return (
                    {
                        "path": leaf.path,
                        "status": leaf.status,
                        "mode": leaf.mode,
                        "bytes": total,
                        "sha256": public_sha256,
                        "git_blob": public_blob,
                        "raw_url": url,
                        "identity_check": "PASS",
                    },
                    payload,
                )
        except VerificationError:
            raise
        except urllib.error.HTTPError as error:
            last_error = error
            transient = error.code in {429, 500, 502, 503, 504}
            if not transient or attempt == MAX_HTTP_ATTEMPTS:
                raise VerificationError(
                    f"raw GitHub request returned HTTP {error.code}: {leaf.path}"
                ) from error
        except (TransientNetworkError, TimeoutError, OSError, http.client.HTTPException) as error:
            last_error = error
            if attempt == MAX_HTTP_ATTEMPTS:
                raise VerificationError(f"raw GitHub read failed: {leaf.path}") from error
        if attempt < MAX_HTTP_ATTEMPTS:
            time.sleep(0.25)
    raise VerificationError(f"raw GitHub read failed: {leaf.path}") from last_error


LOCAL_PATH_RE = re.compile(
    r"(?i)(?:(?<![A-Za-z0-9])[A-Za-z]:[\\/]"
    r"|(?:^|[\s\"'(\[])/(?!/)[A-Za-z0-9._~+-]+(?:/[^\s\"']*)?"
    r"|(?:^|[\s\"'(\[])\\\\[^\\\s]+\\[^\\\s]+)"
)
SECRET_SHAPE_RE = re.compile(
    r"(?i)(?:authorization\s*[:=]|bearer\s+[A-Za-z0-9._~+/-]+"
    r"|access[_ -]?token|api[_ -]?key|client[_ -]?secret|password\s*[:=]"
    r"|github_pat_[A-Za-z0-9_]+|gh[pousr]_[A-Za-z0-9]+)"
)


def sanitized(value: Any) -> None:
    try:
        serialized = json.dumps(
            value, ensure_ascii=False, sort_keys=True, allow_nan=False
        )
    except (TypeError, ValueError) as error:
        raise VerificationError("JSON is not finite and serializable") from error
    require(LOCAL_PATH_RE.search(serialized) is None, "JSON contains a local absolute path")
    require(SECRET_SHAPE_RE.search(serialized) is None, "JSON contains secret-shaped material")

    def visit(item: Any) -> None:
        if isinstance(item, Mapping):
            for key, child in item.items():
                require(isinstance(key, str), "JSON object key is not a string")
                visit(key)
                visit(child)
        elif isinstance(item, list):
            for child in item:
                visit(child)
        elif isinstance(item, str):
            if item.startswith("https://"):
                validate_public_url(item)
                return
            lowered = item.casefold()
            require(not lowered.startswith("file:"), "JSON contains a file URL")
            require(
                not item.startswith(("//", "\\\\")),
                "JSON contains a protocol-relative or UNC path",
            )
            require(
                re.match(r"^[A-Za-z][A-Za-z0-9+.-]*://", item) is None,
                "JSON contains a non-HTTPS URL",
            )
            windows = PureWindowsPath(item)
            require(
                not windows.is_absolute() and windows.drive == "" and windows.root == "",
                "JSON contains a Windows absolute or rooted path",
            )
            require(
                not PurePosixPath(item).is_absolute(),
                "JSON contains a POSIX absolute path",
            )
            require(LOCAL_PATH_RE.search(item) is None, "JSON string embeds a local absolute path")

    visit(value)


def check_embedded_receipt(
    path: str,
    local_payload: bytes | None,
    public_payload: bytes | None,
    identity: Mapping[str, Any],
) -> dict[str, Any]:
    require(local_payload is not None and public_payload is not None, "checked receipt bytes missing")
    require(local_payload == public_payload, "checked receipt public bytes differ from local Git")
    value = strict_json_object(public_payload, "checked receipt")
    sanitized(value)
    schema = value.get("schema")
    require(isinstance(schema, str) and schema != "", "checked receipt lacks a schema")
    require(value.get("status") == "PASS", "checked receipt status is not PASS")
    return {
        "path": path,
        "bytes": identity["bytes"],
        "sha256": identity["sha256"],
        "git_blob": identity["git_blob"],
        "schema": schema,
        "declared_status": "PASS",
        "public_byte_identity_check": "PASS",
        "sanitization_check": "PASS",
        "claim_trust_boundary": "schema and PASS status observed; substantive claims not re-used",
    }


def write_json_atomic(path: Path, value: Mapping[str, Any]) -> None:
    sanitized(value)
    require(not path.is_symlink(), "output receipt path must not be a symlink")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    require(not temporary.is_symlink(), "temporary receipt path must not be a symlink")
    with temporary.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(
            value,
            handle,
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
            allow_nan=False,
        )
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temporary, path)


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Anonymously verify all ordinary changed file bytes at one immutable "
            "public GitHub commit against a bounded local Git comparison."
        )
    )
    parser.add_argument("--repo-root", required=True, type=Path, help="local Git repository root")
    parser.add_argument("--repository", required=True, help="public GitHub owner/repository")
    parser.add_argument("--commit", required=True, help="immutable full head commit ID")
    parser.add_argument("--base-commit", required=True, help="immutable full base commit ID")
    parser.add_argument("--output", type=Path, help="optional sanitized JSON receipt")
    parser.add_argument(
        "--check-receipt",
        metavar="REPO_PATH",
        help="also validate this changed JSON receipt's public bytes and sanitization",
    )
    parser.add_argument("--timeout-seconds", type=int, default=30)
    parser.add_argument("--max-paths", type=int, default=DEFAULT_MAX_PATHS)
    parser.add_argument("--max-file-bytes", type=int, default=DEFAULT_MAX_FILE_BYTES)
    parser.add_argument("--max-total-bytes", type=int, default=DEFAULT_MAX_TOTAL_BYTES)
    args = parser.parse_args(argv)
    try:
        args.repository = safe_repository(args.repository)
        args.commit = exact_commit(args.commit, "commit")
        args.base_commit = exact_commit(args.base_commit, "base-commit")
        require(args.commit != args.base_commit, "base and head commits are identical")
        require(1 <= args.timeout_seconds <= 120, "timeout-seconds must be between 1 and 120")
        require(1 <= args.max_paths <= 4096, "max-paths must be between 1 and 4096")
        require(
            1 <= args.max_file_bytes <= MAX_CONFIGURED_BYTES,
            "max-file-bytes is outside its permitted range",
        )
        require(
            1 <= args.max_total_bytes <= MAX_CONFIGURED_BYTES,
            "max-total-bytes is outside its permitted range",
        )
        require(
            args.max_file_bytes <= args.max_total_bytes,
            "max-file-bytes exceeds max-total-bytes",
        )
        if args.check_receipt is not None:
            args.check_receipt = safe_git_path(args.check_receipt)
            require(
                args.check_receipt.casefold().endswith(".json"),
                "check-receipt must name a JSON file",
            )
    except VerificationError as error:
        parser.error(str(error))
    return args


def run(args: argparse.Namespace) -> dict[str, Any]:
    require(
        args.repo_root.is_dir() and not args.repo_root.is_symlink(),
        "repo-root is not an ordinary directory",
    )
    repo_root = args.repo_root.resolve(strict=True)
    _, probe = run_git(
        repo_root,
        ["rev-parse", "--show-toplevel"],
        timeout_seconds=args.timeout_seconds,
        max_stdout_bytes=MAX_GIT_PATH_BYTES,
        label="verify repository root",
    )
    try:
        actual_root = Path(probe.decode(sys.getfilesystemencoding(), "strict").strip()).resolve(strict=True)
    except (UnicodeDecodeError, OSError) as error:
        raise VerificationError("Git repository root could not be resolved") from error
    require(actual_root == repo_root, "repo-root must be the exact Git top level")

    base, base_tree = local_commit(repo_root, args.base_commit, args.timeout_seconds)
    head, head_tree = local_commit(repo_root, args.commit, args.timeout_seconds)
    require_ancestor(repo_root, base, head, args.timeout_seconds)
    leaves = local_changes(
        repo_root,
        base,
        head,
        timeout_seconds=args.timeout_seconds,
        max_paths=args.max_paths,
        max_file_bytes=args.max_file_bytes,
        max_total_bytes=args.max_total_bytes,
        check_receipt=args.check_receipt,
    )

    repository = verify_repository_public(args.repository, args.timeout_seconds)
    public_base = verify_public_commit(
        args.repository, base, base_tree, args.timeout_seconds
    )
    public_head = verify_public_commit(
        args.repository, head, head_tree, args.timeout_seconds
    )

    changed_paths: list[dict[str, Any]] = []
    public_receipt_payload: bytes | None = None
    checked_identity: Mapping[str, Any] | None = None
    checked_local_payload: bytes | None = None
    for leaf in leaves:
        identity, payload = read_raw_leaf(
            args.repository,
            head,
            leaf,
            args.timeout_seconds,
            leaf.path == args.check_receipt,
        )
        changed_paths.append(identity)
        if leaf.path == args.check_receipt:
            public_receipt_payload = payload
            checked_identity = identity
            checked_local_payload = leaf.receipt_payload

    embedded = None
    if args.check_receipt is not None:
        require(checked_identity is not None, "checked receipt identity was not observed")
        embedded = check_embedded_receipt(
            args.check_receipt,
            checked_local_payload,
            public_receipt_payload,
            checked_identity,
        )

    tuple_rows = [
        {
            key: row[key]
            for key in ("path", "status", "mode", "bytes", "sha256", "git_blob")
        }
        for row in changed_paths
    ]
    receipt: dict[str, Any] = {
        "schema": SCHEMA,
        "status": "PASS",
        "method": (
            "anonymous HTTPS; GitHub API commit/tree equality; bounded local no-rename "
            "changed-path inventory; raw immutable-commit byte, SHA-256, and Git-blob equality"
        ),
        "repository": repository,
        "comparison": {
            "base": public_base,
            "head": public_head,
            "base_is_ancestor": True,
            "diff_command_contract": "git diff --name-status --no-renames BASE..HEAD --",
        },
        "limits": {
            "http_attempts_per_transaction": MAX_HTTP_ATTEMPTS,
            "timeout_seconds": args.timeout_seconds,
            "max_changed_paths": args.max_paths,
            "max_file_bytes": args.max_file_bytes,
            "max_total_bytes": args.max_total_bytes,
        },
        "changed_path_count": len(changed_paths),
        "changed_file_bytes": sum(row["bytes"] for row in changed_paths),
        "changed_paths": changed_paths,
        "changed_path_identity_tuple_set_sha256": sha256_bytes(canonical_json_bytes(tuple_rows)),
        "checked_receipt": embedded,
        "checks": {
            "repository_public": True,
            "base_api_commit_and_tree_equal_local_git": True,
            "head_api_commit_and_tree_equal_local_git": True,
            "base_is_ancestor_of_head": True,
            "changed_inventory_nonempty_and_bounded": True,
            "no_deletions_renames_type_changes_symlinks_or_submodules": True,
            "all_changed_files_raw_read_back": True,
            "all_byte_counts_match": True,
            "all_sha256_match": True,
            "all_git_blob_ids_match": True,
            "checked_receipt_pass": embedded is None or embedded["sanitization_check"] == "PASS",
        },
    }
    sanitized(receipt)
    receipt["receipt_content_sha256"] = sha256_bytes(canonical_json_bytes(receipt))
    sanitized(receipt)
    return receipt


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        receipt = run(args)
        if args.output is not None:
            write_json_atomic(args.output, receipt)
            print(
                json.dumps(
                    {
                        "status": "PASS",
                        "changed_paths": receipt["changed_path_count"],
                        "changed_file_bytes": receipt["changed_file_bytes"],
                        "receipt_content_sha256": receipt["receipt_content_sha256"],
                    },
                    sort_keys=True,
                    allow_nan=False,
                )
            )
        else:
            json.dump(
                receipt,
                sys.stdout,
                ensure_ascii=False,
                sort_keys=True,
                indent=2,
                allow_nan=False,
            )
            sys.stdout.write("\n")
    except VerificationError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
