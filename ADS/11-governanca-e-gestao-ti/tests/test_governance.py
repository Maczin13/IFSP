from pathlib import Path
import sys,pytest
sys.path.insert(0,str(Path(__file__).parents[1]))
from governance_lab import Control,GovernanceAudit,GovernanceRuleError
def control(**kw):
 d=dict(id='C1',objective='risk',framework='COBIT-EDM',owner='owner',evidence='evidence.md',status='implemented',effectiveness=4); d.update(kw); return Control(**d)
def test_pass_requires_evidence_and_effectiveness():
 assert control().result()=='PASS'; assert control(evidence='').result()=='FAIL'; assert control(effectiveness=2).result()=='FAIL'
def test_maturity_scores_status(): assert control().maturity()==5 and control(status='partial',effectiveness=2).maturity()==2 and control(status='missing',effectiveness=0).maturity()==0
def test_summary_and_frameworks():
 r=GovernanceAudit([control(),control(id='C2',framework='ITIL4',status='partial',effectiveness=2)]).summary(); assert r['total_controls']==2 and r['passed']==1 and r['by_framework']['ITIL4']==1 and r['maturity_level_0_to_5']==3.5
def test_invalid_control_domain():
 with pytest.raises(GovernanceRuleError): control(framework='ISO9001')
 with pytest.raises(GovernanceRuleError): control(effectiveness=7)
def test_empty_audit_rejected():
 with pytest.raises(GovernanceRuleError): GovernanceAudit([])
