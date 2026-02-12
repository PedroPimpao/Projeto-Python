#Calculando a Hipotenusa
import math
print('Vamos calcular o valor da hipotenusa!!!')
ad=float(input('Cateto adjacente: '))
op=float(input('Cateto oposto: '))
hipo=math.hypot(ad,op)
print('Dado os valores {} e {}, a hipotenusa vale {:.1f}'.format(ad,op,hipo))

