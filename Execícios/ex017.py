#leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retangulo e mostre o valor da hipotenusa ex017
from math import pow, sqrt, hypot

cateto1 = float(input('Digite o valor do cateto oposto: '))
cateto2 = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = pow(cateto1,2) + pow(cateto2,2)
hipotenusa = sqrt(hipotenusa)

#O valor da hipotenusa também pode ser calculado através do método math.hypot que recebe o valor dos catetos como parametros
hipotenusa2 = hypot(cateto1, cateto2)

print('O valor da hipotenusa é {:.1f}'.format(hipotenusa))
print('O valor da hipotenusa através do metodo hypot é {:.1f}'.format(hipotenusa2))