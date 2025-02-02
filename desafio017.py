import math
cato=int(input('Digite o comprimento do cateto oposto'))
cata=int(input('Digite o valor do cateto adjacente'))
hipo=(math.hypot(cato,cata))
print('O valor da hipotenusa vale: {}'.format(hipo))