nota1=float(input("Informe a sua Nota 1: "))
nota2=float(input("Informe a sua Nota 2: "))
media=(nota1+nota2)/2

if media<5:
    status='REPROVADO'
elif media>=5 and media<7:
    status='RECUPERAÇÃO'
else:
    status='APROVADO'

print("Sua média final é: {:.1f}".format(media))
print("Status: {}".format(status))