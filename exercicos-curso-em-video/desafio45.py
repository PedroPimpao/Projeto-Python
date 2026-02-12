#Jokenpo
import random

maquina=random.randint(1,3)

print("===JOKENPÔ!===")
print("1- Pedra")
print("2- Papel")
print("3- Tesoura")
jogador=int(input("Opção: "))

match jogador:
    case 1:
        opcao='Pedra'
        if maquina==1:
            resultado='EMPATE'
        elif maquina==2:
            resultado='DERROTA'
        elif maquina==3:
            resultado='VITÓRIA'
        else:
            resultado='ERRO'
    case 2:
        opcao='Papel'
        if maquina==1:
            resultado='VITÓRIA'
        elif maquina==2:
            resultado='EMPATE'
        elif maquina==3:
            resultado='DERROTA'
        else:
            resultado='ERRO'
    case 3:
        opcao='Tesoura'
        if maquina==1:
            resultado='DERROTA'
        elif maquina==2:
            resultado='VITÓRIA'
        elif maquina==3:
            resultado='EMPATE'
        else:
            resultado='ERRO'

    case _:
        opcao='Erro'

match maquina:
    case 1:
        opcao_maquina='Pedra'
    case 2:
        opcao_maquina='Papel'
    case 3:
        opcao_maquina='Tesoura'
    case _:
        opcao_maquina='Erro'

print("======================")
print("Sua escolha: {}".format(opcao))
print("CPU: {}".format(opcao_maquina))
print("Resultado: {}".format(resultado))
print("======================")
        


