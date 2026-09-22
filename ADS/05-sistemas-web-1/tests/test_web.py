def test_index_empty(client):
 r=client.get('/'); assert r.status_code==200; assert b'Nenhuma tarefa' in r.data
def test_post_redirect_and_persist(client):
 r=client.post('/tasks',data={'title':'Estudar HTTP'}); assert r.status_code==303
 assert b'Estudar HTTP' in client.get('/').data
def test_validation_empty(client):
 r=client.post('/tasks',data={'title':'   '}); assert r.status_code==400; assert b'Informe um t' in r.data
def test_validation_too_long(client):
 r=client.post('/tasks',data={'title':'x'*121}); assert r.status_code==400
def test_toggle_and_api(client):
 client.post('/tasks',data={'title':'Tarefa'})
 client.post('/tasks/1/toggle'); data=client.get('/api/tasks').get_json(); assert data[0]['done']==1
def test_delete_existing_and_missing(client):
 client.post('/tasks',data={'title':'Remover'}); assert client.delete('/api/tasks/1').status_code==204; assert client.delete('/api/tasks/1').status_code==404
def test_accessible_form(client):
 html=client.get('/').data.decode(); assert 'for="title"' in html and 'aria-describedby="title-help"' in html
 error=client.post('/tasks',data={'title':' '}).data.decode(); assert 'role="alert"' in error
