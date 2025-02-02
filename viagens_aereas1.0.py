print('Bem Vindo (a) a agência de viagens!')
tipo_viagem=int(input('Será realizada uma viagem nacional ou internacional? \n1- Nacional \n2- Internacional \nOpção: '))
passageiros=int(input('Qual é o número de viagantes? '))
pagante=str(input('Nome completo do pagante: ')).strip().title()

match tipo_viagem:

    case 1:
        print('Você selecionou Viagem Nacional!')
        destino=int(input('Qual é o destino da viagem? \n1- Minas Gerais \n2- São Paulo \n3- Rio Grande do Sul \nOpção: '))
        match destino:
            case 1:
                print('Você selecionou Minas Gerais!')
                empresa=int(input('Selecione a companhia aérea: \n1- GOL \n2- AZUL \n3- LATAM \nOpção: '))
                match empresa:
                    case 1:
                        print('Você selecionou a GOL para a viagem até Minas Gerais!')
                        valor=(235*passageiros)
                    case 2:
                        print('Você selecionou a AZUL para a viagem até Minas Gerais!')
                        valor=(245*passageiros)
                    case 3:
                        print('Você selecionou a LATAM para a viagem até Minas Gerais!')
                        valor=(255*passageiros)
                    case _:
                        print('Opção Inválida')
                        valor=(0*passageiros)
                


            case 2:
                print('Você selecionou São Paulo!')
                empresa=int(input('Selecione a companhia aérea: \n1- GOL \n2- AZUL \n3- LATAM \nOpção: '))
                match empresa:
                    case 1:
                        print('Você selecionou a GOL para a viagem até São Paulo!')
                        valor=(270*passageiros)
                    case 2:
                        print('Você selecionou a AZUL para a viagem até São Paulo!')
                        valor=(260*passageiros)
                    case 3:
                        print('Você selecionou a LATAM para a viagem até São Paulo!')
                        valor=(265*passageiros)
                    case _:
                        print('Opção Inválida')
                        valor=(0*passageiros)
            

            case 3:
                print('Você selecionou Rio Grande do Sul!')
                empresa=int(input('Selecione a companhia aérea: \n1- GOL \n2- AZUL \n3- LATAM \nOpção: '))
                match empresa:
                    case 1:
                        print('Você selecionou a GOL para a viagem até Rio Grande do Sul!')
                        valor=(240*passageiros)
                    case 2:
                        print('Você selecionou a AZUL para a viagem até Rio Grande do Sul!')
                        valor=(250*passageiros)
                    case 3:
                        print('Você selecionou a LATAM para a viagem até Rio Grande do Sul!')
                        valor=(220*passageiros)
                    case _:
                        print('Opção Inválida')
                        valor=(0*passageiros)
            case _:
                print('Destino Inválido')
    case 2:
        print('Você selecionou Viagem Internacional! ')
        empresa=int(input('Selecione a companhia aérea: \n1- LATAM \n2- AZUL \nOpção: '))
        match empresa:
            case 1:
                print('Você selecionou LATAM para a sua viagem!')
                destino=int(input('Qual é o destino da viagem? \n1- Miami \n2- Lisboa \n3- Madrid \nOpção: '))
                match destino:
                    case 1:
                        print('Você viajará para Miami com a LATAM')
                        valor=(1320*passageiros)
                    case 2:
                        print('Você viajará para Lisboa com a LATAM')
                        valor=(1640*passageiros)
                    case 3:
                        print('Você viajará para Madrid com a LATAM')
                        valor=(1900*passageiros)
                    case _:
                        print('Destino Inválido')
                        valor=(0*passageiros)
            
            case 2:
                print('Você selecionou AZUL para a sua viagem!')
                destino=int(input('Qual é o destino da viagem? \n1- Miami \n2- Lisboa \n3- Madrid \nOpção: '))
                match destino:
                    case 1:
                        print('Você viajará para Miami com a AZUL')
                        valor=(1220*passageiros)
                    case 2:
                        print('Você viajará para Lisboa com a AZUL')
                        valor=(1710*passageiros)
                    case 3:
                        print('Você viajará para Madrid com a AZUL')
                        valor=(1700*passageiros)
                    case _: 
                        print('Destino Inválido')
                        valor=(0*passageiros) 
            case _:
                print('Opção Inválida')
    case _:
        print('Opção Inválida')

print('A viagem custará R${:.2f}'.format(valor))
print('O pagante será: {}'.format(pagante))