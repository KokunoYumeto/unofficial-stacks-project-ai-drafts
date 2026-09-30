"""Add reversible metadata wrapping and bounded figures without changing formulas."""
import hashlib
import json
import re
from bisect import bisect_right
from datetime import datetime, timezone
from pathlib import Path

C = Path(__file__).resolve().parent
S = C / 'ALGEBRA_CONTEXTUAL_COMPANION_20260929'
H = 'revision-history/before-readable-layout'
BREAK = r'\allowbreak{}'
sha = lambda b: hashlib.sha256(b).hexdigest().upper()
dump = lambda v: (json.dumps(v, ensure_ascii=False, indent=2) + '\n').encode()

def balanced(s, pos, opening, closing):
    assert s[pos] == opening
    level, i = 1, pos + 1
    while i < len(s):
        if s[i] == '\\':
            i += 2
            continue
        if s[i] == opening:
            level += 1
        elif s[i] == closing:
            level -= 1
            if not level:
                return i + 1
        i += 1
    raise AssertionError(('Unbalanced parameter', s[pos:pos+100]))

def protected(s):
    spans = []
    # Text metadata never changes inside an original math environment or delimiter.
    envs = r'equation\*?|align\*?|alignat\*?|gather\*?|multline\*?|eqnarray\*?|displaymath|math|xymatrix|tikzcd'
    for m in re.finditer(r'\\begin\{(' + envs + r')\}', s):
        end = s.find(r'\end{' + m[1] + '}', m.end())
        assert end >= 0
        spans.append((m.start(), end + len(m[1]) + 6))
    environment_spans = sorted(spans)
    environment_starts = [a for a,b in environment_spans]
    i = 0
    while i < len(s):
        env_index = bisect_right(environment_starts, i) - 1
        if env_index >= 0 and i < environment_spans[env_index][1]:
            i = environment_spans[env_index][1]
            continue
        if s.startswith(r'\[', i) or s.startswith(r'\(', i):
            close = r'\]' if s[i+1] == '[' else r'\)'
            end = s.find(close, i + 2)
            assert end >= 0
            spans.append((i, end+2)); i = end+2; continue
        if s[i] == '$':
            delim = '$$' if s.startswith('$$', i) else '$'
            end = i + len(delim)
            while True:
                end = s.find(delim, end)
                assert end >= 0
                n = len(s[:end]) - len(s[:end].rstrip('\\'))
                if n % 2 == 0:
                    break
                end += len(delim)
            spans.append((i, end+len(delim))); i = end+len(delim); continue
        if s[i] == '%':
            end = s.find('\n', i)
            end = len(s) if end < 0 else end
            spans.append((i, end)); i = end; continue
        if s[i] == '\\':
            i += 2
        else:
            i += 1
    pattern = r'\\(label|(?:eq|page|name)?ref|cite[a-zA-Z]*|bibitem|href|hyperlink|hypertarget|url|nolinkurl|path|includegraphics|input|externaldocument|index)\*?'
    for m in re.finditer(pattern, s):
        i = m.end()
        while i < len(s) and s[i].isspace(): i += 1
        while i < len(s) and s[i] == '[':
            i = balanced(s, i, '[', ']')
            while i < len(s) and s[i].isspace(): i += 1
        for _ in range(2 if m[1] in ('href', 'hyperlink', 'hypertarget') else 1):
            if i < len(s) and s[i] == '{':
                i = balanced(s, i, '{', '}')
                while i < len(s) and s[i].isspace(): i += 1
        spans.append((m.start(), i))
    return spans

def break_token(token):
    units = re.findall(r'\\[_#%]|.', token)
    groups, run = [], 0
    limit = 4 if re.fullmatch(r'[A-Fa-f0-9]{40,64}', token) else 12
    for i, unit in enumerate(units):
        groups.append(unit); run += 1
        if i < len(units)-1 and (unit in ['/', '.', '-', ':', r'\_', r'\#'] or run >= limit):
            groups.append(BREAK); run = 0
    return ''.join(groups)

def wrap_metadata(s):
    assert BREAK not in s
    spans = protected(s)
    pattern = r'(?<![A-Za-z0-9])(?:[A-Za-z0-9:/._-]|\\[_#%])+\.(?:md|tex|py|json|jsonl|svg|png|pdf)(?:\\#L\d+)?|(?<![A-Za-z0-9])[A-Fa-f0-9]{40,64}(?![A-Za-z0-9])'
    edits = []
    for m in re.finditer(pattern, s):
        if len(m[0]) < 26 or any(a < m.end() and m.start() < b for a,b in spans):
            continue
        replacement = break_token(m[0])
        assert replacement.replace(BREAK, '') == m[0]
        edits.append(dict(start=m.start(), end=m.end(), original=m[0], replacement=replacement,
                          source_line=s.count('\n', 0, m.start())+1))
    t = s
    for e in reversed(edits): t = t[:e['start']] + e['replacement'] + t[e['end']:]
    assert t.replace(BREAK, '') == s
    return t, edits

def main():
    assert not (S / H).exists()
    old_m = (S / 'MANIFEST.json').read_bytes()
    assert sha(old_m) == '8963D5E15FD8AA5B2B0354980EC04AFD2EE5E1C5CDD11FBF50B6545B73BCC9D1'
    m = json.loads(old_m)
    for row in m['files']:
        assert sha((S / row['file']).read_bytes()) == row['sha256'], row['file']
    files = {H + '/MANIFEST.json': old_m}
    changes = []
    names = sorted({r['tex'] for r in m['proof_notes']} | {'contextual-arguments.tex'} |
                   {r['file'] for r in m['files'] if re.fullmatch(r'contexts/ALGEBRA-CONTEXT-\d+\.tex', r['file'])})
    for name in names:
        old = (S / name).read_bytes()
        new, edits = wrap_metadata(old.decode())
        if edits:
            files[H + '/' + name] = old
            files[name] = new.encode()
            changes.append(dict(file=name, before_sha256=sha(old), after_sha256=sha(new.encode()),
                                literal_wraps=edits, inverse_exact=True, protected_math_and_link_parameters_unchanged=True))
    master_old = (S / 'algebra-editorial.tex').read_bytes()
    old_definition = br'\providecommand{\pandocbounded}[1]{#1}'
    new_definition = br'''% Bound each supplied figure by the available text width; preserve its aspect ratio.
\newsavebox{\AlgebraFigureBox}
\providecommand{\pandocbounded}[1]{%
  \sbox{\AlgebraFigureBox}{#1}%
  \ifdim\wd\AlgebraFigureBox>\linewidth
    \resizebox{\linewidth}{!}{\usebox{\AlgebraFigureBox}}%
  \else\usebox{\AlgebraFigureBox}\fi}
% Long editorial headings occupy their own line; their numbering and text remain.
\makeatletter
\def\subsection{\@startsection{subsection}{2}%
  \z@{.5\linespacing\@plus.7\linespacing}{.3\linespacing}%
  {\normalfont\bfseries}}
\def\subsubsection{\@startsection{subsubsection}{3}%
  \z@{.5\linespacing\@plus.7\linespacing}{.3\linespacing}%
  {\normalfont\bfseries}}
\makeatother
\emergencystretch=3em
\usepackage{enumitem}
\newlist{AlgebraSourceRoutes}{description}{1}
\setlist[AlgebraSourceRoutes]{style=nextline,leftmargin=1.5em,font=\normalfont\bfseries}'''
    assert master_old.count(old_definition) == 1
    master_new = master_old.replace(old_definition, new_definition)
    assert master_new.replace(new_definition, old_definition) == master_old
    files[H + '/algebra-editorial.tex'] = master_old
    files['algebra-editorial.tex'] = master_new
    routing_old = (S / 'source-routing.tex').read_bytes()
    assert b'AlgebraSourceRoutes' not in routing_old
    routing_new = routing_old.replace(br'\begin{description}', br'\begin{AlgebraSourceRoutes}').replace(br'\end{description}', br'\end{AlgebraSourceRoutes}')
    assert routing_new.replace(b'AlgebraSourceRoutes', b'description') == routing_old
    files[H + '/source-routing.tex'] = routing_old
    files['source-routing.tex'] = routing_new
    visual = dict(pdf='ALGEBRA_PORTABLE_BUILD_20260929/attempt-11/a/algebra-editorial.pdf',
                  pdf_sha256='871B04A67E3344B2BEB8CB6DC05D798CABAC2D15B575FF0760242530F5D4D149',
                  pages_actually_viewed=[293,654,656],
                  observations='Pages 293 and 656 visibly clip long source hashes and filenames at the right page edge. Page 654 retains a long displayed identity protruding into the margin; its terms remain visible. Two separate image overflows are confirmed by TeX diagnostics at 724.08 and 651.81 points. Fresh rendered review is required after repair.',
                  complete_document_review=False, accepted=False)
    receipt = dict(id='RENDER-TEX-008', created_at_utc=datetime.now(timezone.utc).isoformat(),
        cause='Unbreakable metadata, long run-in headings, narrow route-list bodies and figures emitted at unrestricted natural dimensions.',
        metadata_changes=changes, total_tokens_wrapped=sum(len(r['literal_wraps']) for r in changes),
        metadata_inverse='Remove only the inserted allowbreak empty-group commands to recover each exact previous TeX file.',
        display_math_changed=False, inline_math_changed=False, labels_changed=False, link_destinations_changed=False,
        source_routing_records_changed=False, original_markdown_changed=False,
        master_before_sha256=sha(master_old), master_after_sha256=sha(master_new),
        bounded_figures=2, figure_bytes_changed=False,
        route_lists=routing_old.count(br'\begin{description}'),
        heading_contents_and_numbering_preserved=True, linebreak_emergency_stretch='3em',
        diagnostic_suppression=False, observed_visual_defects=visual,
        complete_build=False, fresh_visual_acceptance=False)
    old_ledger = (S / 'TYPESETTING_CORRECTIONS.json').read_bytes()
    ledger = json.loads(old_ledger)
    ledger['readable_layout_repair'] = {k:v for k,v in receipt.items() if k != 'metadata_changes'}
    ledger['readable_layout_repair']['full_receipt'] = 'READABLE_LAYOUT_REPAIR.json'
    files[H + '/TYPESETTING_CORRECTIONS.json'] = old_ledger
    files['TYPESETTING_CORRECTIONS.json'] = dump(ledger)
    files['READABLE_LAYOUT_REPAIR.json'] = dump(receipt)
    files['reproducers/' + Path(__file__).name] = Path(__file__).read_bytes()
    for row in m['proof_notes']:
        if row['tex'] in files:
            row['before_metadata_wrapping_tex_sha256'] = row['tex_sha256']
            row['tex_sha256'] = sha(files[row['tex']])
            row['metadata_wrapping_inverse_exact'] = True
            row['namespace_inverse_recovers_exact_initial_tex'] = False
            row['namespace_inverse_note'] = 'Undo the recorded metadata wrapping and earlier identified repairs before comparison with the retained initial conversion.'
    for row in m['source_contexts']:
        name = 'contexts/' + row['id'] + '.tex'
        if name in files:
            row['before_metadata_wrapping_typeset_sha256'] = row['typeset_context_sha256']
            row['typeset_context_sha256'] = sha(files[name])
    m['typesetting_corrections'].update(sha256=sha(files['TYPESETTING_CORRECTIONS.json']),
                                      readable_layout_repair='READABLE_LAYOUT_REPAIR.json')
    m['revised_at_utc'] = receipt['created_at_utc']
    index = {r['file']:r for r in m['files']}
    for name,raw in files.items(): index[name] = dict(file=name, bytes=len(raw), sha256=sha(raw))
    m['files'] = sorted(index.values(),key=lambda r:r['file'])
    for name,raw in files.items():
        p=S/name; p.parent.mkdir(parents=True,exist_ok=True); p.write_bytes(raw)
    (S/'MANIFEST.json').write_bytes(dump(m))
    print(json.dumps(dict(result='PASS_REVERSIBLE_LAYOUT_SOURCE_REPAIR', changed_metadata_files=len(changes),
        total_tokens_wrapped=receipt['total_tokens_wrapped'], route_lists=receipt['route_lists'],
        manifest_sha256=sha(dump(m)), complete_build=False)))

if __name__ == '__main__':
    main()
