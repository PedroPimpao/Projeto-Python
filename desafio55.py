for i in range(1,6):
    peso=float(input("Insira o peso da pessoa ({}): ".format(i)))
    if i==1:
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior=peso
        if peso<menor:
            menor=peso
print("Maior peso: {}kg".format(maior))
print("Menor peso: {}kg".format(menor))







