numero = input('Insira um valor:  ')

value = int(numero)
# value = float(numero)
# value = str(numero)

if isinstance(value, int):
    print('Inteiro')
elif isinstance(value, float):
    print('Decimal')
elif isinstance(value, str):
    print('String')
else: 
    print('Seilá')