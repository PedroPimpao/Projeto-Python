cidade=input('Digite o nome de uma cidade: ').strip()
city=cidade.lower()
print(city)
separado=city.split()
verificacao='rio'in separado[0]
print(verificacao)


