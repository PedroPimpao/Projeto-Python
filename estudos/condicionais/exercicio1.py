nome = ''
idade = 0
maior_idade = False
nome = str(input('Digite seu nome:  '))
idade = int(input('Digite sua idade:  '))

pessoa = {
    "nome": nome,
    "idade" : idade
}

def maioridade(idade): 
    if(idade >= 18):
        return True
    return False

maior_idade = maioridade(pessoa['idade'])

if(maior_idade == True):
    print(f'{pessoa["nome"]} tem {pessoa["idade"]} anos e é MAIOR de idade')
else:
    print(f'{pessoa["nome"]} tem {pessoa["idade"]} anos e é MENOR de idade')
