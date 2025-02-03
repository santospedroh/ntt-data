import sqlite3

conn = sqlite3.connect('post-it-database.db')
cursor = conn.cursor()

# inserindo dados na tabela
cursor.execute("""
INSERT INTO post (nome, mensagem)
VALUES ('Regis', 'Olá, esse é um teste de um banco de dados SQLite3')
""")

cursor.execute("""
INSERT INTO post (nome, mensagem)
VALUES ('Krobe Byrant', 'Best Bastketballer of all times')
""")

cursor.execute("""
INSERT INTO post (nome, mensagem)
VALUES ('Micheal Jordan', 'As for this legend no  comments')
""")

cursor.execute("""
INSERT INTO post (nome, mensagem)
VALUES ('Pedro', 'App Python Flask e SQLite3. Aqui você pode deixar uma mensagem de texto. 🧑🏻‍💻 🚀')
""")

# gravando no bd
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()