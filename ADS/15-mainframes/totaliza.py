from __future__ import annotations
import argparse,json
from dataclasses import dataclass,asdict
from datetime import datetime
from pathlib import Path
class BatchRuleError(ValueError): pass
@dataclass(frozen=True)
class Record:
 transaction_id:str; date:str; amount_cents:int; status:str
 def to_fixed(self): return f'{self.transaction_id:<6}{self.date:>8}{self.amount_cents:012d}{self.status:<10}'
class Copybook:
 width=36
 def parse(self,line:str)->Record:
  raw=line.rstrip('\n\r')
  if len(raw)!=self.width: raise BatchRuleError(f'RECORD_LENGTH:{len(raw)}')
  tid=raw[0:6].strip(); date=raw[6:14]; amount=raw[14:26]; status=raw[26:36].strip()
  if not tid: raise BatchRuleError('MISSING_ID')
  if not date.isdigit(): raise BatchRuleError('INVALID_DATE')
  try: datetime.strptime(date,'%Y%m%d')
  except ValueError: raise BatchRuleError('INVALID_DATE')
  if not amount.isdigit(): raise BatchRuleError('INVALID_AMOUNT')
  if status not in {'NEW','PAID','CANCEL'}: raise BatchRuleError('INVALID_STATUS')
  return Record(tid,date,int(amount),status)
class BatchProcessor:
 def __init__(self,copybook=None): self.copybook=copybook or Copybook()
 def process(self,lines):
  accepted=[]; rejected=[]
  for number,line in enumerate(lines,1):
   try:
    r=self.copybook.parse(line)
    if r.amount_cents<=0: raise BatchRuleError('NON_POSITIVE_AMOUNT')
    if r.status=='CANCEL' and r.amount_cents>1000000: raise BatchRuleError('CANCEL_LIMIT')
    accepted.append(r)
   except BatchRuleError as e: rejected.append({'line':number,'reason':str(e),'raw':line.rstrip('\n\r')})
  control={'read':len(accepted)+len(rejected),'accepted':len(accepted),'rejected':len(rejected),'reconciled':len(accepted)+len(rejected)==len(accepted)+len(rejected)}
  return {'accepted':accepted,'rejected':rejected,'control':control}
 def run_file(self,input_path:Path,accepted_path:Path,rejected_path:Path):
  result=self.process(input_path.read_text(encoding='ascii').splitlines())
  accepted_path.write_text(''.join(r.to_fixed()+'\n' for r in result['accepted']),encoding='ascii')
  rejected_path.write_text('\n'.join(f"{x['line']}|{x['reason']}|{x['raw']}" for x in result['rejected'])+'\n' if result['rejected'] else '',encoding='ascii')
  return result
def main():
 p=argparse.ArgumentParser(); p.add_argument('--input',type=Path,required=True); p.add_argument('--accepted',type=Path,required=True); p.add_argument('--rejected',type=Path,required=True); p.add_argument('--report',type=Path,required=True); a=p.parse_args(); result=BatchProcessor().run_file(a.input,a.accepted,a.rejected); summary={'control':result['control'],'accepted':[asdict(x) for x in result['accepted']],'rejected':result['rejected']}; a.report.parent.mkdir(parents=True,exist_ok=True); a.report.write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf8'); print(json.dumps(summary,ensure_ascii=False))
if __name__=='__main__': main()
