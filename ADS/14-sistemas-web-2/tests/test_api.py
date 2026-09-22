import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]))
from fastapi.testclient import TestClient
from api import app,repo
client=TestClient(app)
def setup_function(): repo.items.clear(); repo.next_id=1
def test_openapi_contract():
 spec=client.get('/openapi.json'); assert spec.status_code==200 and spec.json()['openapi'].startswith('3.') and '/items' in spec.json()['paths']
def test_create_returns_201_and_get():
 r=client.post('/items',json={'title':'Estudar API','priority':5}); assert r.status_code==201 and r.json()['id']==1
 assert client.get('/items/1').json()['title']=='Estudar API'
def test_validation_returns_422():
 assert client.post('/items',json={'title':'','priority':9}).status_code==422
 assert client.post('/items',json={'title':'x'*121}).status_code==422
def test_missing_returns_404(): assert client.get('/items/999').status_code==404 and client.delete('/items/999').status_code==404
def test_list_and_delete():
 client.post('/items',json={'title':'A'}); client.post('/items',json={'title':'B'}); assert len(client.get('/items').json())==2; assert client.delete('/items/1').status_code==204; assert len(client.get('/items').json())==1
def test_health(): assert client.get('/healthz').json()=={'status':'ok'}
