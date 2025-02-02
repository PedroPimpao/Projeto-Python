#Seno, Cosseno e Tangente
import math
print('Calcularemos o valor do Seno, Cosseno e Tangente de um ângulo!!!')
angulo=float(input('Digite um ângulo: '))
radianos=math.radians(angulo)
sen=math.sin(radianos)
cos=math.cos(radianos)
tan=math.tan(radianos)
print('O ângulo {}° possui: '.format(angulo))
print('Seno: {:.2f}'.format(sen))
print('Cosseno: {:.2f}'.format(cos))
Tangente=print('Tangente: {:.2f}'.format(tan))