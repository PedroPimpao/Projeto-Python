#Tabuada
numero=int(input("Digite um número para ver sua tabuada: "))
for i in range(0,11):
    resultado=i*numero
    print("{} x {:2} = {}".format(numero,i,resultado))
