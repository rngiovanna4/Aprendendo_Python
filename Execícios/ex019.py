# Um programa que sorteie um nome de 4 alunos 
import random

lst = []

name1 = input('Digite o nome de 4 alunos:\n ')
name2 = input()
name3 = input()
name4 = input()

lst.append(name1)
lst.append(name2)
lst.append(name3)
lst.append(name4)

#Para adicionar itens a lista eu poderia usar: lst[name1,name2,name3,name4]

print(lst)

print('O aluno escolhido para apagar o quadro foi: ',random.choice(lst))
