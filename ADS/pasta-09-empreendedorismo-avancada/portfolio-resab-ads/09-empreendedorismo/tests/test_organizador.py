from pathlib import Path
from datetime import date
import pytest,sys
sys.path.insert(0,str(Path(__file__).parents[1]))
from organizador import AgileRuleError,Initiative,MVPPlanner,HypothesisStatus
@pytest.fixture
def items(): return [Initiative('A','A',100,3,.8,5,5,300,HypothesisStatus.VALIDATED),Initiative('B','B',50,2,.5,2,3,100),Initiative('C','C',20,1,.9,8,8,80)]
def test_rice_ranking(items): assert MVPPlanner(items).rank()[0].id=='A'
def test_wsfj_and_roi(items): assert items[0].wsfj(3)==1.2 and items[0].roi_time()==60
def test_portfolio_respects_hours(items):
 selected,used=MVPPlanner(items).portfolio(6); assert used<=6 and [x.id for x in selected]==['A']
def test_traction(items):
 r=MVPPlanner(items).traction(); assert r['total_initiatives']==3 and r['validated_hypotheses']==1 and r['validation_rate']==.333
def test_invalid_domains():
 with pytest.raises(AgileRuleError): Initiative('X','x',1,1,1.2,1,1,1)
 with pytest.raises(AgileRuleError): Initiative('X','x',1,1,.5,0,1,1)
def test_invalid_method_and_hours(items):
 p=MVPPlanner(items)
 with pytest.raises(AgileRuleError): p.rank('random')
 with pytest.raises(AgileRuleError): p.portfolio(0)
