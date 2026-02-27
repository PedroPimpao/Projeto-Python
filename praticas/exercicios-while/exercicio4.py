N= int(input('Digite o valor de N:  '))

produtorio = 1
i = 1

while i <= N:
    produtorio = produtorio * i 
    i = i + 1

print(f'O produtório de {N} é {produtorio}')