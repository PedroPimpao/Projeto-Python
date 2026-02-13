a = 0
b = 0

a = float(input('Insira um valor A:  '))
b = float(input('Insira um valor B:  '))

def iguais(a, b):
    if a == b:
        return True
    return False

def resposta():
    if iguais(a, b):
        print(f"Os números {a} e {b} são iguais")
    else:
        print(f"Os números {a} e {b} são diferentes")

resposta()