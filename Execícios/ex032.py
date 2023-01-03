'''Faça um programa que vê se um ano é bissexto'''
ano = int(input('Digite um ano e veja se ele é bissexto\n'))
if ano%4==0:
    print('{} é um ano bissexto!'.format(ano))
else:
    print('{} não é um ano bissexto!'.format(ano))