numero1 = 0
numero2 = 0
try: 
    numero1 = float(input("Insira um numero A: "))
    numero2 = float(input("Insira um numero B: "))
except ValueError: 
    print("Insira um valor válido")
finally: 
    soma = numero1 + numero2
    print(f"O resultado da soma é: {soma}")