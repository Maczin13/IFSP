import sqlite3
def init():
 c=sqlite3.connect(':memory:'); c.execute('pragma foreign_keys=on'); c.execute('create table users(id integer primary key,name text not null)'); c.execute('create table tasks(id integer primary key,user_id integer not null references users(id),status text not null check(status in ('open','done')),created_at text not null,resolved_at text)'); return c
def kpi(c): return c.execute("select status,count(*) from tasks group by status").fetchall()
if __name__=='__main__': print(kpi(init()))
