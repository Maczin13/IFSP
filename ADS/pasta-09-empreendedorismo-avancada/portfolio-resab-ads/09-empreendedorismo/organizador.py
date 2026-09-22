from __future__ import annotations
import argparse,csv,json
from dataclasses import dataclass,asdict
from pathlib import Path
from enum import Enum
class ProductRuleError(ValueError): pass
AgileRuleError=ProductRuleError
class HypothesisStatus(str,Enum): UNTESTED='untested'; TESTING='testing'; VALIDATED='validated'; INVALIDATED='invalidated'
@dataclass
class Initiative:
 id:str; title:str; reach:float; impact:float; confidence:float; effort:float; cost_hours:float; expected_value:float; status:HypothesisStatus=HypothesisStatus.UNTESTED
 def __post_init__(self):
  if not self.id or not self.title: raise ProductRuleError('id e título obrigatórios')
  if self.reach<0 or self.impact<0 or not 0<=self.confidence<=1 or self.effort<=0 or self.cost_hours<=0 or self.expected_value<0: raise ProductRuleError('parâmetros fora do domínio')
 def rice(self): return self.reach*self.impact*self.confidence/self.effort
 def wsfj(self,cost_of_delay:float=0):
  if cost_of_delay<0: raise ProductRuleError('cost_of_delay inválido')
  return (cost_of_delay+self.impact)/self.effort
 def roi_time(self): return self.expected_value/self.cost_hours
@dataclass
class Evidence:
 hypothesis_id:str; metric:str; target:float; observed:float; sample_size:int; status:HypothesisStatus
 def __post_init__(self):
  if self.sample_size<=0: raise ProductRuleError('sample_size deve ser positivo')
 def outcome(self): return 'validated' if self.observed>=self.target else 'invalidated'
class MVPPlanner:
 def __init__(self,items:list[Initiative]): self.items=items
 def rank(self,method='rice'):
  if method not in {'rice','wsfj','roi'}: raise ProductRuleError('método inválido')
  key={'rice':lambda x:x.rice(),'wsfj':lambda x:x.wsfj(x.impact),'roi':lambda x:x.roi_time()}[method]
  return sorted(self.items,key=key,reverse=True)
 def portfolio(self,hours):
  if hours<=0: raise ProductRuleError('horas devem ser positivas')
  selected=[]; used=0
  for item in self.rank('rice'):
   if used+item.cost_hours<=hours: selected.append(item); used+=item.cost_hours
  return selected,used
 def traction(self):
  total=len(self.items); validated=sum(x.status==HypothesisStatus.VALIDATED for x in self.items); testing=sum(x.status==HypothesisStatus.TESTING for x in self.items)
  return {'total_initiatives':total,'validated_hypotheses':validated,'testing_hypotheses':testing,'validation_rate':round(validated/total,3) if total else 0}
def load(path:Path):
 out=[]
 for r in csv.DictReader(path.open(encoding='utf8')): out.append(Initiative(r['id'],r['title'],float(r['reach']),float(r['impact']),float(r['confidence']),float(r['effort']),float(r['cost_hours']),float(r['expected_value']),HypothesisStatus(r.get('status','untested'))))
 return out
def main():
 p=argparse.ArgumentParser(); p.add_argument('--input',type=Path,required=True); p.add_argument('--hours',type=float,required=True); p.add_argument('--output',type=Path,required=True); a=p.parse_args(); planner=MVPPlanner(load(a.input)); ranked=[asdict(x)|{'rice':round(x.rice(),2),'wsfj':round(x.wsfj(x.impact),2),'roi_time':round(x.roi_time(),2)} for x in planner.rank()]; selected,used=planner.portfolio(a.hours); result={'ranked':ranked,'portfolio':[x.id for x in selected],'hours_used':used,'traction':planner.traction()}; a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(result,default=str,ensure_ascii=False,indent=2),encoding='utf8'); print(json.dumps(result,default=str,ensure_ascii=False))
if __name__=='__main__': main()
