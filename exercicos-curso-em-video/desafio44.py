preco=float(input("Preço das compras: R$"))
print("FORMAS DE PAGAMENTO")
print("1- À vista em dinheiro/cheque: 10% de desconto")
print("2- À vista no cartão: 5% de desconto")
print("3- Em até 2x no cartão: Preço normal")
print("4- 3x ou mais no cartão: 20% de juros")
forma_pagamento=int(input("Opção: "))

match forma_pagamento:
    case 1:
        taxa=preco*(10/100)
        valor_final=preco-taxa
    case 2:
        taxa=preco*(5/100)
        valor_final=preco-taxa
    case 3:
        valor_final=preco
        parcela=preco/2
        print("À pagar: 2x R${:.2f}".format(parcela))
    case 4:
        taxa=preco*(20/100)
        valor_final=preco+taxa
    case _:
        valor_final=0

    
print("Total à pagar: R${:.2f}".format(valor_final))
