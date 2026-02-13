# Leia números até que o usuário digite 0.

while True:
    valor = float(input('Insira um valor: '))
    print(f'Valor inserido: {valor}')
    if valor == 0:
        print(f'Você inseriu o valor {valor}. Loop encerrado!')
        break