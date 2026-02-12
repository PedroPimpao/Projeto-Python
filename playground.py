from math import sqrt
# print("Olá, mundo")
# print(10)
# print(5+2-1)
# name = "Pedro"
# idade = 20
# print(f"Nome: {name}\nIdade: {idade}") 

# name2 = "Pedro"
# idade2 = 20
# altura = 1.65
# ativo = True

# x = 10
# y = -3

# pi = 3.14

# inputName = input("Digite seu nome: ")
# inputIdade = int(input("Digite sua idade: "))
# inputAltura = float(input("Digite sua altura: "))

# print(f"Diga meu nome: {inputName}")
# print(f"Diga minha idade: {inputIdade}")
# print(f"Diga minha altura: {inputAltura}")

# print(10/3)
# print(10//3)
# print(2*3)
# print(2**3)

# idade = int(input("Digite sua idade: "))

# if idade >= 18:
#     print(f"{idade} anos, obrigatório votar")
# elif idade >= 16:
#     print(f"{idade} anos, pode votar")
# elif idade <= 12:
#     print(f"{idade} de idade. Você é literalmente crianca, não pode votar")
# else: 
#     print(f"Você tem {idade} anos. Menor de idade, não pode votar")

# print("While")

# contador = 0 

# while contador <= 5:
#     print(contador)
#     contador+=1

# print("For")

# for i in range (5):
#     print(i)

# print('---')

# for i in range(2, 11, 4):
#     print(i)

numeros = [1, 2, 3, 4]
nomes = ["Pedro", "João", "Ana"]

print(numeros[-1])
print(nomes[-1])
print(len(nomes))

numeros.pop()
numeros.append(5)
numeros.remove(2)

print(f"Lista: {numeros}")

cores = ("vermelho", "azuk", "verde")

print(f"Tupla: {cores}")

pessoa = {
    "nome": "Pedro",
    "idade": 20,
    "altura": 1.65
}

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["altura"])

numerosSet = {1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6, 7, 7, 7, 7, 7, }
print(numerosSet)

def soma(a, b):
    return a + b

resultado = soma(3, 5)
print(resultado)

print(sqrt(25))

try: 
    x = int(input("Digite um número: "))
    print(10/x)
except ValueError:
    print('Digite um numero valido')
except ZeroDivisionError:
    print("Não pode dividir por zero")