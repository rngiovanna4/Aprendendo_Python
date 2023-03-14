'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

1 para binário
2 para octal
3 para hexadecimal'''

print('CONVERSOR')
num = int(input('Digite o número que pretende converter\n'))
option = int(input('Escolha uma das opções:\n1-Converter decimal para binário\n2-Converter decimal para octal \n3-Converter decimal para hexadecimal\n'))

if option == 1:
    print('{} equivale a '.format(num),bin(num)[2:], ' em binário')
elif option == 2:
    print('{} equivale a '.format(num),oct(num), ' em octal')
elif option == 3:
    print('{} equivale a '.format(num), f'{num:x}',' em hexadecimal') 
else:
    print('\33[31m Opção inválida. Digite 1, 2 ou 3.')