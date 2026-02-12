import random
import time
print('Eu pensarei em um número de 0 a 5. Tente advinhar!')
numero_comp=(random.randint(0,5))
numero=int(input('Digite um número de 0 a 5: '))
print('PROCESSANDO...')
time.sleep(3)


if numero==numero_comp:
    print('Você venceu! Escolhi o número {} e você acertou!'.format(numero_comp))
else:
    print('Você errou! Esolhi o número {} e você {}.'.format(numero_comp,numero))