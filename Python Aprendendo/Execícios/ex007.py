#leia duas notas e mostre na tela a média entre as notas
name = input('Digite o nome do aluno: ')

grade1 = float(input('Digite duas notas:\n'))
grade2 = float(input())

average = (grade1+grade2)/2

print('A média de {} é: {:.1f}'.format(name, average))