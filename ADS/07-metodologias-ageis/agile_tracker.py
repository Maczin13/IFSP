from __future__ import annotations
import argparse, csv, json
from dataclasses import dataclass, asdict
from datetime import date
from enum import Enum
from pathlib import Path

class AgileRuleError(ValueError): pass
class Status(str, Enum): TODO='Todo'; IN_PROGRESS='In Progress'; DONE='Done'
@dataclass
class WorkItem:
    id:str; title:str; points:int; status:Status=Status.TODO
    created_at:date|None=None; started_at:date|None=None; done_at:date|None=None
    def __post_init__(self):
        if not self.id.strip() or not self.title.strip(): raise AgileRuleError('id e título são obrigatórios')
        if not isinstance(self.points,int) or isinstance(self.points,bool) or self.points<=0: raise AgileRuleError('pontos devem ser inteiros positivos')
        if self.status==Status.DONE and not self.done_at: raise AgileRuleError('item Done exige done_at')
        if self.started_at and self.created_at and self.started_at<self.created_at: raise AgileRuleError('started_at anterior à criação')
        if self.done_at and self.started_at and self.done_at<self.started_at: raise AgileRuleError('done_at anterior ao início')
    def lead_time(self)->int|None: return (self.done_at-self.created_at).days if self.done_at and self.created_at else None
    def cycle_time(self)->int|None: return (self.done_at-self.started_at).days if self.done_at and self.started_at else None
    def transition(self,status:Status,when:date):
        if status==Status.IN_PROGRESS and self.status==Status.TODO: self.started_at=when
        if status==Status.DONE:
            if self.status==Status.TODO: self.started_at=self.created_at or when
            self.done_at=when
        self.status=status

class AgileTracker:
    def __init__(self,items:list[WorkItem],wip_limit:int|None=None):
        if wip_limit is not None and wip_limit<=0: raise AgileRuleError('wip_limit inválido')
        self.items=items; self.wip_limit=wip_limit
    def get(self,item_id):
        for i in self.items:
            if i.id==item_id:return i
        raise AgileRuleError(f'item inexistente: {item_id}')
    def transition(self,item_id,status:Status,when:date):
        item=self.get(item_id)
        active=sum(x.status==Status.IN_PROGRESS for x in self.items)
        if status==Status.IN_PROGRESS and item.status!=Status.IN_PROGRESS and self.wip_limit is not None and active>=self.wip_limit: raise AgileRuleError('limite WIP excedido')
        if item.status==Status.DONE: raise AgileRuleError('item concluído não pode retroceder')
        item.transition(status,when)
    def filter(self,status:Status|None=None): return [x for x in self.items if status is None or x.status==status]
    def velocity(self,period_start:date,period_end:date)->int:
        return sum(x.points for x in self.items if x.status==Status.DONE and x.done_at and period_start<=x.done_at<=period_end)
    def metrics(self):
        lead=[x.lead_time() for x in self.items if x.lead_time() is not None]; cycle=[x.cycle_time() for x in self.items if x.cycle_time() is not None]
        avg=lambda xs: round(sum(xs)/len(xs),2) if xs else None
        return {'total_items':len(self.items),'by_status':{s.value:len(self.filter(s)) for s in Status},'completed_points':sum(x.points for x in self.items if x.status==Status.DONE),'average_lead_time_days':avg(lead),'average_cycle_time_days':avg(cycle),'wip_limit':self.wip_limit}

def parse_date(v): return date.fromisoformat(v) if v else None
def load_csv(path:Path):
 out=[]
 for r in csv.DictReader(path.open(encoding='utf8')):
  out.append(WorkItem(r['id'],r['title'],int(r['points']),Status(r['status']),parse_date(r.get('created_at')),parse_date(r.get('started_at')),parse_date(r.get('done_at'))))
 return out
def main():
 p=argparse.ArgumentParser(); p.add_argument('--input',type=Path,required=True); p.add_argument('--start',default='2026-09-01'); p.add_argument('--end',default='2026-09-30'); p.add_argument('--wip',type=int,default=3); p.add_argument('--output',type=Path,required=True); a=p.parse_args()
 t=AgileTracker(load_csv(a.input),a.wip); result={'metrics':t.metrics(),'velocity':t.velocity(date.fromisoformat(a.start),date.fromisoformat(a.end)),'done':[asdict(x) | {'status':x.status.value} for x in t.filter(Status.DONE)]}; a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(result,default=str,ensure_ascii=False,indent=2),encoding='utf8'); print(json.dumps(result,default=str,ensure_ascii=False))
if __name__=='__main__': main()
