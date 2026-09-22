from __future__ import annotations
import os, sqlite3
from flask import Flask, current_app, jsonify, redirect, render_template, request, url_for, g

SCHEMA='''CREATE TABLE IF NOT EXISTS tasks(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 title TEXT NOT NULL CHECK(length(trim(title)) BETWEEN 1 AND 120),
 done INTEGER NOT NULL DEFAULT 0 CHECK(done IN (0,1)),
 created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);'''

def create_app(test_config=None):
 app=Flask(__name__,instance_relative_config=True)
 app.config.from_mapping(DATABASE=os.path.join(app.instance_path,'tasks.sqlite'),TESTING=False)
 if test_config: app.config.update(test_config)
 os.makedirs(app.instance_path,exist_ok=True)
 with app.app_context(): init_db()
 @app.get('/')
 def index(): return render_template('index.html',tasks=query_tasks())
 @app.post('/tasks')
 def create_task():
  title=request.form.get('title','').strip()
  if not title: return render_template('index.html',tasks=query_tasks(),error='Informe um título.'),400
  if len(title)>120: return render_template('index.html',tasks=query_tasks(),error='O título deve ter até 120 caracteres.'),400
  db=get_db(); db.execute('INSERT INTO tasks(title) VALUES (?)',(title,)); db.commit()
  return redirect(url_for('index'),code=303)
 @app.post('/tasks/<int:task_id>/toggle')
 def toggle_task(task_id):
  db=get_db(); row=db.execute('SELECT done FROM tasks WHERE id=?',(task_id,)).fetchone()
  if row is None: return jsonify(error='tarefa não encontrada'),404
  db.execute('UPDATE tasks SET done=? WHERE id=?',(0 if row['done'] else 1,task_id)); db.commit(); return redirect(url_for('index'),303)
 @app.delete('/api/tasks/<int:task_id>')
 def delete_task(task_id):
  db=get_db(); cur=db.execute('DELETE FROM tasks WHERE id=?',(task_id,)); db.commit()
  return ('',204) if cur.rowcount else (jsonify(error='tarefa não encontrada'),404)
 @app.get('/api/tasks')
 def api_tasks(): return jsonify([dict(r) for r in query_tasks()])
 @app.teardown_appcontext
 def close_db(_exc):
  db=g.pop('db',None)
  if db is not None: db.close()
 return app

def get_db():
 if 'db' not in g:
  g.db=sqlite3.connect(current_app.config['DATABASE'])
  g.db.row_factory=sqlite3.Row
 return g.db

def init_db():
 db=sqlite3.connect(current_app.config['DATABASE']); db.executescript(SCHEMA); db.close()
def query_tasks(): return get_db().execute('SELECT id,title,done,created_at FROM tasks ORDER BY id DESC').fetchall()
