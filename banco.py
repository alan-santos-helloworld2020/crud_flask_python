import sqlite3
from sqlite3.dbapi2 import Cursor
db=sqlite3.connect('banco/onload.db')
class Banco:
  
    def criar():
        db.execute('''CREATE TABLE IF NOT EXISTS cliente
         (id INTEGER PRIMARY KEY AUTOINCREMENT,
         nome TEXT NOT NULL,
         telefone  TEXT NULL,
         email  TEXT NULL,
         cep  TEXT NULL);''')
        db.close()

    
    def lisar():
        cursor = db.execute('SELECT * FROM cliente')
        return cursor

