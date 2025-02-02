idade=int(input("Informe a sua idade: "))

if idade>0 and idade<=9:
    classificacao='MIRIM'
elif idade>9 and idade<=14:
    classificacao='INFANTIL'
elif idade>14 and idade<=19:
    classificacao='JUNIOR'
elif idade>19 and idade<=20:
    classificacao='SÊNIOR'
elif idade>20:
    classificacao='MASTER'
elif idade<0:
    classificacao='ERRO'

print("Você tem {} anos de idade, logo pertence a categoria {}".format(idade,classificacao))
