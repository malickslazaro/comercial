#!/usr/bin/env python3
"""WTG commercial renderer. Private input, public-only rendering."""
import argparse,json,html,re,shutil,os,hashlib,hmac,base64,time,secrets,urllib.request
from decimal import Decimal,ROUND_HALF_UP
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def esc(v):return html.escape(str(v),quote=True)
def money(v):return f'{Decimal(v):,.2f}'.replace(',','X').replace('.',',').replace('X','.')+' €'
def url(v):
 from urllib.parse import urlsplit
 u=urlsplit(v)
 if u.scheme!='https' or not u.hostname or u.username or u.password:raise ValueError('El CTA debe ser una URL HTTPS válida')
 return esc(v)
def build(source,out):
 d=json.loads(Path(source).read_text());p=d['public'];cid=d['id'];out=Path(out).resolve()
 if not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',cid):raise ValueError('ID de cliente no válido')
 if out.exists() and any(out.iterdir()):raise ValueError('La carpeta de salida debe estar vacía; conserva la versión anterior')
 if out==ROOT or ROOT in out.parents and 'dist' not in out.relative_to(ROOT).parts:raise ValueError('Genera dentro de dist/ o fuera del repo')
 design=p.get('design','wtg')
 if design not in ['wtg','ujo','audidat','suderow']:raise ValueError('Diseño desconocido')
 rate=Decimal(p.get('vatRate','21'))
 if not rate.is_finite() or rate<0 or rate>100:raise ValueError('IVA no válido')
 options='';budget=''
 for op in p.get('options',[]):
  amount=Decimal(op['amount'])
  if not amount.is_finite() or amount<0:raise ValueError('Importe no válido')
  vat=(amount*rate/100).quantize(Decimal('.01'),rounding=ROUND_HALF_UP)
  items=''.join('<li>'+esc(x)+'</li>' for x in op.get('includes',[]))
  options+=f'<article><h3>{esc(op["name"])}</h3><p class="price">{money(amount)}</p><p>+ IVA ({esc(rate)} %)</p><ul>{items}</ul></article>'
  budget+=f'<article><h2>{esc(op["name"])}</h2><ul>{items}</ul><p>Base: {money(amount)} · IVA: {money(vat)} · Total: {money(amount+vat)}</p></article>'
 blocks=''
 for s in p.get('sections',[]):
  blocks+=f'<section class="section"><div class="wrap"><h2>{esc(s["title"])}</h2><p>{esc(s.get("text",""))}</p><ul>'+''.join('<li>'+esc(i)+'</li>' for i in s.get('items',[]))+'</ul></div></section>'
 faqs=''.join(f'<details><summary>{esc(f["question"])}</summary><p>{esc(f["answer"])}</p></details>' for f in p.get('faqs',[]))
 cta=f'<a class="btn" href="{url(p["cta"]["url"])}">{esc(p["cta"]["label"])} ↗</a>'
 css='''body{font-family:Helvetica,Arial,sans-serif;color:#151515;background:white;font-size:17px;line-height:1.6;margin:0}h1{font-size:clamp(32px,5vw,56px);line-height:1.1}h2,h3{font-size:26px;line-height:1.3}p,li,summary,a{font-size:17px}.wrap{width:min(1100px,calc(100% - 40px));margin:auto}.top-inner{display:flex;align-items:center;justify-content:space-between;padding:22px 0}.brand img{width:100px;height:auto}.hero,.section,.close{padding:64px 0}.section{border-bottom:1px solid #ddd}.compare{display:grid;grid-template-columns:1fr 1fr;gap:24px}.compare article{padding:28px;background:#f7f7fa;border:1px solid #ddd}.price{color:#4435ed;font-weight:bold;font-size:26px}.btn{display:inline-block;background:#4435ed;color:white;padding:14px 24px;text-decoration:none;border-radius:4px}.close{background:#17151d;color:white}details{padding:18px 0;border-bottom:1px solid #ddd}summary{cursor:pointer}a:focus-visible,summary:focus-visible{outline:3px solid #4435ed;outline-offset:4px}img{max-width:100%}article{break-inside:avoid}@media(max-width:700px){.compare{grid-template-columns:1fr}.hero,.section,.close{padding:40px 0}.top-inner{gap:20px;flex-wrap:wrap}}@media print{.top,.btn{display:none}.hero,.section,.close{padding:20px 0;background:white;color:#151515}}'''
 def shell(title,body):return f'<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{esc(title)}</title><link rel="icon" href="/favicon-wtg.svg"><link rel="stylesheet" href="/design.css"><style>{css}</style></head><body>{body}</body></html>'
 options_section=f'<section class="section" id="opciones"><div class="wrap"><h2>Opciones de colaboración</h2><div class="compare">{options}</div><p><a href="/presupuesto.html">Ver presupuesto imprimible ↗</a></p></div></section>' if options else ''
 page=f'<header class="top"><div class="wrap top-inner"><a class="brand" href="/"><img src="/assets/wtg.png" alt="WTG"></a><span>{esc(p["company"])}</span><a href="/cuestionario/">Cuestionario</a></div></header><main><section class="hero"><div class="wrap"><p>WTG × {esc(p["company"])}</p><h1>{esc(p["title"])}</h1><p>{esc(p.get("intro",""))}</p>{cta}</div></section>{blocks}{options_section}<section class="section"><div class="wrap"><h2>Preguntas frecuentes</h2>{faqs}</div></section><section class="close"><div class="wrap"><h2>Próximos pasos</h2><p>Confirmamos el alcance y acordamos el calendario de inicio.</p>{cta}</div></section></main>'
 out.mkdir(parents=True,exist_ok=True);shutil.copytree(ROOT/'marca',out/'assets');shutil.copy2(ROOT/'marca/favicon-wtg.svg',out/'favicon-wtg.svg');shutil.copy2(ROOT/f'plantillas/{design}.css',out/'design.css')
 (out/'index.html').write_text(shell(p['title'],page));(out/'presupuesto.html').write_text(shell('Presupuesto · '+p['company'],f'<main class="wrap"><h1>Presupuesto · {esc(p["company"])}</h1><p>Opciones alternativas; no se suman entre sí.</p>{budget}<button onclick="window.print()">Imprimir / Guardar PDF</button></main>'))
 q=ROOT/'cuestionarios/independiente';shutil.copytree(q,out/'cuestionario');(out/'api').mkdir();shutil.move(out/'cuestionario/service.mjs',out/'api/service.mjs');(out/'admin').mkdir()
 for a,b in [('admin.html','index.html'),('admin.css','admin.css'),('admin.mjs','admin.mjs')]:shutil.move(out/'cuestionario'/a,out/'admin'/b)
 schema=json.loads((q/'schema.json').read_text());schema.update(clientId=cid,storageKey='wtg-discovery-'+cid,subtitle='WTG · '+p['company'],prefill={})
 (out/'cuestionario/schema.json').write_text(json.dumps(schema,ensure_ascii=False))
 form=(out/'cuestionario/index.html').read_text().replace('Cliente',esc(p['company']));(out/'cuestionario/index.html').write_text(form)
 shutil.copy2(q/'visit.mjs',out/'visit.mjs')
 for file in [out/'index.html',out/'cuestionario/index.html']:
  file.write_text(file.read_text().replace('</body>','<script type="module" src="/visit.mjs"></script></body>'))
 (out/'package.json').write_text(json.dumps({'private':True,'type':'module','engines':{'node':'22.x'},'dependencies':{'@vercel/blob':'2.8.2'}}))
 (out/'vercel.json').write_text(json.dumps({'regions':['cdg1'],'functions':{'api/service.mjs':{'maxDuration':30}},'headers':[{'source':'/(.*)','headers':[{'key':'X-Robots-Tag','value':'noindex, nofollow'}]}]}))
 (out/'.vercelignore').write_text('.env*\nnode_modules\n.vercel\n')
 print('Web, presupuesto, cuestionario y administración generados:',out)
def monitor(origin,state,report):
 if not origin.startswith('https://'):raise ValueError('Origen HTTPS requerido')
 secret=os.environ['ADMIN_SESSION_SECRET'];encode=lambda v:base64.urlsafe_b64encode(v).rstrip(b'=').decode()
 p=encode(json.dumps({'exp':int(time.time())+300,'nonce':secrets.token_hex(16)}).encode());sig=encode(hmac.new(secret.encode(),('admin:'+p).encode(),hashlib.sha256).digest())
 req=urllib.request.Request(origin.rstrip('/')+'/api/service?op=activity',headers={'Cookie':'__Host-wtg_admin='+p+'.'+sig})
 with urllib.request.urlopen(req,timeout=35) as f:d=json.load(f)
 # activity API collections; preserve only event metadata in private state/report.
 old=json.loads(Path(state).read_text()) if Path(state).exists() else None
 openings=d.get('openings',[]);responses=d.get('responses',d.get('finalizations',[]))
 events=[{'id':'open:'+str(x['id'])+':'+x.get('page',''),'type':'apertura','page':x.get('page'),'at':x.get('at',x.get('openedAt'))} for x in openings if not x.get('internal')]
 events += [{'id':'final:'+str(x['id']),'type':'formulario_finalizado','at':x['finalizedAt']} for x in responses if x.get('finalizedAt')]
 seen=set(old or []);changes=[x for x in events if x['id'] not in seen] if old is not None else []
 for filename,value in [(state,[x['id'] for x in events]),(report,{'checkedAt':time.time(),'changes':changes})]:
  path=Path(filename);path.parent.mkdir(parents=True,exist_ok=True);tmp=path.with_suffix('.tmp');tmp.write_text(json.dumps(value,ensure_ascii=False));tmp.chmod(0o600);tmp.replace(path)
 print(json.dumps({'changes':changes},ensure_ascii=False))
if __name__=='__main__':
 a=argparse.ArgumentParser();s=a.add_subparsers(dest='cmd',required=True);b=s.add_parser('build');b.add_argument('source');b.add_argument('--out',required=True);m=s.add_parser('monitor');m.add_argument('--origin',required=True);m.add_argument('--state',required=True);m.add_argument('--report',required=True);n=a.parse_args()
 if n.cmd=='build':build(n.source,n.out)
 else:monitor(n.origin,n.state,n.report)
