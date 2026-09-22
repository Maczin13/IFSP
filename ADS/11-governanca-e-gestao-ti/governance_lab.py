from __future__ import annotations
import argparse,csv,json
from dataclasses import dataclass,asdict
from pathlib import Path
class GovernanceRuleError(ValueError): pass
@dataclass(frozen=True)
class Control:
 id:str; objective:str; framework:str; owner:str; evidence:str; status:str; effectiveness:int
 def __post_init__(self):
  if not self.id or not self.objective or not self.owner: raise GovernanceRuleError('identificação, objetivo e proprietário são obrigatórios')
  if self.framework not in {'COBIT-EDM','COBIT-APO','ITIL4'}: raise GovernanceRuleError('framework não suportado')
  if self.status not in {'implemented','partial','missing'}: raise GovernanceRuleError('status inválido')
  if not 0<=self.effectiveness<=5: raise GovernanceRuleError('efetividade deve estar entre 0 e 5')
 def result(self): return 'PASS' if self.status=='implemented' and self.evidence and self.effectiveness>=3 else 'FAIL'
 def maturity(self): return {'missing':0,'partial':2,'implemented':5}[self.status] if self.result()=='PASS' else min(self.effectiveness,2)
class GovernanceAudit:
 def __init__(self,controls:list[Control]):
  if not controls: raise GovernanceRuleError('matriz vazia')
  self.controls=controls
 def assess(self):
  rows=[]
  for c in self.controls: rows.append(asdict(c)|{'result':c.result(),'maturity':c.maturity()})
  return rows
 def summary(self):
  rows=self.assess(); by={f:sum(c.framework==f for c in self.controls) for f in {'COBIT-EDM','COBIT-APO','ITIL4'}}; passed=sum(r['result']=='PASS' for r in rows); score=round(sum(r['maturity'] for r in rows)/(len(rows)*5)*5,2)
  return {'total_controls':len(rows),'passed':passed,'failed':len(rows)-passed,'pass_rate':round(passed/len(rows),3),'maturity_level_0_to_5':score,'by_framework':by}
def load(path:Path):
 out=[]
 for r in csv.DictReader(path.open(encoding='utf8')): out.append(Control(r['id'],r['objective'],r['framework'],r['owner'],r['evidence'],r['status'],int(r['effectiveness'])))
 return out
def main():
 p=argparse.ArgumentParser(); p.add_argument('--input',type=Path,required=True); p.add_argument('--output',type=Path,required=True); a=p.parse_args(); audit=GovernanceAudit(load(a.input)); result={'summary':audit.summary(),'controls':audit.assess()}; a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8'); print(json.dumps(result,ensure_ascii=False))
if __name__=='__main__': main()
