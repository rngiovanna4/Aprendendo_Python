#Mostre o dobro, o triplo e a raíz quadrada de um número
number = int(input(' Digite um número: '))
bend = number*2
triple = number*3
root = pow(number,(1/2))

print(' O dobro de {}: {}\n O triplo de {}: {}\n A raíz quadrada de {}: {:.2f}\n '.format(number,bend,number,triple,number, root))