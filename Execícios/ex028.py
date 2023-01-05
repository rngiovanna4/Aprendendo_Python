'''Um jogo onde o computador pensa em um número e o usuário tenta adivinha qual foi o número escolhido. O programa deve escrever na tela se o usuário ganhou ou perdeu'''
from random import randint
from time import sleep
num = randint(1,5)
print('Vamos jogar?')
chute = int(input('Digite um número de 0 a 5 e tente adivinhar em que número eu pensando!\n'))
#print(num)
print('ANALISANDO A SUA RESPOSTA...')
sleep(3)

if num==chute:
    print('O número que eu pensei é {}. Você venceu!'.format(num))
else:
    print('Perdeu! Pensei no número é {}. Mais sorte na próxima! hehe/'.format(num))