from datetime import datetime

dia_hoje=datetime.today().day
mes_hoje=datetime.today().month
ano_hoje=datetime.today().year
print("Data: {}/{}/{}".format(dia_hoje,mes_hoje,ano_hoje))
hoje=datetime.now()
data_hoje=hoje.date()

numero_pessoas=int(input("Quantidade de pessoas: "))
total_maioridade=0
total_menoridade=0

for i in range(1,numero_pessoas+1):
    print("\nPessoa ({})".format(i))
    print("Insira sua data de nascimento: ")
    dia=int(input("Dia: "))
    mes=int(input("Mês: "))
    ano=int(input("Ano: "))
    data_nascimento=datetime(year=ano,month=mes,day=dia)
    idade_dias=data_hoje-data_nascimento.date()
    idade_ano=idade_dias/365.25
    print("Idade: {} anos".format(idade_ano.days))
    if idade_ano.days>=18:
        condicao='MAIORIDADE'
        total_maioridade=total_maioridade+1
    else:
        condicao='MENORIDADE'
        total_menoridade=total_menoridade+1
    print("Condição: {}".format(condicao))

print("\n")
print("==========================================")
print("Menoridade(Menor de 18 anos): {}".format(total_menoridade))
print("Maioridade(Maior de 18 anos ou): {}".format(total_maioridade))
print("==========================================")



