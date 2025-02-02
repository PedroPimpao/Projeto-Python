contador=0
soma=0
for i in range(0,6):
    contador=contador+1
    numero=int(input("Insira um numero inteiro ({}): ".format(contador)))
    if numero%2==0:
            soma=soma+numero
print("")
print("A soma dos números inteiros pares é: {}".format(soma))