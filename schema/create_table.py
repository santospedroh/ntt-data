import sqlite3

# conectando...
conn = sqlite3.connect('post-it-database.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE post (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        mensagem TEXT NOT NULL,
        criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);
""")

print('Tabela criada com sucesso.')
# desconectando...
conn.close()