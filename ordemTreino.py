#Vamos sortear a ordem do treino da semana
import random
print('Vamos sortear a ordem de treinos da semana!!!')
treinos=['Braço','Perna','Costas','Peito','Fullbody','Abdômen']
random.shuffle(treinos)
print('A ordem de treinos dessa semana será: {}'.format(treinos))
