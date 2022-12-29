#Um programa que sortei a ordem de apresentação de 4 alunos ex020
from random import shuffle

i=0
lst = []
print('Digite o nome de quatro alunos para sortear a ordem de apresentação')
while i<4:
    lst.append(input(f'Digite o nome do {i+1}º aluno '))
    i = i+1

print(lst)
shuffle(lst)
print('A ordem de apresentação é: ', lst)
