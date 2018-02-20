
import sqlite3

with sqlite3.connect("sqlite_db.db") as db:
    cursor = db.cursor()

cursor.execute('''
drop table if exists entries;
''')
cursor.execute('''
create table entries (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);
''')

db.commit()