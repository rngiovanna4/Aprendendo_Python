#Leia a largura e altura de uma parede em metros e calcule sua área e a quantidade de tinta necessária para pinta-lá sabendo que
#cada litro de tinta, pinta uma área de 2 m2

altura= float(input('Digite a altura da parede em metros: '))
largura  = float(input('Digite a largura da mesma parede em metros: '))

area = altura * largura

uneed = area/2

print('Será necessário utilizar {:.1f}L de tinta'.format(uneed))
