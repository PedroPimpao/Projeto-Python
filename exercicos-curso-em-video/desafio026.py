frase=input('Digite uma frase: ').strip().lower()
quantidade=frase.count('a')
primeira_loc=frase.find('a')+1
ultima_loc=frase.rfind('a')+1
total_letras=len(frase)
print('A letra A aparece {} vezes na frase'.format(quantidade))
print('A primeira letra A apareceu na posição {}'.format(primeira_loc))
print('A última letra A apareceu na posição {}'.format(ultima_loc))




