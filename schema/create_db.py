import sqlite3

conn = sqlite3.connect('post-it-database.db')
print('Banco de daos criado com sucesso.')
conn.close()