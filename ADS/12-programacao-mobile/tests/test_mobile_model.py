from pathlib import Path
import sys,pytest
sys.path.insert(0,str(Path(__file__).parents[1]))
from mobile_model import LocalStore,Repository,StateHolder,SyncService,NetworkUnavailable,MobileRuleError
@pytest.fixture
def stack(tmp_path):
 s=LocalStore(str(tmp_path/'app.db')); r=Repository(s); return s,r,StateHolder(r,s)
def test_local_write_creates_outbox(stack):
 s,r,h=stack; state=h.add_note('Estudar UDF'); assert len(state.notes)==1 and state.pending_sync==1 and state.online is False; s.close()
def test_invalid_title(stack):
 with pytest.raises(MobileRuleError): stack[2].add_note('  ')
def test_toggle_is_versioned(stack):
 s,r,h=stack; n=h.add_note('Tarefa').notes[0]; h.repo.toggle(n.id); assert h.state().notes[0].done is True and h.state().notes[0].version==2; s.close()
def test_outbox_retries_after_network_failure(stack):
 s,r,h=stack; h.add_note('Sincronizar'); calls=[]
 def flaky(payload):
  calls.append(payload)
  if len(calls)==1: raise NetworkUnavailable('offline')
 service=SyncService(s,flaky); first=h.sync(service); assert first.pending_sync==1 and first.error=='offline'; second=h.sync(service); assert second.pending_sync==0 and len(calls)==2; s.close()
def test_sync_preserves_local_when_remote_fails(stack):
 s,r,h=stack; h.add_note('Offline'); service=SyncService(s,lambda _: (_ for _ in ()).throw(NetworkUnavailable('sem rede'))); state=h.sync(service); assert state.notes[0].title=='Offline' and state.pending_sync==1; s.close()
def test_remote_ack_is_idempotent_for_queue(stack):
 s,r,h=stack; h.add_note('Uma vez'); seen=[]; service=SyncService(s,lambda p: seen.append(p['id'])); state=h.sync(service); assert state.pending_sync==0 and len(seen)==1; s.close()
