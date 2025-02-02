import math
angulo=int(input('Digite um ângulo: '))
radianos=(math.radians(angulo))
print('O ângulo de {}° possui:'.format(angulo))
print('Seno de {:.2f}'.format(math.sin(radianos)))
print('Cosseno de {:.2f}'.format(math.cos(radianos)))
print('Tangente de {:.2f}'.format(math.tan(radianos)))