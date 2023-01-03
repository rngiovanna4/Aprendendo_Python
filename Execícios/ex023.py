'''Leia um número e apresente:
num = 1834
unidade: 4
dezenas: 3
centenas: 8
milhares: 1'''


#numero= input('Digite um número\n')

'''--------------------------Resolução formato String----------------------------------'''

'''print("""unidades: {}\ndezenas: {}\ncentenas: {}\nmilhares: {}""".format(numero[3], numero[2], numero[1], numero[0]))'''

'''--------------------------Resolução formato String----------------------------------'''
from math import trunc
numero = int(input('Digite um número\n'))
milhar = trunc(numero/1000)
centena = trunc((numero - (milhar*1000))/100)
dezena = trunc((numero-((milhar*1000)+(centena*100)))//10)
unidade = trunc((numero - ((milhar*1000)+(centena*100)))%10)
print('unidades: ', unidade)
print('dezenas: ', dezena)
print('centenas: ',centena)
print('milhares: ', milhar )
