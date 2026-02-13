# Crie uma função que calcule a média de 3 notas.
a = float(input('Insira o valor A:  '))
b = float(input('Insira o valor B:  '))
c = float(input('Insira o valor C:  '))

def calc_media(a, b, c):
    return (a+b+c)/3

print(f'Valor da média: {calc_media(a, b, c)}')
