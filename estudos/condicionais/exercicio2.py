nome = ''
nota = 0

nome = str(input('Diga seu nome:  '))
nota = float(input('Digite sua nota:  '))

aluno = {
    "nome" : nome,
    "nota" : nota
}

def aprovado(nota):
    if(nota >= 6):
        return True
    return False

def resposta():
    if(aprovado(aluno['nota'])):
        print(f'O aluno {aluno["nome"]} foi APROVADO com a nota {aluno["nota"]}')
    else:
        print(f'O aluno {aluno["nome"]} foi REPROVADO com a nota {aluno["nota"]}')
        
resposta()