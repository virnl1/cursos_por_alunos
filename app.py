import streamlit as st
import dados

st.title("Sistema de Cadastro de Alunos")

#Cadastro

st.header("Cadastro de Alunos")
nome = st.text_input("Nome do aluno")
idade = st.number_input("Idade do aluno", min_value=1, max_value=100)
curso = st.selectbox("Curso", ["Ciência de dados","Engenharia de Software", "Banco de Dados", "Inteligência Artificial",
                               "Enfermagem",
                                "Medicina", "Direito"])
nota_final =st.slider("Nota final", 0.0,10.0,5.0)

if st.button("Cadastrar Aluno"):
    if nome and idade and curso:
        dados.inserir_aluno(nome, idade, curso, nota_final)
        st.success("Aluno cadastrado com sucesso!")
    else:
        st.error("Por favor, preencha todos os campos obrigatórios.")

st.divider()

#Listar com filtro por curso
st.header("Listar Alunos")
cursos = ["Todos"] + dados.listar_cursos_unicos()
curso_filtro = st.selectbox("Filtrar por curso", cursos)

if curso_filtro != "Todos":
    alunos = dados.listar_por_curso(curso_filtro)
else:
    alunos = dados.listar_alunos()

st.table(alunos)

#Deletar aluno

st.subheader("Deletar Aluno")
id_deletar = st.number_input("ID do aluno a ser deletado", min_value=1, step=1)
if st.button("Deletar Aluno"):
        dados.deletar_aluno(id_deletar)
        st.success("Aluno com ID deletado com sucesso!")
