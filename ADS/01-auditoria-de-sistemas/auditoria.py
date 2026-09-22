import argparse,csv,hashlib,json,ipaddress,sys
from collections import defaultdict
from datetime import datetime,timezone
from pathlib import Path
REQ={'event_id','timestamp','user','ip','role','event','result','approval_id'}

def digest(p):
 h=hashlib.sha256(); h.update(Path(p).read_bytes()); return h.hexdigest()
def audit(path,window=5):
 rows=[]; errors=[]
 with open(path,encoding='utf8',newline='') as fh:
  r=csv.DictReader(fh)
  if set(r.fieldnames or [])!=REQ: raise ValueError('schema invalido')
  for n,row in enumerate(r,2):
   try:
    dt=datetime.fromisoformat(row['timestamp'].replace('Z','+00:00')).astimezone(timezone.utc)
    ipaddress.ip_address(row['ip'])
    if row['result'] not in {'success','failed'}: raise ValueError('result')
    row['_dt']=dt; rows.append(row)
   except Exception as e: errors.append({'line':n,'error':str(e)})
 findings=[]
 for row in rows:
  h=row['_dt'].hour
  if h<6 or h>=22: findings.append({'type':'out_of_hours','event_id':row['event_id'],'severity':'medium','evidence':[row['event_id']]})
  if row['event'] in {'delete_user','update_role','export'} and (row['role']=='admin') and not row['approval_id']:
   findings.append({'type':'sensitive_without_approval','event_id':row['event_id'],'severity':'high','evidence':[row['event_id']]})
 groups=defaultdict(list)
 for row in rows:
  if row['event']=='login' and row['result']=='failed': groups[(row['user'],row['ip'])].append(row)
 for (user,ip),evs in groups.items():
  evs.sort(key=lambda x:x['_dt'])
  for i in range(len(evs)-2):
   span=(evs[i+2]['_dt']-evs[i]['_dt']).total_seconds()/60
   if span<=window:
    findings.append({'type':'brute_force_indication','user':user,'ip':ip,'severity':'high','attempts':3,'evidence':[e['event_id'] for e in evs[i:i+3]]}); break
 return rows,findings,errors
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--input',default='access_logs.csv'); ap.add_argument('--output',default='results/run'); ap.add_argument('--window',type=int,default=5); ap.add_argument('--expected-sha256'); a=ap.parse_args()
 actual=digest(a.input)
 if a.expected_sha256 and actual!=a.expected_sha256: print('hash divergente',file=sys.stderr); return 2
 rows,findings,errors=audit(a.input,a.window); out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True)
 clean=[{k:v for k,v in x.items() if not k.startswith('_')} for x in rows]
 summary={'records':len(rows),'invalid':len(errors),'findings':len(findings),'sha256':actual,'finding_types':{t:sum(x['type']==t for x in findings) for t in sorted({x['type'] for x in findings})}}
 (out.with_suffix('.json')).write_text(json.dumps({'findings':findings,'errors':errors},indent=2),encoding='utf8')
 (out.parent/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf8')
 print(json.dumps(summary,sort_keys=True)); return 1 if errors else 0
if __name__=='__main__': sys.exit(main())
