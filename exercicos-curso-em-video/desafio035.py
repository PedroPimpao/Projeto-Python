#Formação de triângulo
print('='*25)
print('Analisador de Triângulos')
print('='*25)
a=float(input('Digite o segmento de a: '))
b=float(input('Digite o segmento de b: '))
c=float(input('Digite o segmento de c: '))
if a+b>c and a+c>b and b+c>a:
    print('Com os segmentos {}, {} e {} é POSSÍVEL formar um TRIÂNGULO'.format(a,b,c))
    if a==b==c:
        print('O triângulo é EQUILÁTERO')
    elif a-b==0 or a-c==0 or b-c==0:
        print('O triângulo é ISÓCELES')
    elif a!=b!=c:
        print('O triângulo é ESCALENO')
else:
    print('Com os segmentos {}, {} e {} NÃO é possível formar um TRIÂNGULO'.format(a,b,c))



