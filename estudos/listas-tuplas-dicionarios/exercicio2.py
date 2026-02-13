# Leia 5 nomes e armazene em uma lista.

lista = []
qtd_nomes = 0
nome = ''

qtd_nomes = int(input('Quantos nomes serão inseridos na lista?: '))

for i in range(1, qtd_nomes + 1):
    nome = str(input(f'Insira um nome [{i}]:  '))
    lista.append(nome)

print(f'{qtd_nomes} nomes na lista:')
for i in lista:
    print(i)
    print('---------')