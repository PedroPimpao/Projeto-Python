a = float(input('Insira o valor A:  '))
b = float(input('Insira o valor B:  '))
c = float(input('Insira o valor C:  '))
resultado = 0

def media(a, b, c):
    return (a+b+c)/3

resultado = media(a, b, c)

print(f"Média: {resultado}")