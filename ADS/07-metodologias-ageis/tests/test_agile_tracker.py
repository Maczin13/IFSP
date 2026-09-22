from datetime import date
import pytest
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parents[1]))
from agile_tracker import AgileRuleError,AgileTracker,Status,WorkItem
@pytest.fixture
def items():
 d=date(2026,9,1); return [WorkItem('A','A',3,Status.DONE,d,d,date(2026,9,4)),WorkItem('B','B',5,Status.IN_PROGRESS,d,date(2026,9,3)),WorkItem('C','C',2,Status.TODO,d)]
def test_velocity_and_metrics(items):
 t=AgileTracker(items,2); assert t.velocity(date(2026,9,1),date(2026,9,30))==3; assert t.metrics()['average_lead_time_days']==3.0; assert t.metrics()['average_cycle_time_days']==3.0
def test_filter_by_status(items): assert [x.id for x in AgileTracker(items).filter(Status.TODO)]==['C']
def test_wip_limit(items):
 t=AgileTracker(items,wip_limit=1)
 with pytest.raises(AgileRuleError,match='WIP'): t.transition('C',Status.IN_PROGRESS,date(2026,9,5))
@pytest.mark.parametrize('points',[0,-1,True,1.5])
def test_points_contract(points):
 with pytest.raises(AgileRuleError): WorkItem('X','x',points)
def test_done_requires_date():
 with pytest.raises(AgileRuleError): WorkItem('X','x',1,Status.DONE)
def test_done_cannot_retrocede(items):
 with pytest.raises(AgileRuleError): AgileTracker(items).transition('A',Status.IN_PROGRESS,date(2026,9,6))
def test_transition_records_dates(items):
 t=AgileTracker(items); t.transition('C',Status.IN_PROGRESS,date(2026,9,5)); t.transition('C',Status.DONE,date(2026,9,8)); x=t.get('C'); assert x.cycle_time()==3 and x.lead_time()==7
def test_missing_item(items):
 with pytest.raises(AgileRuleError,match='inexistente'): AgileTracker(items).get('Z')
