numero_pessoas=int(input("Insira o número de pessoas a serem analisadas: "))
soma_idade=0
menos_vinte=0
maior=0
nome_maior=''
for i in range(1,numero_pessoas+1):
    print("---Pessoa ({})---".format(i))
    nome=str(input("Nome: ")).strip().upper()
    idade=int(input("Idade: "))
    sexo=str(input("Sexo(M/F): ")).strip().upper()
    soma_idade=soma_idade+idade
    media_idade=soma_idade/numero_pessoas
    if sexo=='F':
        if idade<20:
            menos_vinte=menos_vinte+1
    
    if i==1 and sexo=='M':
        maior=idade
        nome_maior=nome
    if sexo=='M' and idade>maior:
        maior=idade
        nome_maior=nome
    
print("=========================")
print("Média de idade: {:.1f}".format(media_idade))
print("Número de mulheres com menos de 20 anos: {}".format(menos_vinte))
print("Maior idade masculina: {}".format(maior))
print("Nome do homem mais velho: {}".format(nome_maior.title()))
print("=========================")
   
