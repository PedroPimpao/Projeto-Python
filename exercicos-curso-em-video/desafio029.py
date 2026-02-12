#Radar Eletrônico
velocidade=int(input('Qual a velocidade do veículo? '))
velocidade_excedida=(velocidade-80)
multa=(velocidade_excedida*7)
print('A velocidade é {}km/h'.format(velocidade))
if velocidade>300:
    print('Você esta a {}km/h! Isso é um foguete?'.format(velocidade))
    print('Multa de R${:.2f}'.format(multa))
else:
    if velocidade<=80:
        print('Velocidade dentro do limite. Boa viagem!')
    else:
        print('Velocidade acima do limite de 80km/h. Multa de R${:.2f}'.format(multa))


print('')
print('1 Bebida + 4 Rodas = 7 Palmos. A conta pode não bater, mas você sim! Se beber, não dirija!!!')