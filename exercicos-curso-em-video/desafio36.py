valor_casa=float(input("Digite o valor da casa: R$"))
salario=float(input("Digite o seu salário: R$"))
anos=int(input("Em quantos anos deseja pagar?: "))
meses=anos*12
prestacao_mensal=valor_casa/meses
parte_salario=salario*(30/100)
print("A prestação mensal da casa vale: R${:.2f}".format(prestacao_mensal))
print("30% do salario vale: R${:.2f}".format(parte_salario))
if prestacao_mensal>parte_salario:
    print("Emprestimo NEGADO")
else: 
    print("Emprestimo APROVADO")

