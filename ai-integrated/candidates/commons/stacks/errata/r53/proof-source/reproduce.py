"""Reproduce one R53 prior/corrected chapter proof from the complete bundled inputs."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
from tex_slot import TexSlot

ROOT=Path(__file__).resolve().parent
def sha(raw):return hashlib.sha256(raw).hexdigest().upper()

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--role',choices=['prior','successor'],required=True)
    p.add_argument('--chapter',choices=['introduction','topology'],required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--pdflatex',default=shutil.which('pdflatex'))
    p.add_argument('--bibtex',default=shutil.which('bibtex'))
    a=p.parse_args(); out=a.output.resolve()
    if out.exists() or not a.pdflatex or not a.bibtex:raise ValueError('Use a fresh output and available TeX engines')
    data=json.loads((ROOT/'inputs.json').read_bytes())
    for row in data['files']:
        raw=(ROOT/row['path']).read_bytes()
        assert len(raw)==row['bytes'] and sha(raw)==row['sha256'],row['path']
    out.mkdir(parents=True)
    for name in (a.chapter+'.tex','preamble.tex','stacks-project.cls','chapters.tex','my.bib'):
        (out/name).write_bytes((ROOT/a.role/name).read_bytes())
    env=dict(os.environ,SOURCE_DATE_EPOCH='1790010000',FORCE_SOURCE_DATE='1',TZ='UTC')
    if os.name=='nt':from tex_process_guard import run_captured
    with TexSlot(15000) as slot:
        def launch(command,label):
            if os.name=='nt':
                result=run_captured(command,cwd=out,env=env,timeout=180,caller_holds_tex_mutex=slot.owned,
                    receipt_path=out/(label+'-capture.json'))
            else:result=subprocess.run(command,cwd=out,env=env,timeout=180,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
            (out/(label+'.log')).write_text(result.stdout,encoding='utf-8')
            if result.returncode:raise RuntimeError('Build failed: '+label)
        prior=None
        for sweep in range(1,7):
            launch([a.pdflatex,'-no-shell-escape','-interaction=nonstopmode','-halt-on-error','-file-line-error',
                '-recorder','-synctex=1',a.chapter+'.tex'],'tex-'+str(sweep))
            if sweep==1:launch([a.bibtex,a.chapter],'bibtex')
            vector={ext:sha((out/(a.chapter+'.'+ext)).read_bytes()) for ext in ('pdf','aux','out','toc','bbl')}
            if vector==prior:break
            prior=vector
        else:raise RuntimeError('No fixed point within six sweeps')
        raw=(out/(a.chapter+'.pdf')).read_bytes(); actual={'bytes':len(raw),'sha256':sha(raw)}
        assert actual==data['pdfs'][a.role][a.chapter],(actual,data['pdfs'][a.role][a.chapter])
    receipt={'passed':True,'role':a.role,'chapter':a.chapter,'pdf':actual,'fixed_point_sweep':sweep,'mutex':slot.receipt,
        'scope':'Isolated chapter proof; intentionally omits external chapter auxiliaries. Not a complete cross-chapter Stacks reader.'}
    (out/'REPRODUCTION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(receipt))

if __name__=='__main__':main()
