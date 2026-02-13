numero = 0
numero = float(input('Insira um número:  '))

def tipo_numero(numero):
    if numero > 0:
        print(f"O número {numero} é positivo")
    elif numero < 0:
        print(f"O número {numero} é negativo")
    else:
        print(f"Zero")

tipo_numero(numero)