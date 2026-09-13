"""Assemble exact chapter PDFs with collision-free destinations; no TeX changes.

The merged file is a new artifact, requiring its own byte/determinism/visual QA.
Existing source PDFs are read only. Named destinations are chapter::name.
"""
from __future__ import annotations
import io
from pathlib import Path, PurePosixPath
from pypdf import PdfReader, PdfWriter
import pypdf
from pypdf.generic import ArrayObject, DictionaryObject, NameObject, TextStringObject, NumberObject
from cumulative_source import identity, require, validate_master

PDF_NAME = '01-cumulative-reader.pdf'

def chapter_ranges(chapters, artifacts):
    by_stem = {r['stem']:r for r in artifacts}
    require(len(by_stem) == len(artifacts), 'duplicate PDF artifact')
    require(set(by_stem) == {r['stem'] for r in chapters}, 'master/build chapter mismatch')
    start, result = 1, []
    for chapter in chapters:
        row = by_stem[chapter['stem']]
        require(type(row['pages']) is int and row['pages'] > 0, 'invalid page count')
        result.append({'stem':chapter['stem'], 'title':chapter['title'], 'start_page':start,
                       'end_page':start+row['pages']-1, 'pages':row['pages'],
                       'source_pdf':{k:row[k] for k in ('bytes','sha256')}})
        start += row['pages']
    return result

def namespace(stem, name):
    require('::' not in stem, 'invalid chapter namespace')
    return stem+'::'+str(name)

def remote_stem(file_spec):
    if hasattr(file_spec, 'get_object'):
        file_spec = file_spec.get_object()
    if isinstance(file_spec, dict):
        file_spec = file_spec.get('/UF', file_spec.get('/F',''))
    value = str(file_spec)
    # Do not internalize network URLs, absolute paths, or escaped relative paths.
    if ':' in value or '\\' in value or value.startswith('/') or '..' in value.split('/'):
        return None
    path = PurePosixPath(value)
    if len(path.parts) != 1:
        return None
    return path.stem if path.suffix.lower() == '.pdf' else None

def internal_remote_target(action, included_stems):
    """Only a proven sibling filename names this release's included chapter."""
    if action.get('/S') != '/GoToR':
        return None
    stem = remote_stem(action.get('/F'))
    return stem if stem in included_stems else None

def rewrite_link_action(action, stem, included_stems, destination, clone):
    """Shared actual action branch; retained external file/destination is exact."""
    require('/Next' not in action, 'chained PDF action needs dedicated review')
    kind = action.get('/S')
    target = internal_remote_target(action,included_stems)
    if kind == '/GoTo' or target is not None:
        rewritten = DictionaryObject({NameObject('/S'):NameObject('/GoTo'),
            NameObject('/D'):destination(action['/D'], target or stem, remote=target is not None)})
        return rewritten, 'internalized' if target is not None else 'local'
    require(kind in ('/GoToR','/URI'), 'unsupported active PDF action: '+str(kind))
    return clone(action), 'external' if kind == '/GoToR' else 'uri'

def normalized_name(value):
    if isinstance(value, bytes):
        return value.decode('utf-8')
    return str(value)

def merge_chapters(pdf_root, master, artifacts, output_path):
    validate_master(master)
    require(master.get('pypdf_version') == pypdf.__version__, 'assembly runtime differs from committed master')
    rows = chapter_ranges(master['chapters'], artifacts)
    readers, destination_sets, offsets = {}, {}, {}
    pdf_root = Path(pdf_root).resolve(strict=True)
    for row in rows:
        stem = row['stem']
        path = pdf_root/(stem+'.pdf')
        require(path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(pdf_root), 'invalid chapter PDF path')
        raw = path.read_bytes()
        require(identity(raw) == row['source_pdf'], 'chapter PDF identity mismatch: '+stem)
        reader = PdfReader(io.BytesIO(raw), strict=True)
        require(not reader.is_encrypted and len(reader.pages) == row['pages'], 'chapter PDF shape mismatch')
        require(not reader.get_fields(), 'fillable PDFs require a dedicated merger')
        readers[stem], offsets[stem] = reader, row['start_page']-1
        destination_sets[stem] = set(reader.named_destinations)
    writer = PdfWriter()
    for row in rows:
        for page in readers[row['stem']].pages:
            writer.add_page(page, excluded_keys=('/Annots',))

    def explicit_destination(value, stem, remote=False):
        if hasattr(value, 'get_object'):
            value = value.get_object()
        if not isinstance(value, (list, ArrayObject)):
            name = normalized_name(value)
            require(name in destination_sets[stem], 'missing named destination: '+stem+':'+name)
            return TextStringObject(namespace(stem, name))
        require(len(value) >= 2, 'malformed explicit destination')
        first = value[0]
        if remote:
            require(isinstance(first, (int, NumberObject)), 'remote destination is not a numeric page')
            index = int(first)
        else:
            index = readers[stem].get_page_number(first.get_object() if hasattr(first,'get_object') else first)
        require(index is not None and 0 <= index < len(readers[stem].pages), 'destination page out of range')
        return ArrayObject([writer.pages[offsets[stem]+index].indirect_reference,
                            *[x.clone(writer) for x in value[1:]]])

    for row in rows:
        stem = row['stem']
        reader = readers[stem]
        for name, dest in reader.named_destinations.items():
            index = reader.get_destination_page_number(dest)
            require(index is not None and 0 <= index < row['pages'], 'bad source named destination')
            array = ArrayObject([writer.pages[offsets[stem]+index].indirect_reference,
                                 *[v.clone(writer) for v in dest.dest_array[1:]]])
            writer.add_named_destination_array(TextStringObject(namespace(stem,name)), array)
        writer.add_outline_item(row['title'], offsets[stem])

    internalized, retained_external, local_links, external_loci = 0, 0, 0, []
    for row in rows:
        stem = row['stem']
        for page_index, page in enumerate(readers[stem].pages):
            annotations = ArrayObject()
            for ref in page.get('/Annots', []):
                source = ref.get_object()
                require(source.get('/Subtype') != '/Widget', 'unexpected PDF widget')
                copied = DictionaryObject()
                for key, value in source.items():
                    if key not in ('/P','/A','/Dest'):
                        copied[NameObject(key)] = value.clone(writer)
                if '/Dest' in source:
                    copied[NameObject('/Dest')] = explicit_destination(source['/Dest'],stem)
                    local_links += 1
                if '/A' in source:
                    action = source['/A'].get_object()
                    rewritten, disposition = rewrite_link_action(action,stem,readers,explicit_destination,
                                                                 lambda value:value.clone(writer))
                    copied[NameObject('/A')] = rewritten
                    if disposition == 'local':
                        local_links += 1
                    elif disposition == 'internalized':
                        internalized += 1
                    elif disposition == 'external':
                        retained_external += 1
                        external_loci.append({'stem':stem,'page':page_index+1,
                            'file':str(action.get('/F')),'destination':str(action.get('/D'))})
                copied[NameObject('/P')] = writer.pages[offsets[stem]+page_index].indirect_reference
                annotations.append(writer._add_object(copied))
            if annotations:
                writer.pages[offsets[stem]+page_index][NameObject('/Annots')] = annotations
    writer.add_metadata({'/Title':'Unofficial Stacks Project AI Drafts - cumulative 36-chapter reader',
                         '/Subject':'An unofficial draft collection, not the complete Stacks Project or an official release',
                         '/Creator':'Cumulative native-source release workflow'})
    with Path(output_path).open('xb') as stream:
        writer.write(stream)
    merged = PdfReader(output_path, strict=True)
    require(len(merged.pages) == sum(r['pages'] for r in rows), 'cumulative page count changed')
    expected_names = {namespace(stem,name) for stem,names in destination_sets.items() for name in names}
    require(set(merged.named_destinations) == expected_names, 'merged destination inventory differs')
    for row in rows:
        for index, original in enumerate(readers[row['stem']].pages):
            actual = merged.pages[offsets[row['stem']]+index]
            require(list(actual.mediabox) == list(original.mediabox)
                    and list(actual.cropbox) == list(original.cropbox), 'page boxes changed')
            require(actual.get_contents().get_data() == original.get_contents().get_data(), 'page drawing stream changed')
            for ref in actual.get('/Annots', []):
                annotation = ref.get_object()
                action = annotation.get('/A', {})
                target = annotation.get('/Dest', action.get('/D') if action.get('/S') == '/GoTo' else None)
                if isinstance(target, (str,bytes)):
                    require(normalized_name(target) in expected_names, 'dangling merged internal destination')
    return {'scope':'36-chapter cumulative release, not the full Stacks Project',
            'chapter_count':len(rows), 'total_pages':len(merged.pages), 'chapters':rows,
            'links':{'internalized':internalized, 'retained_external':retained_external,
                     'local_links':local_links, 'external_loci':external_loci},
            'mechanical_checks':'page count, named-destination closure, page boxes, drawing-stream bytes',
            'visual_qa_performed':False}
