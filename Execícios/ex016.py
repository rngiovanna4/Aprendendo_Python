#Crie um programa que leia um número real e que imprima sua porção inteira EX:6,127 parte inteira: 6
from math import trunc
number1 = float(input('Digite um número real: '))
number = (trunc(number1))

print('A sua porção inteira é ', number)
print (number1)

#Ou podemos mostrar a porção inteira sem importar a função trunc
print (int(number1))

