#Calculando Descontos 
preco=float(input('Digite o preço do produto:'))
promocao=int(input('Qual é a promoção?'))
desconto=(preco*(promocao/100))
preco_novo=(preco-desconto)
print('O produto que custava R${}, na promoção com desconto de {}% vai passar a custar R${:.2f}'.format(preco,promocao,preco_novo))