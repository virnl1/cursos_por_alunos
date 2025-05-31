import sqlite3

#Criando uma conexão com o banco de dados
conexao = sqlite3.connect('alunos.db')

#criando um cursor
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    curso TEXT NOT NULL ,
    nota_final REAL NOT NULL
);

"""
)

#Fechando a conexão

conexao.close()

print("Tabela alunos criada com sucesso!")