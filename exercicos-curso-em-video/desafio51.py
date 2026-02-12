#Progressão Aritimética
numero_termos=int(input("Número de termos: "))
primeiro_termo=int(input("Primeiro Termo: "))
razao=int(input("Razão: "))

inter=razao*(numero_termos-1)

termo_geral=primeiro_termo+inter

for i in range(primeiro_termo,termo_geral+1,razao):
    print(i)
 