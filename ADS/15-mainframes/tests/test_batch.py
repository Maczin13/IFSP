from pathlib import Path
import sys,pytest
sys.path.insert(0,str(Path(__file__).parents[1]))
from totaliza import BatchProcessor,Copybook,BatchRuleError

def line(tid='TRX001',date='20260921',amount='000000001250',status='NEW'): return f'{tid:<6}{date:>8}{amount}{status:<10}'
def test_copybook_maps_fixed_fields():
 r=Copybook().parse(line()); assert r.transaction_id=='TRX001' and r.date=='20260921' and r.amount_cents==1250 and r.status=='NEW'
def test_batch_reconciles_and_writes_accepts_rejects():
 result=BatchProcessor().process([line(),line(amount='000000000000'),line(date='20260230')]); assert result['control']=={'read':3,'accepted':1,'rejected':2,'reconciled':True}; assert {x['reason'] for x in result['rejected']}=={'NON_POSITIVE_AMOUNT','INVALID_DATE'}
@pytest.mark.parametrize('raw', ['short',line(status='UNKNOWN'),line(amount='not-a-number')])
def test_invalid_records_are_rejected(raw):
 r=BatchProcessor().process([raw]); assert r['control']['rejected']==1 and r['control']['reconciled']
def test_cancel_limit():
 r=BatchProcessor().process([line(amount='000001000001',status='CANCEL')]); assert r['rejected'][0]['reason']=='CANCEL_LIMIT'
def test_empty_batch_reconciles(): assert BatchProcessor().process([])['control']['reconciled'] is True
