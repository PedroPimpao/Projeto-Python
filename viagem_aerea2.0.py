print('='*34)
print('Bem Vindo(a) a Agência de Viagens!')
print('='*34)
pagante=str(input('Digite seu nome completo: ')).strip().title()
passageiros=int(input('Qual é o numero de passageiros? '))
tipo_viagem=int(input('Qual o tipo de viagem? \n1- Viagem Nacional \n2- Viagem Internacional \nOpção: '))

match tipo_viagem:
    
    case 1:
        print('Você selecionou Viagem Nacional!')
        empresa_nac=int(input('Selecione a companhia aérea : \n1- GOL \n2- AZUL \n3- LATAM \nOpção: '))
        
        if empresa_nac==1:
            nome_empresa='GOL'
        elif empresa_nac==2:
            nome_empresa='AZUL'
        elif empresa_nac==3:
            nome_empresa='LATAM'
        else:
            print('Companhia aérea nacional não encontrada')
            nome_empresa='"Não encontrada"'
        
        print('Você selecionou {}'.format(nome_empresa))
        destino=int(input('Qual é o destino da viagem? \n1- São Paulo \n2- Minas Gerais \nOpção: '))
        if destino==1:
            nome_destino='São Paulo'
        elif destino==2:
            nome_destino='Minas Gerais'
        else:
            nome_destino='"Destino não Identificado"'
        print('O destino da viagem será {} pela {}'.format(nome_destino,nome_empresa))

        match empresa_nac:
            case 1:
                if destino==1:
                    preco=(130*passageiros)
                elif destino==2:
                    preco=(185*passageiros)
                else:
                    preco=(0*passageiros)
            case 2:
                if destino==1:
                    preco=(145*passageiros)
                elif destino==2:
                    preco=(210*passageiros)
                else:
                    preco=(0*passageiros)
            case 3:
                if destino==1:
                    preco=(135*passageiros)
                elif destino==2:
                    preco=(195*passageiros)
                else:
                    preco=(0*passageiros)
            case _:
                print('Isso tá erradoo')
                preco=(0*passageiros)
        print('='*90)
        print('A Viagem Nacional terá como destino {} pela {} pelo valor de R${:.2f}'.format(nome_destino, nome_empresa,preco))
        print('Titular da compra: {}'.format(pagante))
        print('='*90)

    case 2:
        print('Você selecionou Viagem Internacional!')
        empresa_int=int(input('Selecione a companhia aérea: \n1- AZUL \n2- LATAM \nOpção: '))
        if empresa_int==1:
            nome_empresa='AZUL'
        elif empresa_int==2:
            nome_empresa='LATAM'
        else:
            nome_empresa='"Não Identificado INT"' 
        destino_int=int(input('Qual é o destino da viagem? \n1- Lisboa \n2- Orlando \nOpção: '))
        if destino_int==1:
            nome_destino='Lisboa'
        elif destino_int==2:
            nome_destino='Orlando'
        else:
            nome_destino='Destino internacional não identificado' 

        match empresa_int:
            case 1:
                if destino_int==1:
                    preco=(1500*passageiros)
                elif destino_int==2:
                    preco=(1210*passageiros)
                else:
                    preco=(0*passageiros)
            case 2:
                if destino_int==1:
                    preco=(1340*passageiros)
                elif destino_int==2:
                    preco=(1150*passageiros)
                else:
                    preco=(0*passageiros)
            case _:
                print('Isso não ta certo')
                preco=(0*passageiros)
        print('='*90)        
        print('A Viagem Internacional terá como destino {} pela {} pelo valor de R${:.2f}'.format(nome_destino,nome_empresa,preco))
        print('Titular da compra: {}'.format(pagante))
        print('='*90)
    case _:
        print('Tipo de viagem não identificada')
