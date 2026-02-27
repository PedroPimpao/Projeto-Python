tabela=[]

contador=0

for i in range (3):
    linha = []
    for j in range (3):
        contador +=1
        linha.append(contador)
    tabela.append(linha)

print(tabela)

