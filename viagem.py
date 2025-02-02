distancia = float(input('Qual a distância de sua viagem? '))
print('Você está prestes a realizar uma viagem de {} km'.format(distancia))
print('-=-'*25)
print('Escolha uma empresa de ônibus para realizar sua viagem: ')
print('')
empresa = int(input('1- 1001 \n2- Itapemirim \n3- Util \n \nEscolha: '))
print('-=-'*25)

match empresa:

    case 1:
        print('Você optou por 1001!')
        if distancia<=200:
            preco=(distancia*0.5)
            print('Preço até 200km 1001')
        else:
            preco=(distancia*0.45)
            print('Preço acima de 200km 1001')
    case 2:
        print('Você optou por Itapemirim!')
        if distancia<=200:
            preco=(distancia*0.65)
            print('Preço até 200km Itapemirim')
        else:
            preco=(distancia*0.4)
            print('Preço acima 200km Itapemirim')
    case 3:
        print('Você optou por Util!')
        if distancia<=200:
            preco=(distancia*0.6)
            print('Preço até 200km Util')
        else:
            preco=(distancia*0.5)
            print('Preço acima de 200km Util')
    case _:
        print('Opção inválida')

if empresa==1:
    nome_empresa='1001'
elif empresa==2:
    nome_empresa='Itapemirim'
elif empresa==3:
    nome_empresa='Util'
else:
    nome_empresa='Empresa não registrada'
    
print('-=-'*30)
print('Você fará uma viagem de {} km pela empresa {} pelo valor de R${:.2f}'.format(distancia,nome_empresa,preco))
print('-=-'*30)