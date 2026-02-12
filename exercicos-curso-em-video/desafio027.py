nome=str(input('Digite seu nome completo: ')).strip().lower().split()
print(nome)
primeiro_nome=nome[0]
print(primeiro_nome)
ultimo_nome=nome[len(nome)-1]
print(ultimo_nome)
print('Bem vindo(a) {} {}!'.format(primeiro_nome.capitalize(),ultimo_nome.capitalize()))





