# Crie uma lista com 5 números e mostre a soma deles.

lista = []
soma = 0
for i in range (1,6):
    valor = int(input(f'Insira um valor [{i}]:'))
    lista.append(valor)

print(lista)

for i in lista:
    soma += i
print(f'Soma: {soma}')