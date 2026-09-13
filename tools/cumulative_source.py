"""Git-bound complete native source inventory. Never inspects untracked paths.

Install in tools/ before binding the final build source commit. This module is
also the consumer's independently recomputed archive membership contract.
"""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import zipfile

SCHEMA = 'native-cumulative-source-inventory/v1'
POLICY = 'all-committed-native-inputs-plus-build-support'
NATIVE = {'.tex', '.sty', '.cls', '.def', '.cfg', '.clo', '.fd', '.bib', '.bst', '.ist'}
FIGURES = {'.png', '.jpg', '.jpeg', '.eps', '.svg'}
SUPPORT = ('tools/', 'scripts/', 'documentation/')
ROOT_SUPPORT = {'Makefile', 'README', 'README.md', 'COPYING', 'CONTRIBUTORS', 'PROVENANCE.md'}
REQUIRED_TOOLS = ('cumulative-master.json', 'cumulative_source.py', 'cumulative_reader.py',
                  'reconstruct_cumulative.py', 'CUMULATIVE-RECONSTRUCTION.md',
                  'build_fixed_point.py')
MASTER = 'current/tools/cumulative-master.json'
METADATA = 'SOURCE-INVENTORY.json'

def require(ok, message):
    if not ok:
        raise ValueError(message)

def identity(raw):
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest().upper()}

def canonical_json(value):
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True, allow_nan=False)+'\n').encode()

def parse_json(raw):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, 'duplicate JSON key: '+key)
            result[key] = value
        return result
    def constant(value):
        raise ValueError('non-finite JSON constant: '+value)
    return json.loads(raw, object_pairs_hook=pairs, parse_constant=constant)

def safe_path(value):
    require(type(value) is str and bool(value) and not value.startswith('/'), 'unsafe member path')
    for part in value.split('/'):
        require(part not in ('', '.', '..') and part[-1] not in (' ', '.')
                and not any(ord(c) < 32 or ord(c) == 127 or c in '<>:"\\|?*' for c in part),
                'unsafe Windows member path: '+repr(value))
        device = part.split('.')[0].rstrip(' .').upper()
        require(device not in {'CON','PRN','AUX','NUL','CLOCK$','CONIN$','CONOUT$'}
                and re.fullmatch(r'(?:COM|LPT)[1-9\u00b9\u00b2\u00b3]', device) is None,
                'reserved Windows device path: '+repr(value))
    return value

def validate_stems(stems):
    require(type(stems) in (list, tuple) and bool(stems), 'nonempty chapter stem list required')
    require(all(type(s) is str and re.fullmatch('[a-z][a-z0-9-]*',s) for s in stems), 'invalid chapter stem')
    require(len(stems) == len(set(stems)), 'duplicate chapter stem')
    return stems

def validate_master(master, stems=None):
    keys = {'schema','title','scope','native_format','assembly_script','reconstruction_script','pypdf_version','chapters'}
    require(type(master) is dict and set(master) == keys, 'invalid cumulative master fields')
    require(master['schema'] == 'cumulative-reader-master/v1', 'wrong cumulative master schema')
    require(master['assembly_script'] == 'tools/cumulative_reader.py'
            and master['reconstruction_script'] == 'tools/reconstruct_cumulative.py', 'unexpected master script')
    require(all(type(master[k]) is str and bool(master[k].strip()) and not any(ord(c)<32 for c in master[k])
                for k in keys-{'chapters'}), 'invalid master text field')
    require(re.fullmatch(r'[0-9]+\.[0-9]+\.[0-9]+',master['pypdf_version']), 'invalid master runtime version')
    rows = master['chapters']
    require(type(rows) is list and bool(rows) and all(type(r) is dict and set(r)=={'stem','title'} for r in rows),
            'invalid master chapter rows')
    validate_stems([r['stem'] for r in rows])
    stems = [r['stem'] for r in rows] if stems is None else validate_stems(stems)
    require([r['stem'] for r in rows] == list(stems), 'master chapter profile differs')
    require(all(type(r['title']) is str and bool(r['title'].strip()) and not any(ord(c)<32 for c in r['title']) for r in rows),
            'invalid chapter title')
    return master

def validate_inventory_shape(inventory):
    required = {'schema','source_commit','authority_commit','master_path','chapter_stems','members','closure'}
    require(type(inventory) is dict and required <= set(inventory)
            and set(inventory) <= required | {'scope','baseline_current_distinction'}, 'invalid source inventory fields')
    require(inventory['schema'] == SCHEMA, 'wrong source inventory schema')
    for key in ('source_commit','authority_commit'):
        require(type(inventory[key]) is str and re.fullmatch('[0-9a-f]{40}',inventory[key]), 'invalid Git commit identity')
    require(inventory['master_path'] == MASTER, 'unexpected cumulative master path')
    validate_stems(inventory['chapter_stems'])
    require(inventory['closure'] == {'policy':POLICY,'checked':True}
            and type(inventory['closure'].get('checked')) is bool, 'invalid source closure declaration')
    rows = inventory['members']
    require(type(rows) is list and bool(rows), 'nonempty source member table required')
    result, namespaces = {}, set()
    for row in rows:
        require(type(row) is dict and set(row) == {'archive_path','git_commit','git_path','git_blob','bytes','sha256'},
                'invalid source member fields')
        name, path = safe_path(row['archive_path']), safe_path(row['git_path'])
        parts = name.split('/',1)
        require(len(parts)==2 and parts[0] in ('current','baseline'), 'invalid source namespace')
        label, relative = parts
        require(relative == path and row['git_commit'] == inventory['source_commit' if label=='current' else 'authority_commit'],
                'source namespace/Git identity mismatch')
        require(type(row['git_blob']) is str and re.fullmatch('[0-9a-f]{40}',row['git_blob']), 'invalid Git blob identity')
        require(type(row['bytes']) is int and row['bytes'] >= 0, 'invalid source byte count')
        require(type(row['sha256']) is str and re.fullmatch('[0-9A-F]{64}',row['sha256']), 'invalid source SHA-256')
        require(name.casefold() not in result, 'duplicate/case-colliding source member')
        result[name.casefold()] = row
        namespaces.add(label)
    require(namespaces == {'current','baseline'}, 'both current and baseline source must be preserved')
    names = [r['archive_path'] for r in rows]
    require(names == sorted(names), 'source member table must have canonical order')
    required_members = {MASTER,*('current/'+s+'.tex' for s in inventory['chapter_stems']),
                        *('current/tools/'+name for name in REQUIRED_TOOLS)}
    require(required_members <= set(names), 'required chapter/master/build-support member missing')
    for key in ('scope','baseline_current_distinction'):
        if key in inventory:
            require(type(inventory[key]) is str and bool(inventory[key].strip()), 'invalid inventory description')
    return {r['archive_path']:r for r in rows}

def assert_no_reparse(path, *, missing_ok=False):
    """Check every lexical ancestor before resolve() can hide a symlink/junction."""
    path = Path(path).absolute()
    cursor = Path(path.anchor)
    for part in path.parts[1:]:
        cursor = cursor/part
        try:
            entry = os.lstat(cursor)
        except FileNotFoundError:
            require(missing_ok, 'missing source path: '+str(cursor))
            continue
        require(not stat.S_ISLNK(entry.st_mode)
                and not (getattr(entry,'st_file_attributes',0) & getattr(stat,'FILE_ATTRIBUTE_REPARSE_POINT',1024)),
                'symlink/reparse path rejected: '+str(cursor))
    return path

def verified_member_bytes(root, row, *, strip_current=False):
    name = safe_path(row['archive_path'])
    if strip_current:
        require(name.startswith('current/'), 'expected current source member')
        name = name[len('current/'):]
    root = assert_no_reparse(root).resolve(strict=True)
    path = assert_no_reparse(root/name)
    require(path.resolve(strict=True).is_relative_to(root), 'source path escapes root')
    with path.open('rb') as stream:
        opened = os.fstat(stream.fileno())
        require(stat.S_ISREG(opened.st_mode), 'source is not a regular file')
        raw = stream.read()
    after = os.lstat(assert_no_reparse(path))
    require((opened.st_dev,opened.st_ino) == (after.st_dev,after.st_ino), 'source path changed during read')
    require(identity(raw) == {k:row[k] for k in ('bytes','sha256')}, 'source byte identity changed: '+name)
    return raw

class GitObjects:
    def __init__(self, root):
        self.root = Path(root)
    def raw(self, *args):
        return subprocess.check_output(['git', '-C', str(self.root), *args])
    def commit(self, revision):
        require(re.fullmatch('[0-9a-f]{40}', revision) is not None, 'exact commit required')
        require(self.raw('rev-parse', revision+'^{commit}').decode().strip() == revision,
                'not an exact commit object')
        return revision
    def tree(self, revision):
        self.commit(revision)
        result = {}
        for record in self.raw('ls-tree', '-r', '-z', revision).split(b'\0'):
            if not record:
                continue
            meta, path = record.split(b'\t', 1)
            mode, kind, blob = meta.decode().split()
            path = path.decode('utf-8')
            safe_path(path)
            result[path] = {'mode': mode, 'kind': kind, 'blob': blob}
        return result
    def blob(self, revision, path):
        safe_path(path)
        return self.raw('cat-file', 'blob', revision+':'+path)

def selected_native_paths(tree):
    """Pure policy, shared by producer and consumer. No trusted boolean gate."""
    return {path for path in tree if PurePosixPath(path).suffix.lower() in NATIVE | FIGURES
            or path.startswith(SUPPORT) or path in ROOT_SUPPORT}

def uncomment(text):
    # An escaped percent is text. Count preceding backslashes for literal %.
    lines = []
    for line in text.splitlines():
        cut = len(line)
        for index, char in enumerate(line):
            if char == '%':
                j = index-1
                while j >= 0 and line[j] == '\\':
                    j -= 1
                if (index-1-j) % 2 == 0:
                    cut = index
                    break
        lines.append(line[:cut])
    return '\n'.join(lines)

# A TeX control word stops before a digit: ``\input2.inc`` is an input call,
# even though a regular-expression word boundary would silently miss it.
DEPENDENCY = re.compile(r'\\(includegraphics|bibliographystyle|bibliography|documentclass|usepackage|RequirePackage|LoadClass|include|input)(?![A-Za-z])')
ARGUMENT = re.compile(r'\s*\*?\s*(?:\[[^\]]*\]\s*)?\{([^{}]+)\}')
DECLARATION = re.compile(r'\\(?:def|gdef|edef|xdef|let)\s*$|\\(?:newcommand|renewcommand|providecommand|DeclareRobustCommand)\*?\s*\{?\s*$')

def dependency_calls(text, path):
    """Parse every occurrence, rejecting unsupported executable syntax.

    Macro declaration identifiers and the literal protected command name in a
    class-warning MessageBreak are not calls. This is intentionally not a TeX
    macro interpreter: executable macro-valued file arguments fail closed.
    """
    for match in DEPENDENCY.finditer(text):
        preceding = text[:match.start()]
        slash_count = len(preceding)-len(preceding.rstrip('\\'))
        if slash_count % 2 or DECLARATION.search(preceding):
            continue
        command, tail = match[1], text[match.end():]
        argument = ARGUMENT.match(tail)
        if argument:
            token = argument[1].strip()
        elif command == 'input':
            literal = re.match(r'\s*([^\s\\{}#%]+)',tail)
            require(literal is not None, 'unsupported/dynamic native dependency: '+path+': '+match[0])
            token = literal[1]
        elif (command == 'includegraphics' and preceding.endswith('\\protect')
              and tail.startswith('\\MessageBreak')):
            continue
        else:
            raise ValueError('unsupported/dynamic native dependency: '+path+': '+match[0])
        require(not any(c in token for c in '\\#{}%~') and '^^' not in token,
                'dynamic native dependency: '+path+': '+token)
        yield command, token

def native_closure(objects, commit, tree, chapter_stems):
    """Resolve literal local TeX inputs; system classes/packages remain runtime deps.

    Externaldocument AUXs are generated references, not native inputs. All chapter
    bodies are nevertheless retained by the inventory's global native policy.
    """
    roots = [stem+'.tex' for stem in chapter_stems]
    require(all(root in tree for root in roots), 'chapter source missing from committed tree')
    seen, parsed, pending, system = set(), set(), [(root,True) for root in roots], set()
    while pending:
        path, parse_as_tex = pending.pop()
        if path in seen and (not parse_as_tex or path in parsed):
            continue
        require(tree[path]['kind'] == 'blob' and tree[path]['mode'] in ('100644', '100755'),
                'native source is not a regular committed blob: '+path)
        seen.add(path)
        if not parse_as_tex:
            continue
        parsed.add(path)
        text = uncomment(objects.blob(commit, path).decode('utf-8'))
        for command, token in dependency_calls(text,path):
            tokens = token.split(',') if command in ('bibliography','usepackage','RequirePackage') else [token]
            for token in tokens:
                token = token.strip()
                safe_path(token)
                suffixes = {'input': ['.tex'], 'include': ['.tex'], 'bibliography': ['.bib'],
                            'bibliographystyle': ['.bst'], 'documentclass': ['.cls'],
                            'usepackage': ['.sty'], 'RequirePackage': ['.sty'], 'LoadClass': ['.cls'],
                            'includegraphics': ['.pdf','.png','.jpg','.jpeg','.eps','.svg']}[command]
                names = [token] if PurePosixPath(token).suffix else [token+s for s in suffixes]
                if command == 'input' and not PurePosixPath(token).suffix:
                    names.append(token)  # Extensionless native files are valid inputs.
                # TeX runs from the project root; preserve root precedence.
                candidates = names + [str(PurePosixPath(path).parent/n) for n in names]
                target = next((name for name in candidates if name in tree), None)
                if target:
                    pending.append((target,command not in ('includegraphics','bibliography','bibliographystyle')))
                elif command in ('bibliographystyle','documentclass','usepackage','RequirePackage','LoadClass'):
                    system.add(command+':'+token)
                else:
                    raise ValueError('unresolved native dependency: '+path+': '+token)
    return seen, sorted(system)

def expected_source_members(root, source_commit, authority_commit, chapter_stems):
    """Return exactly archive_path -> six-field member identities.

    Current inputs are build-source Git bytes. The unmodified pinned authority is
    separately retained; an AI-only chapter need not exist in that older tree.
    """
    objects = root if hasattr(root, 'tree') and hasattr(root, 'blob') else GitObjects(root)
    validate_stems(chapter_stems)
    result = {}
    for label, commit in [('current',source_commit), ('baseline',authority_commit)]:
        tree = objects.tree(commit)
        selected = selected_native_paths(tree)
        roots = chapter_stems if label == 'current' else [s for s in chapter_stems if s+'.tex' in tree]
        closure, _ = native_closure(objects, commit, tree, roots)
        selected.update(closure)
        if label == 'current':
            require(all('tools/'+name in selected for name in REQUIRED_TOOLS), 'cumulative build support is not committed')
            master = parse_json(objects.blob(commit, 'tools/cumulative-master.json'))
            validate_master(master,chapter_stems)
        for path in sorted(selected):
            safe_path(path)
            row = tree[path]
            require(row['kind'] == 'blob' and row['mode'] in ('100644','100755'),
                    'archive input is not a regular Git blob: '+path)
            raw = objects.blob(commit, path)
            archive_path = label+'/'+path
            result[archive_path] = {'archive_path': archive_path, 'git_commit': commit,
                'git_path': path, 'git_blob': row['blob'], **identity(raw)}
    require(len({p.casefold() for p in result}) == len(result), 'case-colliding archive paths')
    return result

def make_inventory(root, source_commit, authority_commit, chapter_stems):
    members = expected_source_members(root, source_commit, authority_commit, chapter_stems)
    inventory = {'schema': SCHEMA, 'source_commit': source_commit, 'authority_commit': authority_commit,
            'master_path': MASTER, 'chapter_stems': list(chapter_stems),
            'members': [members[p] for p in sorted(members)],
            'closure': {'policy': POLICY, 'checked': True},
            'scope': '36-chapter cumulative release; additional native source is preserved, not claimed as built',
            'baseline_current_distinction': 'baseline is the pinned unmodified official source; current is the AI draft build source'}
    validate_inventory_shape(inventory)
    return inventory

def write_source_zip(root, inventory_raw, destination):
    inventory = parse_json(inventory_raw)
    validate_inventory_shape(inventory)
    expected = expected_source_members(root, inventory['source_commit'], inventory['authority_commit'], inventory['chapter_stems'])
    require(inventory['members'] == [expected[p] for p in sorted(expected)], 'source inventory is not exact native closure')
    objects = GitObjects(root)
    with zipfile.ZipFile(destination, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=9, allowZip64=True) as archive:
        for name in sorted([*expected, METADATA]):
            data = inventory_raw if name == METADATA else objects.blob(expected[name]['git_commit'], expected[name]['git_path'])
            if name != METADATA:
                require(identity(data) == {k:expected[name][k] for k in ('bytes','sha256')}, 'Git input drift')
            info = zipfile.ZipInfo(name, (1980,1,1,0,0,0))
            info.create_system, info.external_attr = 3, 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    verify_source_zip(destination, inventory_raw, expected)
    return {'source_members': len(expected), 'native_bytes': sum(v['bytes'] for v in expected.values())}

def verify_source_zip(path, inventory_raw, expected):
    inventory = parse_json(inventory_raw)
    require(validate_inventory_shape(inventory) == expected, 'ZIP expected inventory is not the validated table')
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        require([info.filename for info in infos] == sorted([*expected, METADATA]), 'missing/extra/duplicate source ZIP member')
        require(not archive.comment, 'unexpected source ZIP comment')
        for info in infos:
            safe_path(info.filename)
            require(not info.is_dir() and info.create_system == 3
                    and info.external_attr == 0o100644 << 16
                    and stat.S_ISREG(info.external_attr >> 16)
                    and info.flag_bits & ~0x800 == 0
                    and info.compress_type == zipfile.ZIP_DEFLATED
                    and info.date_time == (1980,1,1,0,0,0)
                    and not info.comment and not info.extra and info.internal_attr == 0,
                    'source ZIP member is not a deterministic regular file: '+info.filename)
        require(archive.read(METADATA) == inventory_raw, 'embedded source inventory mismatch')
        for name, row in expected.items():
            require(identity(archive.read(name)) == {k:row[k] for k in ('bytes','sha256')}, 'source ZIP byte mismatch: '+name)

def verify_extracted(root):
    root = assert_no_reparse(root).resolve(strict=True)
    metadata = assert_no_reparse(root/METADATA)
    require(stat.S_ISREG(os.lstat(metadata).st_mode), 'inventory is not a regular file')
    raw = metadata.read_bytes()
    inventory = parse_json(raw)
    members = validate_inventory_shape(inventory)
    for row in inventory['members']:
        verified_member_bytes(root,row)
    validate_master(parse_json(verified_member_bytes(root,members[MASTER])), inventory['chapter_stems'])
    return inventory
