nome=str(input('Qual é o nome do aluno? ')).strip().title()
print('')
t1=float(input('Digite a nota do Teste 1: '))
p1=float(input('Digite a nota da Prova 1: '))
m1=(t1+p1)/2
print('')
t2=float(input('Digite a nota do Teste 2: '))
p2=float(input('Digite a nota da Prova 2: '))
m2=(t2+p2)/2
print('')
t3=float(input('Digite a nota do Teste 3: '))
p3=float(input('Digite a nota da Prova 3: '))
m3=(t3+p3)/2
print('')
media_total=m1+m2+m3
media_final=(m1+m2+m3)/3
print('')

if media_final>=7:
    print('O aluno(a) {} teve a Média Final {:.1f} e foi aprovado! Parabens!'.format(nome,media_final))
else:
    print('O aluno(a) {} teve a Média Final {:.1f} e infelizmente foi reprovado(a)... Estude mais!'.format(nome,media_final))

print('O aluno(a) {} teve médias M1={:.1f}, M2={:.1f} e M3={:.1f}'.format(nome,m1,m2,m3))
print('Média Total igual a: {:.1f}'.format(media_total))

print('')
print('Análise de Desempenho de {}'.format(nome))
print('Média do 1° Trimestre: {:.1f}'.format(m1))
print('Média do 2° Trimestre: {:.1f}'.format(m2))
print('Média do 3° Trimestre: {:.1f}'.format(m3))
print('')
if m1>=7:
    print('A média do 1° Trimestre foi BOA')
else:
    print('A média do 1° Trimestre foi RUIM')

if m2>=7:
    print('A média do 2° Trimestre foi BOA')
else:
    print('A média do 2° Trimestre foi RUIM')

if m3>=7:
    print('A média do 3° Trimestre foi BOA')
else:
    print('A média do 3° Trimestre foi RUIM')
print('')
