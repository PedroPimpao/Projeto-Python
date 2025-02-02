a=float(input('Digite o primeiro valor: '))
b=float(input('Digite o segundo valor: '))
c=float(input('Digite o terceiro valor: '))
if a<b<c:
    print('O maior valor é {} e o menor é {}'.format(c,a))
elif c<b<a:
    print('O maior valor é {} e o menor é {}'.format(a,c))
elif b<a<c:
    print('O maior valor é {} e o menor é {}'.format(c,b))
elif c<a<b:
    print('O maior valor é {} e o menor é {}'.format(b,c))
elif a<c<b:
    print('O maior valor é {} e o menor é {}'.format(b,a))
elif b<c<a:
    print('O maior valor é {} e o menor é {}'.format(a,b))