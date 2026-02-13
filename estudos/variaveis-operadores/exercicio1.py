# Leia dois números e mostre: soma, subtração, multiplicação e divisão.

resultado = ''
operacao = 0
a = float(input('Insira o valor A: '))
b = float(input('Insira o valor B: '))
operacao = int(input('Qual a operação? \n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nOperação: '))

def soma(a, b):
    return a+b

def subtracao(a, b):
    return a-b

def multiplicacao(a, b):
    return a*b

def divisao(a, b):
    if b == 0:
        return 'Impossível dividir por zero'
    return a/b

match operacao: 
    case 1:
        resultado = soma(a, b)
    case 2:
        resultado = subtracao(a, b)
    case 3: 
        resultado = multiplicacao(a, b)
    case 4:
        resultado = divisao(a, b)
    case _: 
        resultado = 'Operação inválida'

print(f"Resultado: {resultado}")