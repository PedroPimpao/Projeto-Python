# Leia dois números e diga qual é o maior.

a = int(input("Digite o valor A:  "))
b = int(input("Digite o valor B:  "))

if a > b:
    print(f'{a} é maior')
elif b > a: 
    print(f'{b} é maior')
else: 
    print(f'{a} e {b} são iguais')
