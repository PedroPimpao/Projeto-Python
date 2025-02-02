#Aluguel de Carros
kmr=float(input('Qual a quantidade de Kilometros percorridos?'))
dias=int(input('Qual o número de dias de aluguel?'))
valor_dias=(dias*60)
valor_km=(kmr*0.15)
valor_total=(valor_dias+valor_km)
print('O valor a pagar pelo aluguel é: R${:.2f}'.format(valor_total))