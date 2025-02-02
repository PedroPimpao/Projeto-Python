soma=0
contador=0
for i in range(1,500,2): 
    if i%3==0:
        contador=contador+1
        print(i)
        soma=soma+i
print("==================")
print("Total de valores somados: {}".format(contador))
print("Somatório: {}".format(soma))
print("==================")