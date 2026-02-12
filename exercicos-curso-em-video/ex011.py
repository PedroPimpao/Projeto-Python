#Pintando Parede
altura=float(input('Qual é a altura da parede?(Em metros)'))
largura=float(input('Qual é a largura da parede?(Em metros)'))
area=(altura*largura)
tinta=(area/2)
print('A parede possui dimensão de {}x{} e sua área vale {:.3f}m²'.format(largura,altura,area))
print('Para pintar a parede em questão, você precisará de {}L de tinta'.format(tinta))