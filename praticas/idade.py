from datetime import datetime

dia_hoje=datetime.today().day
mes_hoje=datetime.today().month
ano_hoje=datetime.today().year
print("Data de hoje: {}/{}/{}".format(dia_hoje,mes_hoje,ano_hoje))

hoje=datetime.now()
data_hoje=hoje.date()
print("Insira sua data de nascimento: ")
dia=int(input("Dia: "))
mes=int(input("Mês: "))
ano=int(input("Ano: "))

data_nascimento=datetime(year=ano,month=mes,day=dia)
print("Data de hoje: {}".format(data_hoje))
print("Data de nascimento: {}".format(data_nascimento.date()))

idade_dias=data_hoje-data_nascimento.date()
idade_anos=idade_dias/365.25
print("Minha idade: {} anos".format(idade_anos.days))










