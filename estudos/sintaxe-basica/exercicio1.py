# Faça um programa que imprima seu nome, idade e curso, cada um em uma linha.

nome = str(input("Insira seu nome:  "))
idade = int(input("Insira sua idade:  "))
curso = str(input("Insira o nome do seu curso: "))

aluno = {
    "nome": nome,
    "idade": idade,
    "curso": curso
}

print(f"Nome: {aluno['nome']}\nIdade: {aluno['idade']}\nCurso: {aluno['curso']}")