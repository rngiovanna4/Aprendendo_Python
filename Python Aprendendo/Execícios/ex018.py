# Um programa que leia um angulo qualquer e mostre o valor do seno, cosseno e a tangente ex018
from math import cos, degrees, radians, sin, tan, radians , pi

degrees = float(input('Digite o valor de um ângulo: '))
radians = radians(degrees)
#(degrees*pi)/180 convertendo graus em radianos


print('Cosseno de {}º é {:.3f}'.format(degrees, cos(radians)))
print('Seno de {}º é {:.3f}'.format(degrees, sin(radians)))
print('Tangente de {}º é {:.3f}'.format(degrees, tan(radians)))

