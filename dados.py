import sqlite3

def conectar_bd():
    #Estabelece uma conexão com o banco de dados SQLite.
    return  sqlite3.connect('alunos.db')

def inserir_aluno(nome, idade, curso, nota_final):
    #Insere um novo aluno na tabela alunos.
    con = conectar_bd()
    cur = con.cursor() 
    cur = cur.execute("""
        INSERT INTO alunos (nome, idade, curso, nota_final)
        VALUES (?, ?, ?, ?)
    """, (nome, idade, curso, nota_final))
    con.commit()
    con.close()

def listar_alunos():
        con = conectar_bd()
        cur = con.cursor()
        cur.execute("SELECT * FROM alunos")
        dados = cur.fetchall()
        con.close()
        return dados
    
def deletar_aluno(id):
        con = conectar_bd()
        cur = con.cursor()
        cur.execute("DELETE FROM alunos WHERE id = ?", (id,))
        con.commit()
        con.close()

def listar_cursos_unicos():
        con = conectar_bd()
        cur = con.cursor()
        cur.execute("SELECT DISTINCT curso FROM alunos")
        cursos = [c[0] for c in cur.fetchall()]
        con.close()
        return cursos

def listar_por_curso(curso):
        con = conectar_bd()
        cur = con.cursor()
        cur.execute("SELECT * FROM alunos WHERE curso = ?", (curso,))
        dados = cur.fetchall()
        con.close()
        return dados
 