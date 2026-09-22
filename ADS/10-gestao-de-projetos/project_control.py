from __future__ import annotations
import argparse,json
from dataclasses import dataclass,asdict
from pathlib import Path
class ProjectRuleError(ValueError): pass
@dataclass(frozen=True)
class Task:
 id:str; duration:float; deps:tuple[str,...]=()
 def __post_init__(self):
  if not self.id or self.duration<=0: raise ProjectRuleError('id e duração válidos são obrigatórios')
@dataclass(frozen=True)
class Schedule:
 id:str; es:float; ef:float; ls:float; lf:float; slack:float

def cpm(tasks:list[Task])->dict:
 ids={t.id for t in tasks}
 if len(ids)!=len(tasks): raise ProjectRuleError('ids duplicados')
 for t in tasks:
  missing=set(t.deps)-ids
  if missing: raise ProjectRuleError(f'predecessor ausente: {sorted(missing)}')
 succ={i:[] for i in ids}; indeg={i:0 for i in ids}
 for t in tasks:
  for d in t.deps: succ[d].append(t.id); indeg[t.id]+=1
 queue=[i for i,n in indeg.items() if n==0]; order=[]
 while queue:
  n=queue.pop(0); order.append(n)
  for s in succ[n]:
   indeg[s]-=1
   if indeg[s]==0: queue.append(s)
 if len(order)!=len(tasks): raise ProjectRuleError('ciclo detectado no grafo de dependências')
 by={t.id:t for t in tasks}; es={}; ef={}
 for n in order:
  es[n]=max((ef[d] for d in by[n].deps),default=0); ef[n]=es[n]+by[n].duration
 project_end=max(ef.values(),default=0); lf={n:project_end for n in ids}; ls={}
 for n in reversed(order):
  if succ[n]: lf[n]=min(ls[s] for s in succ[n])
  ls[n]=lf[n]-by[n].duration
 result=[Schedule(n,es[n],ef[n],ls[n],lf[n],ls[n]-es[n]) for n in order]
 return {'tasks':[asdict(x) for x in result],'project_duration':project_end,'critical_path':[x.id for x in result if abs(x.slack)<1e-9]}

def evm(pv:float,ev:float,ac:float,bac:float)->dict:
 if min(pv,ev,ac,bac)<0: raise ProjectRuleError('valores EVM não podem ser negativos')
 if bac==0: raise ProjectRuleError('BAC deve ser positivo')
 cpi=ev/ac if ac else None; spi=ev/pv if pv else None
 eac=bac/cpi if cpi else None; etc=eac-ac if eac is not None else None
 return {'PV':pv,'EV':ev,'AC':ac,'BAC':bac,'CV':ev-ac,'SV':ev-pv,'CPI':cpi,'SPI':spi,'EAC':eac,'ETC':etc,'VAC':bac-eac if eac is not None else None}
def load(path:Path):
 raw=json.loads(path.read_text(encoding='utf8')); return [Task(x['id'],float(x['duration']),tuple(x.get('deps',[]))) for x in raw['tasks']],raw['evm']
def main():
 p=argparse.ArgumentParser(); p.add_argument('--input',type=Path,required=True); p.add_argument('--output',type=Path,required=True); a=p.parse_args(); tasks,data=load(a.input); result={'cpm':cpm(tasks),'evm':evm(**data)}; a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8'); print(json.dumps(result,ensure_ascii=False))
if __name__=='__main__': main()
