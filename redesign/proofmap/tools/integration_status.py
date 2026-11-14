"""전제 변환 범위, 참조 연결, 기존 본문 및 중복을 별도 축으로 표시한다."""
from itertools import combinations


def integration_status(doc, contracts, bindings=None):
    bindings=contracts.contract_audit(doc) if bindings is None else bindings
    graphs={g['id']:g for g in doc['graphs']}
    nodes={};maps={}
    def owner(ref):
        g=graphs[ref['graph']]
        return next(n for n in g['nodes'] if n['id']==ref['node'])
    def ref_items(ref):
        entry=contracts.output_entry(doc,ref)
        return entry.get('selected_clauses',[ref['output']])
    def names(ref):
        raw=owner(ref)['outputs'][ref['output']]
        return [raw.get('clauses',{}).get(k,{}).get('title',k) for k in ref_items(ref)]
    for gid,g in graphs.items():
        strict=g.get('premise_mode')=='edges_only'
        imports=[];legacy_bodies=[];overlaps=[]
        for n in g['nodes']:
            data={'imports':None,'overlaps':[],'pending':[],'forwarded':[],
                  'bodyMode':'reference' if n.get('statement_ref') else 'inherited' if n.get('inherit_statement') else 'independent'}
            if n.get('statement') and any(o.get('role')=='given' for o in n.get('outputs',{}).values()):
                data['pending'].append('기존 전체 본문과 이름 붙은 입력 항목의 의미 대응 미검토')
                legacy_bodies.append(n['id'])
            for e in g['edges']:
                if e['from']!=n['id'] or not e.get('output_ref'):continue
                ref=e['output_ref']
                try:
                    data['forwarded'].append({'edge':e['id'],'ref':ref,'items':names(ref)})
                except (KeyError,StopIteration,ValueError,TypeError):pass
            if n.get('inherit_statement') and data['forwarded']:
                data['pending'].append('전달 출력은 항목 참조 적용; 상속한 전체 본문은 별도 저장 상태')
                legacy_bodies.append(n['id'])
            if g.get('parent') and n['kind']=='external':
                record={'node':n['id'],'tracked':bool(n.get('import_edge') and n.get('statement_ref')),
                        'matched':False,'parentGraph':g['parent']['graph'],'parentEdge':n.get('import_edge'),
                        'items':[],'issues':[],'upstreamPending':[]}
                if record['tracked']:
                    try:
                        pg=graphs[g['parent']['graph']]
                        pe=next(e for e in pg['edges'] if e['id']==n['import_edge'] and e['to']==g['parent']['node'] and e['from']==n['external_ref'])
                        record['matched']=contracts.contains_ref(doc,pe.get('output_ref'),n['statement_ref'])
                        record['items']=names(n['statement_ref'])
                        src=owner(n['statement_ref'])
                        if src.get('statement') and any(o.get('role')=='given' for o in src.get('outputs',{}).values()):
                            record['upstreamPending'].append(n['statement_ref']['graph']+'/'+src['id']+': 기존 전체 본문 대응 미검토')
                    except (KeyError,StopIteration,ValueError,TypeError):pass
                record['issues']=bindings['nodes'].get((gid,n['id']),[])
                imports.append(record);data['imports']=record
                if not record['tracked']:data['pending'].append('외부 입력–부모 입력의 항목 참조 미적용')
                elif not record['matched']:data['pending'].append('부모 입력 edge와 선택 항목의 참조 충돌')
            nodes[(gid,n['id'])]=data
        external=[n for n in g['nodes'] if n['kind']=='external' and n.get('statement_ref')]
        for a,b in combinations(external,2):
            ra,rb=a['statement_ref'],b['statement_ref']
            if any(ra.get(k)!=rb.get(k) for k in ['graph','node','output']):continue
            try:shared=sorted(set(ref_items(ra))&set(ref_items(rb)))
            except (KeyError,StopIteration,ValueError,TypeError):continue
            if shared:
                item={'left':a['id'],'right':b['id'],'items':shared}
                overlaps.append(item)
                nodes[(gid,a['id'])]['overlaps'].append(item);nodes[(gid,b['id'])]['overlaps'].append(item)
        total=len(imports);tracked=sum(i['tracked'] for i in imports);matched=sum(i['matched'] for i in imports)
        maps[gid]={'mode':'edge 전용 적용' if strict else '기존 전제 모델 · 미변환',
                   'referenceEdges':sum(bool(e.get('output_ref')) for e in g['edges']),
                   'totalEdges':len(g['edges']),'imports':imports,'tracked':tracked,'matched':matched,'totalImports':total,
                   'overlaps':overlaps,'legacyBodies':legacy_bodies,
                   'plainEdges':[e['id'] for e in g['edges'] if not e.get('output_ref')],
                   'reviewEdges':[e['id'] for e in g['edges'] if bindings['edges'].get((gid,e['id']))],
                   'pendingUpstream':sorted({s for i in imports for s in i['upstreamPending']}),
                   'stage':'부분 적용' if not strict or tracked!=total or matched!=total or overlaps or legacy_bodies else '전제 경로 적용 완료'}
    return {'graphs':maps,'nodes':nodes}
