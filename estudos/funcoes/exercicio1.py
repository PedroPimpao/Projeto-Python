# Crie uma função que receba dois números e retorne a soma.
a = 0
b = 0

a = float(input('Insira um valor A: '))
b = float(input('Insira um valor B: '))

def soma (a, b):
    return a+b

print(f'Resultado da soma: {soma(a, b)}')