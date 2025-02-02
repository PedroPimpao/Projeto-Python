#Desconto de 8% com pagamento à vista e 15% de aumento se for parcelado.
produto=input('Qual é o produto desejado?')
preco=float(input('Qual é o preco do produto {}?'.format(produto)))
desconto=(preco*(8/100))
preco_desconto=(preco-desconto)
aumento=(preco*(15/100))
preco_aumento=(preco+aumento)
parcela=(preco/10)
print('O produto "{}", que custa originalmente R${}, passará a custar R${:.2f} caso seja pago à vista, ou custará R${:.2f} caso seja parcelado em 10x R${:.2f}.'.format(produto,preco,preco_desconto,preco_aumento,parcela))