# Crie uma função que receba uma lista e retorne o maior valor

lista_valores = []
qtd_valores = 0

qtd_valores = int(input('Quantos valores terá a lista?: '))
valor = 0

for i in range(1, qtd_valores + 1):
    valor = float(input(f'Insira um valor [{i}]:  '))
    lista_valores.append(valor)
    
def maior_valor(lista):
    return max(lista)

m_valor = maior_valor(lista_valores)
print(f'Maior valor da lista: {m_valor}')