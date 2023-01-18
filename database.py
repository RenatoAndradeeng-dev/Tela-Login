from distutils.util import execute
import sqlite3

conexao = sqlite3.connect('conexao.db')

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Username TEXT NOT NULL,
    Email TEXT NOT NULL,
    Password TEXT NOT NULL,
    ConfPassword TEXT NOT NULL 
)""")

print('conexao com banco feita com sucesso!')