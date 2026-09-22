CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nome TEXT NOT NULL);
CREATE TABLE tarefas (id INTEGER PRIMARY KEY, usuario_id INTEGER, status TEXT, FOREIGN KEY(usuario_id) REFERENCES usuarios(id));
