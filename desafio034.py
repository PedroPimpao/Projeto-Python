salario=float(input('Digite seu salário atual: '))
if salario>1250:
    novo_salario=(salario+(salario*(10/100)))
else:
    novo_salario=(salario+(salario*(15/100)))
print('O novo salário é R${:.2f}'.format(novo_salario))

