'''Leia o nome de uma pessoa e mostre na tela:
1- o nome todo maiúsculo
2- o nome todo minúsculo
3- quantidade de letras no nome inteiros (sem os espaços)
4- número de letras no primeiro nome'''
name = input('Digite o seu nome')
name = name.strip()
print(name.upper())
print(name.lower())


spaces = name.count(' ')
numname = len(name)

numname = (numname - spaces)
print('A quantidade de letras de {} é {}'.format(name,numname))