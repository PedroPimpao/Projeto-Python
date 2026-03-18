lista_produtos = ["iphone", "ipad", "airpod", "macbook"]
tupla_produtos = ("iphone", "ipad", "airpod", "macbook")
set_produtos = {"iphone": 1500, "ipad": 1200, "airpod": 1234, "macbook": 1700}
print(set_produtos)

# Pegar valores
print(lista_produtos[0])
print(tupla_produtos[0])
print(list(set_produtos)[0])

# Adicionar
lista_produtos.append('apple watch')
# set_produtos.add('apple watch')


# Repetidos
lista_produtos = ["iphone", "ipad", "airpod", "macbook", "macbook"]
tupla_produtos = ("iphone", "ipad", "airpod", "macbook", "macbook")
set_produtos = {"iphone", "ipad", "airpod", "macbook", "macbook"}

print(lista_produtos)
print(tupla_produtos)
print(set_produtos)