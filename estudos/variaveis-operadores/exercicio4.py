# Leia um número e diga se ele é par ou ímpar.

valor = int(input('Insira um valor:  '))

if valor % 2 == 0:
    print(f'{valor} é par')
else: 
    print(f'{valor} é impar')