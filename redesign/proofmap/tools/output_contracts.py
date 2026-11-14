"""출력 항목 참조, 내용 확장, 검토 지문. 수학적 함의 판정은 하지 않는다."""
import copy
import hashlib
import json


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def output_entry(doc, ref):
    g = next(g for g in doc['graphs'] if g['id'] == ref['graph'])
    n = next(n for n in g['nodes'] if n['id'] == ref['node'])
    raw=n['outputs'][ref['output']]
    if 'clauses' not in raw:
        return raw
    entry=copy.deepcopy(raw)
    if 'clauses' in entry:
        selected=ref.get('clauses',list(entry['clauses']))
        if not selected or len(selected)!=len(set(selected)) or any(k not in entry['clauses'] for k in selected):
            raise ValueError('선택한 입력 항목 없음 또는 중복')
        entry['statement']='\n\n'.join(entry['clauses'][k]['statement'] for k in selected)
        entry['defines']=sorted({s for k in selected for s in entry['clauses'][k].get('defines',[])})
        entry['bindings']={s:v for k in selected for s,v in entry['clauses'][k].get('bindings',{}).items()}
        entry['selected_clauses']=selected
    return entry


def contains_ref(doc, offered, requested):
    if not offered or any(offered.get(k)!=requested.get(k) for k in ['graph','node','output']):
        return False
    a,b=output_entry(doc,offered),output_entry(doc,requested)
    return set(b.get('selected_clauses',[]))<=set(a.get('selected_clauses',[]))


def proof_snapshot(doc, proof):
    """증명 graph의 의미 관련 자료와 하위 graph를 해시한다. 배치는 제외한다."""
    gathered, visited = [], set()
    fields = {'id','kind','status','inputs','statement','statement_ref','conditions','derivation','produces',
              'subgraph','external_ref','inherit_statement','local_context','floor_used','input_ports',
              'import_edge','introductions','requires_bindings'}
    def math_node(n):
        value={k:v for k,v in n.items() if k in fields}
        if 'input_ports' in value:
            # 검토 지문 자체는 명제가 아니다. 출력으로 되돌아오는 참조에도
            # hash(hash(...)) 고정점을 만들지 않도록 요구 항목만 기록한다.
            value['input_ports']={name:{k:v for k,v in port.items() if k!='reviewed_fingerprint'}
                                  for name,port in value['input_ports'].items()}
        return value
    def math_edge(e):
        value={k:v for k,v in e.items() if k not in {'label','summary','layout','in_complete_vertex'}}
        if e.get('output_ref'):
            value['resolved_payload']=payload(output_entry(doc,e['output_ref']))
        return value
    def source_math(gid, nid, seen=None):
        seen=set() if seen is None else seen
        if (gid,nid) in seen:
            return {'cycle':[gid,nid]}
        seen.add((gid,nid))
        g=next(g for g in doc['graphs'] if g['id']==gid)
        n=next(n for n in g['nodes'] if n['id']==nid)
        value=math_node(n)
        if n.get('statement_ref'):
            value['resolved_payload']=payload(output_entry(doc,n['statement_ref']))
        if n.get('inherit_statement') and g.get('parent'):
            ref=n.get('external_ref') if n['kind']=='external' else g['parent']['node']
            value['inherited_source']=source_math(g['parent']['graph'],ref,seen)
        return value
    def visit(gid):
        if gid in visited:
            return
        visited.add(gid)
        g = next(g for g in doc['graphs'] if g['id'] == gid)
        item={'id':gid,'contexts':g.get('contexts',[]),'premise_mode':g.get('premise_mode'),
                         'nodes':[math_node(n) for n in g['nodes']],
                         'edges':[math_edge(e) for e in g['edges']]}
        # 하위 증명의 바깥 입력도 의미 의존성이다. 출력 소유자의
        # outputs/input_ports/검토 지문은 넣지 않아 자기 지문 순환을 피한다.
        if g.get('parent'):
            pg=next(pg for pg in doc['graphs'] if pg['id']==g['parent']['graph'])
            pn=next(pn for pn in pg['nodes'] if pn['id']==g['parent']['node'])
            incoming=[math_edge(e) for e in pg['edges'] if e['to']==pn['id']]
            item['boundary']={'graph':pg['id'],'node':pn['id'],'inputs':pn.get('inputs',[]),
                              'edges':incoming,
                              'sources':[source_math(pg['id'],nid) for nid in pn.get('inputs',[])],
                              'contexts':[c for c in pg.get('contexts',[]) if pn['id'] in c['nodes']]}
        gathered.append(item)
        for n in g['nodes']:
            if n.get('subgraph'):
                visit(n['subgraph'])
    visit(proof['graph'])
    g = next(g for g in doc['graphs'] if g['id']==proof['graph'])
    if not any(n['id']==proof['node'] for n in g['nodes']):
        raise ValueError('proof node 없음')
    return gathered


def payload(entry):
    return {k:entry.get(k, [] if k in ['conditions','defines'] else {}) if k in ['conditions','defines','bindings']
            else entry.get(k,'') for k in ['statement','conditions','grounding','defines','bindings']}


def fingerprint(doc, ref):
    entry = output_entry(doc,ref)
    return digest({'payload':payload(entry), 'proof':None if entry.get('role')=='given' else proof_snapshot(doc,entry['proof'])})


def contract_audit(doc):
    """각 검토 상태를 반환한다. metadata를 새로 승인하거나 갱신하지 않는다."""
    node_issues, edge_issues, outputs = {}, {}, {}
    def add(table,key,msg):
        table.setdefault(key,[]).append(msg)
    for g in doc['graphs']:
        nodes={n['id']:n for n in g['nodes']}
        strict=g.get('premise_mode')=='edges_only'
        if strict and g.get('contexts'):
            for n in g['nodes']:
                add(node_issues,(g['id'],n['id']),'edge 전용 graph에 context 전제가 추가됨')
        for n in g['nodes']:
            if strict:
                for field in ['local_context','conditions']:
                    if n.get(field):add(node_issues,(g['id'],n['id']),f'부모 입력으로 추적되지 않는 {field} 추가')
                if n['kind']=='external':
                    try:
                        pg=next(pg for pg in doc['graphs'] if pg['id']==g['parent']['graph'])
                        pe=next(e for e in pg['edges'] if e['id']==n['import_edge'] and e['to']==g['parent']['node'] and e['from']==n['external_ref'])
                        if not contains_ref(doc,pe.get('output_ref'),n['statement_ref']):
                            add(node_issues,(g['id'],n['id']),'부모 입력이 공급하지 않은 항목의 projection')
                    except (KeyError,StopIteration,ValueError,TypeError):
                        add(node_issues,(g['id'],n['id']),'부모 입력 edge에서 추적할 수 없는 외부 전제')
                provided={}
                for edge in g['edges']:
                    if edge['to']==n['id'] and edge.get('output_ref'):
                        try:
                            for symbol,binding in output_entry(doc,edge['output_ref']).get('bindings',{}).items():
                                provided.setdefault(symbol,set()).add(binding)
                        except (KeyError,StopIteration,ValueError,TypeError):pass
                for symbol,required in n.get('requires_bindings',{}).items():
                    if provided.get(symbol)!={required}:
                        add(node_issues,(g['id'],n['id']),f'기호 {symbol}의 binding 공급 불일치')
                for intro in n.get('introductions',[]):
                    allowed={'id','kind','symbol','expr','uses_symbols','scope'} if intro.get('kind')=='notation' else {'id','kind','symbol','domain','uses_symbols','scope'}
                    if intro.get('kind') not in ['notation','arbitrary_index'] or set(intro)-allowed:
                        add(node_issues,(g['id'],n['id']),'로컬 도입에 새 가정 또는 허용하지 않은 필드 추가')
                    if intro.get('scope')!=f"{g['id']}.{n['id']}.{intro.get('symbol')}":
                        add(node_issues,(g['id'],n['id']),'로컬 도입의 binding scope 불일치')
                    if intro.get('symbol') in provided:
                        add(node_issues,(g['id'],n['id']),'로컬 도입이 공급된 기호를 덮어씀')
                scopes={i.get('scope') for i in n.get('introductions',[]) if i.get('kind')=='arbitrary_index'}
                for produced in n.get('produces',[]):
                    e=next((e for e in g['edges'] if e['id']==produced.get('edge')),None)
                    if e and e['from']!=e['to'] and scopes-set(produced.get('generalizes',[])):
                        add(node_issues,(g['id'],n['id']),'출력에서 로컬 지표 범위를 닫지 않음')
                for e in g['edges']:
                    if e['from']==e['to']==n['id'] and e.get('loop',{}).get('index_scope') not in scopes:
                        add(node_issues,(g['id'],n['id']),'귀납 edge와 로컬 지표의 범위가 다름')
            if 'statement_ref' in n:
                try:
                    output_entry(doc,n['statement_ref'])
                    if 'statement' in n:
                        add(node_issues,(g['id'],n['id']),'진술 참조와 독립 statement가 중복됨')
                except (KeyError,StopIteration,ValueError,TypeError):
                    add(node_issues,(g['id'],n['id']),'진술 참조의 요구 출력 없음')
            for name,entry in n.get('outputs',{}).items():
                ref={'graph':g['id'],'node':n['id'],'output':name}
                key=(g['id'],n['id'],name)
                issues=[]
                try:
                    if entry.get('role')=='given':
                        if strict:add(node_issues,(g['id'],n['id']),'자식 graph에 새 given 전제를 만들 수 없음')
                        outputs[key]={'fingerprint':fingerprint(doc,ref),'issues':[]}
                        continue
                    proof_hash=digest(proof_snapshot(doc,entry['proof']))
                    review=entry.get('proof_review',{})
                    if review.get('output_fingerprint') != digest(payload(entry)):
                        issues.append('출력'+' 변경 후 유도 재검토 필요')
                    if review.get('proof_fingerprint') != proof_hash:
                        issues.append('내부 증명 변경 후 출력 대응 재검토 필요')
                    outputs[key]={'fingerprint':fingerprint(doc,ref),'issues':issues}
                except (KeyError,StopIteration,ValueError,TypeError):
                    issues.append('출력 유도 참조를 찾을 수 없음')
                    outputs[key]={'fingerprint':None,'issues':issues}
                for msg in issues:add(node_issues,(g['id'],n['id']),f'출력 {name}: {msg}')
        for e in g['edges']:
            if 'output_ref' not in e:
                continue
            ek=(g['id'],e['id'])
            try:
                ref=e['output_ref'];entry=output_entry(doc,ref)
                src=nodes[e['from']]
                origin={'graph':g['id'],'node':src['id'],'output':ref['output']}
                inherited=(src.get('inherit_statement') and g.get('parent') and
                           ref['graph']==g['parent']['graph'] and ref['node']==src.get('external_ref'))
                if ref!=origin and not contains_ref(doc,src.get('statement_ref'),ref) and not inherited:
                    add(edge_issues,ek,'보낸 node가 선언하지 않은 출력 참조')
                if 'statement' in e:
                    add(edge_issues,ek,'출력 참조 edge에 독립 statement가 중복됨')
                target=nodes[e['to']]
                ports=[p for p in target.get('input_ports',{}).values() if p.get('edge')==e['id']]
                if not ports:add(edge_issues,ek,'받는 입력의 검토 기록 없음')
                for port in ports:
                    if port.get('requires')!=ref:
                        add(edge_issues,ek,'수신 요구 출력과 전달 출력 불일치')
                    elif port.get('reviewed_fingerprint')!=fingerprint(doc,ref):
                        add(edge_issues,ek,'출력·조건·증명 변경 후 수신 재검토 필요')
            except (KeyError,StopIteration,ValueError,TypeError):
                add(edge_issues,ek,'요구 출력 또는 유도 참조 없음')
        for n in g['nodes']:
            for name,port in n.get('input_ports',{}).items():
                e=next((e for e in g['edges'] if e['id']==port.get('edge') and e['to']==n['id']),None)
                if e is None:
                    add(node_issues,(g['id'],n['id']),f'입력 port {name}: 연결 edge 없음')
                elif e.get('output_ref')!=port.get('requires'):
                    add(edge_issues,(g['id'],e['id']),f'입력 port {name}: 요구 출력 없음 또는 불일치')
    # 출력 자체의 검토 상태를 그 출력을 쓰는 edge로 전달한다.
    for g in doc['graphs']:
        for e in g['edges']:
            ref=e.get('output_ref')
            if ref:
                record=outputs.get((ref.get('graph'),ref.get('node'),ref.get('output')), {})
                for issue in record.get('issues',[]):add(edge_issues,(g['id'],e['id']),issue)
            for issue in edge_issues.get((g['id'],e['id']),[]):
                for nid in [e['from'],e['to']]:add(node_issues,(g['id'],nid),f"edge {e['id']}: {issue}")
        # 사용처의 뒤쪽은 보수적으로 재검토 대상으로 표시한다. 내용은 자동 수정하지 않는다.
        queue=[n['id'] for n in g['nodes'] if (g['id'],n['id']) in node_issues]
        seen=set(queue)
        while queue:
            current=queue.pop(0)
            for edge in g['edges']:
                if edge['from']==current and edge['to'] not in seen:
                    seen.add(edge['to']);queue.append(edge['to'])
                    add(node_issues,(g['id'],edge['to']),f"상류 {current}의 출력 대응 변경 후 재검토 필요")
    return {'nodes':node_issues,'edges':edge_issues,'outputs':outputs}


def resolve_document(doc):
    """단독 HTML/export에는 참조한 진술과 조건 전체를 싣는다. 원본은 변경하지 않는다."""
    resolved=copy.deepcopy(doc)
    for g in resolved['graphs']:
        for n in g['nodes']:
            if 'statement_ref' in n:
                try:
                    entry=output_entry(doc,n['statement_ref']);n['statement']=entry['statement'];n['conditions']=entry.get('conditions',[])
                    n['imported_defines']=entry.get('defines',[])
                    n['imported_bindings']=entry.get('bindings',{})
                except (KeyError,StopIteration,ValueError,TypeError):n['statement']='[요구 출력 없음]'
        for e in g['edges']:
            if 'output_ref' in e:
                try:
                    entry=output_entry(doc,e['output_ref'])
                    conditions=' '.join(entry.get('conditions',[]))
                    e['statement']=entry['statement']+('\n\n성립 조건: '+conditions if conditions else '')
                    e['defines']=entry.get('defines',e.get('defines',[]))
                    e['bindings']=entry.get('bindings',{})
                except (KeyError,StopIteration,ValueError,TypeError):e['statement']='[요구 출력 없음]'
    return resolved
