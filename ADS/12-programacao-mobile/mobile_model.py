from __future__ import annotations
import argparse,json,sqlite3,time,uuid
from dataclasses import dataclass,asdict
from datetime import datetime,timezone
from pathlib import Path
class MobileRuleError(ValueError): pass
class NetworkUnavailable(ConnectionError): pass
@dataclass(frozen=True)
class Note:
 id:str; title:str; done:bool=False; version:int=1
@dataclass(frozen=True)
class AppState:
 notes:tuple[Note,...]; pending_sync:int; online:bool; error:str|None=None
class LocalStore:
 def __init__(self,path=':memory:'): self.db=sqlite3.connect(path); self.db.row_factory=sqlite3.Row; self.db.executescript('CREATE TABLE IF NOT EXISTS notes(id TEXT PRIMARY KEY,title TEXT NOT NULL,done INTEGER NOT NULL,version INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS outbox(id INTEGER PRIMARY KEY AUTOINCREMENT,note_id TEXT NOT NULL,op TEXT NOT NULL,payload TEXT NOT NULL,attempts INTEGER NOT NULL DEFAULT 0);')
 def save_note(self,n:Note): self.db.execute('INSERT INTO notes VALUES(?,?,?,?) ON CONFLICT(id) DO UPDATE SET title=excluded.title,done=excluded.done,version=excluded.version',(n.id,n.title,int(n.done),n.version)); self.db.commit()
 def enqueue(self,n:Note): self.db.execute('INSERT INTO outbox(note_id,op,payload) VALUES(?,?,?)',(n.id,'upsert',json.dumps(asdict(n)))); self.db.commit()
 def notes(self): return tuple(Note(r['id'],r['title'],bool(r['done']),r['version']) for r in self.db.execute('SELECT * FROM notes ORDER BY rowid'))
 def outbox(self): return list(self.db.execute('SELECT * FROM outbox ORDER BY id'))
 def ack(self,rowid): self.db.execute('DELETE FROM outbox WHERE id=?',(rowid,)); self.db.commit()
 def fail(self,rowid): self.db.execute('UPDATE outbox SET attempts=attempts+1 WHERE id=?',(rowid,)); self.db.commit()
 def close(self): self.db.close()
class Repository:
 def __init__(self,store:LocalStore): self.store=store
 def create(self,title):
  if not isinstance(title,str) or not title.strip(): raise MobileRuleError('título vazio')
  n=Note(str(uuid.uuid4()),title.strip()); self.store.save_note(n); self.store.enqueue(n); return n
 def toggle(self,note_id):
  current=next((n for n in self.store.notes() if n.id==note_id),None)
  if not current: raise MobileRuleError('nota não encontrada')
  n=Note(current.id,current.title,not current.done,current.version+1); self.store.save_note(n); self.store.enqueue(n); return n
class SyncService:
 def __init__(self,store:LocalStore,remote): self.store=store; self.remote=remote
 def drain(self,max_items=100):
  processed=0; errors=[]
  for row in self.store.outbox()[:max_items]:
   try:
    payload=json.loads(row['payload']); self.remote(payload); self.store.ack(row['id']); processed+=1
   except NetworkUnavailable as e: self.store.fail(row['id']); errors.append(str(e)); break
  return {'processed':processed,'remaining':len(self.store.outbox()),'errors':errors}
class StateHolder:
 def __init__(self,repo:Repository,store:LocalStore): self.repo=repo; self.store=store; self.online=False; self.error=None
 def state(self): return AppState(self.store.notes(),len(self.store.outbox()),self.online,self.error)
 def add_note(self,title): self.repo.create(title); return self.state()
 def sync(self,service:SyncService):
  self.online=True; result=service.drain(); self.error=result['errors'][0] if result['errors'] else None; return self.state()
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--db',default='results/mobile.sqlite'); ap.add_argument('--out',default='results/state.json'); a=ap.parse_args(); s=LocalStore(a.db); r=Repository(s); h=StateHolder(r,s); h.add_note('Revisar arquitetura offline-first'); Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(asdict(h.state()),default=str,ensure_ascii=False,indent=2),encoding='utf8'); print(json.dumps(asdict(h.state()),default=str,ensure_ascii=False)); s.close()
if __name__=='__main__': main()
