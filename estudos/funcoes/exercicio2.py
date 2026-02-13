# Crie uma função que receba um número e diga se ele é par.

num = 0
num = int(input('Insira um valor:  '))

def epar(num):
    if num % 2 == 0:
        return True
    return False

if epar(num):
    print(f'O valor {num} é par')
else:
    print(f'O valor {num} é impar')