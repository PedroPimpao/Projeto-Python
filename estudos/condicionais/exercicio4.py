salario = 0
salario = float(input('Digite seu salário:  R$'))
novo_salario = 0
valor_base = 2000

def dar_bonus(salario):
    bonus = (10/100)*salario
    return salario + bonus

def analise_bonus(salario):
    if salario >= valor_base:
        novo_salario = dar_bonus(salario)
        print(f"[10% Bonus] O salário que era R${salario} foi reajustado para R${novo_salario}")
    else:
        print(f"O salário R${salario} é menor do que R${valor_base}, logo não receberá bonus")

analise_bonus(salario)