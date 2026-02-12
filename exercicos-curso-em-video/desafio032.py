from datetime import date
print('='*34)
print('O ano é BISSEXTO ou NÃO? ')
print('='*34)
ano=int(input('Digite um ano para análise (ou digite 0 para o ano atual): '))
resultado=(ano%4)
if ano==0:
    ano=date.today().year
    if ano%4==0 and ano%100 !=0 or ano%400==0:
        print('O ano {} é BISSEXTO'.format(ano))
    else:
        print('O ano {} NÃO é BISSEXTO',format(ano))

elif resultado==0 and ano%100!=0 or ano%400==0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))
