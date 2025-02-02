#Reajuste Salarial
salario=float(input('Qual o salário do funcionario?'))
reajuste=int(input('Qual é o valor do reajuste?'))
aumento=(salario*(reajuste/100))
novo_salario=(salario+aumento)
print('Um funcionário que ganhava R${:.2f}, com {}% de aumento, passa a receber R${:.2f}'.format(salario,reajuste,novo_salario))