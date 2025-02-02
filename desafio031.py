distancia=float(input('Qual é a distância da viagem? '))
viagens_200=(distancia*0.5)
viagens_longas=(distancia*0.45)
print('A distância da viagem é {} km'.format(distancia))
if distancia<=200:
    print('O valor da passagem é R${:.2f} '.format(viagens_200))
else:
    print('O valor da passagem é R${:.2f} '.format(viagens_longas))