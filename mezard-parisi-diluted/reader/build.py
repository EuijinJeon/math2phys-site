"""Build a numbered, offline HTML reader directly from the release LaTeX."""
import base64
import html
import json
import re
import shutil
import subprocess
import tempfile
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parents[1] / 'redesign/source'
LABEL = r'\\label(?:\[\w+\])?\{([^}]+)\}'
DISPLAY = r'\\\[(.*?)\\\]|\\begin\{(equation|align\*?)\}(.*?)\\end\{\2\}'
REF = r'\\(eqref|ref|[Cc]ref|cite)(?:\[([^\]]+)\])?\{([^}]+)\}'
THEOREMS = 'lemma|theorem|corollary|remark|proposition'
esc = html.escape


def plain(text):
    text = re.sub(r"\\(['])\{?(\w)\}?", lambda m: unicodedata.normalize('NFC', m[2]+'\u0301'), text)
    return text.replace(r'\&', '&').replace('--', '–').replace('~', ' ').replace('``', '“').replace("''", '”')


def bibliography():
    with tempfile.TemporaryDirectory() as d:
        path = Path(d)
        shutil.copy(SOURCE / 'references.bib', path)
        (path/'paper.aux').write_text(r'\citation{*}'+'\n'+r'\bibstyle{plain}'+'\n'+r'\bibdata{references}')
        subprocess.run(['bibtex', 'paper'], cwd=d, check=True, stdout=subprocess.DEVNULL)
        data = (path/'paper.bbl').read_text()
    entries = {}
    for key, body in re.findall(r'\\bibitem\{([^}]+)\}(.*?)(?=\\bibitem|\\end\{thebibliography\})',data,re.S):
        body = re.sub(r'\\href\{([^}]+)\}\{([^}]+)\}',r'\2',body)
        body = plain(body.replace('\\newblock',' ').replace('\\em ','').replace('\\ ',' ')).replace('{','').replace('}','')
        entries[key] = ' '.join(body.split())
    return entries


def generate():
    main = (SOURCE/'main.tex').read_text()
    body = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}',main,re.S)[1]
    body += '\n' + '\n'.join((SOURCE/(f+'.tex')).read_text() for f in re.findall(r'\\input\{(sections/[^}]+)\}',main))
    bib = bibliography()
    labels, tokens, expressions = {}, [], []
    chunks = ['<h2 id="abstract">Abstract</h2>']
    options = ['<option value="abstract">Abstract</option>']
    notes = json.loads((ROOT/'annotations.json').read_text())
    inputs = json.loads((ROOT/'inputs.json').read_text())
    outputs = {}
    for target, sources in inputs.items():
        for source, description in sources.items():
            outputs.setdefault(source, {})[target] = description
    unused = set(notes) | set(inputs) | set(outputs)
    sentence = section = subsection = equation = theorem = 0

    def token(markup):
        tokens.append(markup)
        return f'⟪{len(tokens)-1}⟫'

    def math(tex, display=False):
        expressions.append([tex.strip(),display])
        return f'<!--math{len(expressions)-1}-->'

    def display(m):
        nonlocal equation
        env, raw = m[2], (m[1] if m[1] is not None else m[3]).strip()
        rows = raw.split(r'\\') if env == 'align' else [raw]
        parts = []
        for row in rows:
            tag = ''
            if env in ('equation','align') and not re.search(r'\\(?:notag|nonumber)\b',row):
                equation += 1
                tag = f'{section}.{equation}'
            for label in re.findall(LABEL,row):
                labels[label] = ('Equation', tag)
            tex = re.sub(LABEL,'',row)
            tex = re.sub(r'\\(?:notag|nonumber)\b','',tex).strip()
            if env in ('align','align*'):
                tex = r'\begin{aligned}'+tex+r'\end{aligned}'
            anchors = ''.join(f'<i id="{key}"></i>' for key in re.findall(LABEL,row))
            parts.append(f'<div class="formula">{anchors}{math(tex,True)}'
                         + (f'<span>({tag})</span>' if tag else '') + '</div>')
        tail = re.sub(r'\\end\{(?:aligned|gathered|cases)\}\s*$', '', re.sub(LABEL, '', raw))
        ended = tail.rstrip().endswith('.')
        return token(''.join(parts)) + ('※' if ended else '')

    def reference(m):
        command, arg, keys = m.groups()
        out = []
        for key in keys.split(','):
            key = key.strip()
            if command == 'cite':
                out.append(f'<a href="#bib-{key}">{list(bib).index(key)+1}</a>')
            else:
                kind, number = labels[key]
                value = f'({number})' if command == 'eqref' else number
                if command.lower() == 'cref':
                    value = kind + ' ' + value
                out.append(f'<a href="#{key}">{value}</a>')
        value = ', '.join(out)
        return '['+value+(', '+esc(plain(arg)) if arg else '')+']' if command=='cite' else value

    def annotation(text):
        parts = re.split(r'(\\\(.*?\\\)|\\\[.*?\\\])',text, flags=re.S)
        return ''.join(math(p[2:-2],p.startswith(r'\[')) if i%2 else esc(p) for i,p in enumerate(parts))

    def emit(text):
        nonlocal sentence
        text = re.sub(r'\$([^$]*)\$', lambda m:token(math(m[1])),text)
        text = re.sub(REF, lambda m:token(m[0]),text)
        text = re.sub(r'\\emph\{([^{}]*)\}',r'<em>\1</em>',text)
        text = ' '.join(plain(text).split())
        for part in re.split(r'(?<=[.!?])(?=\s|$)|(?<=\.</em>)(?=\s)|※',text):
            part = part.strip()
            if not part: continue
            sentence += 1
            key = f'S{sentence:04d}'
            # Tokens keep complete math and citations intact during segmentation.
            content = re.sub(r'⟪(\d+)⟫',lambda m:tokens[int(m[1])],part)
            entries = notes.get(key,[])
            unused.discard(key)
            if key in notes and (not isinstance(entries,list) or not entries):
                raise ValueError(key)
            panel = ''.join('<h4>'+annotation(e['question'])+'</h4><p>'+annotation(e['answer'])+'</p>' for e in entries)
            for heading, links in [('입력', inputs.get(key)), ('출력', outputs.get(key))]:
                if links:
                    items = ''.join(
                        f'<li><a href="#{esc(other)}">{esc(other)}</a> · {esc(reason)}</li>'
                        for other, reason in links.items()
                    )
                    panel += f'<h4>{heading}</h4><ul>{items}</ul>'
            chunks.append(f'<article id="{key}"><a class="number" aria-expanded="false" href="#{key}">{key}</a>'
                          f'<div class="sentence" lang="en">{content}</div><aside hidden'
                          + (' data-noted' if panel else '')+'>'+ (panel or '아직 작성된 주석이 없습니다.')+'</aside></article>')

    # Structural headings delimit paragraphs. List markers stay inside the
    # grammatical sentence, including lists introduced by “such that”.
    structure = re.compile(r'\\(section|subsection|paragraph)\{([^{}]+)\}|'
        r'\\begin\{('+THEOREMS+r'|proof)\}(?:\[([^\]]+)\])?|'
        r'\\end\{(?:'+THEOREMS+r'|proof)\}|\\begin\{figure\}.*?\\end\{figure\}',re.S)
    pos = 0
    current = None
    def prose(s):
        s = re.sub(DISPLAY,display,s,flags=re.S)
        def anchor(m):
            labels[m[1]] = current
            chunks.append(f'<i id="{m[1]}"></i>')
            return ''
        s = re.sub(LABEL,anchor,s)
        def enumeration(m):
            items=m[2].split(r'\item')[1:]
            return ' '.join(token('<b>'+('('+['i','ii','iii'][i]+')' if 'roman' in m[1] else str(i+1)+'.')+'</b>')+' '+item.strip() for i,item in enumerate(items))
        s = re.sub(r'\\begin\{enumerate\}\[([^\]]*)\](.*?)\\end\{enumerate\}',enumeration,s,flags=re.S)
        emit(s)
    for m in structure.finditer(body):
        prose(body[pos:m.start()])
        pos = m.end()
        if m[1]:
            name,title=m[1],m[2]
            if name=='paragraph':
                chunks.append('<h4>'+title+'</h4>')
                continue
            if name=='section':
                section+=1
                equation=theorem=subsection=0
                n=str(section)
            else:
                subsection+=1
                n=f'{section}.{subsection}'
            current=('Section',n)
            tag='h2' if name=='section' else 'h3'
            chunks.append(f'<{tag} id="sec-{n}">{n} {title}</{tag}>')
            options.append(f'<option value="sec-{n}">{n} {title}</option>')
        elif m[3]:
            kind=m[3].capitalize()
            if kind!='Proof':
                theorem+=1
                current=(kind,f'{section}.{theorem}')
                kind+=' '+current[1]
            title=m[4] or ''
            title=re.sub(r'\$([^$]*)\$',lambda t:math(t[1]),title)
            chunks.append('<h4>'+kind+(' · '+title if title else '')+'</h4>')
        elif m[0].startswith(r'\begin{figure}'):
            key=re.search(LABEL,m[0])[1]
            labels[key]=('Figure','1')
            image=base64.b64encode((ROOT/'figure1.png').read_bytes()).decode()
            chunks.append(f'<figure id="{key}"><img alt="One local shift on the target tree" src="data:image/png;base64,{image}"><figcaption>Figure 1</figcaption></figure>')
            emit(re.search(r'\\caption\{(.*?)\}\s*\\label',m[0],re.S)[1])
    prose(body[pos:])
    if unused: raise ValueError(f'Unknown sentence IDs: {unused}')
    chunks.append('<h2 id="references">References</h2><ol>')
    options.append('<option value="references">References</option>')
    chunks.extend(f'<li id="bib-{k}">{esc(v)}</li>' for k,v in bib.items())
    chunks.append('</ol>')
    article=re.sub(REF,reference,'\n'.join(chunks))
    macros={k:v for k,v in re.findall(r'\\(?:re)?newcommand\{(\\\w+)\}(?:\[1\])?\{(.*)\}',main)}
    macros.update({k:r'\operatorname{'+v+'}' for k,v in re.findall(r'\\DeclareMathOperator\{(\\\w+)\}\{(\w+)\}',main)})
    data=json.dumps(dict(expressions=expressions,macros=macros))
    rendered=json.loads(subprocess.run(['node',str(ROOT/'math.cjs')],input=data,text=True,stdout=subprocess.PIPE,check=True).stdout)
    article=re.sub(r'<!--math(\d+)-->',lambda m:rendered[int(m[1])],article)
    template=(ROOT/'template.html').read_text()
    (ROOT/'index.html').write_text(template.replace('<!--BODY-->',article).replace('<!--TOC-->',''.join(options)))
    print(f'{sentence} sentences, {len(expressions)} rendered expressions, {len(bib)} references')


if __name__=='__main__':
    generate()
