# Crie um dicionário com nome e nota de um aluno.

nome = ''
nota = 0
lista_alunos = []
qtd_alunos = 0

qtd_alunos = int(input('Quantos alunos serão inseridos na lista?:  '))

for i in range(1, qtd_alunos + 1):
    nome = str(input('Diga seu nome:  '))
    nota = float(input('Insira sua nota:  '))
    aluno = {
        "nome" : nome,
        "nota" : nota,
    }
    lista_alunos.append(aluno)

print(f'{qtd_alunos} alunos na lista:')
print('-----')
for aluno in lista_alunos:
    print(f'Nome: {aluno['nome']} | Nota: {aluno['nota']}')