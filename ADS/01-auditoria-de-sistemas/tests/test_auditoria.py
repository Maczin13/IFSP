import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]))
from auditoria import audit
def test_fixture_detects_expected_patterns():
 rows,findings,errors=audit(Path(__file__).parents[1]/"access_logs.csv")
 assert len(rows)==7 and not errors
 assert sum(x["type"]=="out_of_hours" for x in findings)==4
 assert any(x["type"]=="brute_force_indication" for x in findings)
 assert any(x["type"]=="sensitive_without_approval" for x in findings)
def test_window_does_not_join_distant_failures(tmp_path):
 p=tmp_path/"x.csv"
 p.write_text("event_id,timestamp,user,ip,role,event,result,approval_id\nA,2026-01-01T08:00:00+00:00,u,1.1.1.1,g,login,failed,\nB,2026-01-01T08:10:00+00:00,u,1.1.1.1,g,login,failed,\nC,2026-01-01T08:20:00+00:00,u,1.1.1.1,g,login,failed,\n")
 assert not any(x["type"]=="brute_force_indication" for x in audit(p)[1])
