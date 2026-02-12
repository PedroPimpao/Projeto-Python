from datetime import date
ano=date.today().year
idade=int(input("Informe sua idade: "))
print("Estamos no ano de {} e você tem {} anos".format(ano,idade))

if idade==18:
    print("Está na hora de se alistar!")
elif idade>18:
    diferenca=idade-18
    print("Está {} anos atrasado para o Alisamento Militar!".format(diferenca))
elif idade<18:
    diferenca=18-idade
    print("Ainda restam {} anos para o Alisamento Militar".format(diferenca))