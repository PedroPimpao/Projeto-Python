peso=float(input("Informe seu peso em Kg: "))
altura=float(input("Informe sua altura em Metros: "))
imc=peso/altura**2
print("Seu IMC é: {:.2f}".format(imc))
sexo=int(input("Informe o sexo: \n1- Masculino \n2- Feminino \nOpção: "))
match sexo:
    case 1:
        sexo_nome='Masculino'
        if imc>=0 and imc<18.5:
            condicao='Abaixo do peso'
        elif imc>=18.5 and imc<25:
            condicao='Peso Ideal'
        elif imc>=25 and imc<30:
            condicao='Sobrepeso'
        elif imc>=30 and imc<40:
            condicao='Obesidade'
        elif imc>=40:
            condicao="Obesidade Mórbida"
        else:
            condicao='ERRO'
    case 2:
        sexo_nome='Feminino'
        if imc>=0 and imc<18.5:
            condicao='Abaixo do peso'
        elif imc>=18.5 and imc<25:
            condicao='Peso Ideal'
        elif imc>=25 and imc<30:
            condicao='Sobrepeso'
        elif imc>=30 and imc<40:
            condicao='Obesidade'
        elif imc>=40:
            condicao="Obesidade Mórbida"
        else:
            condicao='ERRO'
    case _:
        print("Erro")

print("======================") 
print("Sexo: {}".format(sexo_nome))
print("Peso: {}Kg".format(peso))
print("Altura: {}m".format(altura))
print("IMC: {:.1f}kg/m²".format(imc))
print("Condição: {}".format(condicao))   
print("======================") 

