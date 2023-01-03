'''Leia o nome de uma pessoa e mostre na tela:
1- o nome todo maiúsculo
2- o nome todo minúsculo
3- quantidade de letras no nome inteiros (sem os espaços)
4- número de letras no primeiro nome'''
name = str(input('Digite o seu nome completo')).strip()
print(name.upper())
print(name.lower())


spaces = name.count(' ')#Quantos espaços vazios há no nome
numname = len(name) #Tamanho da string digitada (contando com os espaços)

numname = (numname - spaces)
print('A quantidade de letras de {} é {}'.format(name,numname))