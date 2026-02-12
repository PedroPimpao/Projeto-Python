numero1 = input('Insira um numero A:  ')
numero2 = input('Insira um numero B:  ')

value1 = int(numero1)
value2 = int(numero2)

if isinstance(value1, int) and isinstance(value2, int):
    print('Ambos os valores são inteiros')

print(f"Numero: {numero1}\nTipo: {type(value1)}")
print(f"Numero: {numero2}\nTipo: {type(value2)}")