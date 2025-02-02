#Conversor de Moedas 
real=float(input('Quanto você tem na carteira em Reais?'))
dolar=(real/5.15)
euro=(real/5.51)
pesoar=(real/0.0059)
print('Considerando R${:.2f}, ao realizar as conversões, você possui:'.format(real))
print('{:.2f}US$ (Dólar)'.format(dolar))
print('{:.2f} em Euro'.format(euro))
print('{:.2f} Pesos Argentinos (KKKKKKKK)'.format(pesoar))

