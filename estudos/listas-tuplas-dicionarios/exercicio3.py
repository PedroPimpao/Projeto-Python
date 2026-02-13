# Encontre o maior e o menor número de uma lista.

lista = []
qtd_valores = 0
qtd_valores = int(input('Quantos valoes serão inseridos na lista?: '))

soma = 0
for i in range (1, qtd_valores + 1):
    valor = int(input(f'Insira um valor [{i}]:'))
    lista.append(valor)

print(lista)

print(f'Maior: {max(lista)}\nMenor: {min(lista)}')
