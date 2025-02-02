print("___VALORES PARES NO INTERVALO___")
inicio=int(input("Valor de inicio: "))
final=int(input("Valor do fim do intervalo: "))

for i in range(inicio,final+1):
    if i%2==0:
        print(i)
print("FIM!")