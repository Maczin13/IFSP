from pathlib import Path
import sys,pytest
sys.path.insert(0,str(Path(__file__).parents[1]))
from project_control import ProjectRuleError,Task,cpm,evm
def test_cpm_dates_float_and_critical_path():
 r=cpm([Task('A',3),Task('B',5,('A',)),Task('C',4,('A',)),Task('D',2,('B','C'))]); assert r['project_duration']==10; assert r['critical_path']==['A','B','D']; assert r['tasks'][2]['slack']==1
def test_cycle_is_rejected():
 with pytest.raises(ProjectRuleError,match='ciclo'): cpm([Task('A',1,('B',)),Task('B',1,('A',))])
def test_missing_predecessor_is_rejected():
 with pytest.raises(ProjectRuleError,match='ausente'): cpm([Task('A',1,('X',))])
def test_evm_complete_indicators():
 r=evm(80,72,90,120); assert r['CV']==-18 and r['SV']==-8; assert r['CPI']==.8 and r['SPI']==.9; assert r['EAC']==150 and r['ETC']==60 and r['VAC']==-30
def test_evm_zero_pv_is_defined(): assert evm(0,10,5,100)['SPI'] is None
def test_negative_or_zero_bac_rejected():
 with pytest.raises(ProjectRuleError): evm(1,1,1,0)
 with pytest.raises(ProjectRuleError): evm(-1,1,1,10)
