'''Um jogo onde o computador pensa em um número e o usuário tenta adivinha qual foi o número escolhido. O programa deve escrever na tela se o usuário ganhou ou perdeu'''
from random import randint
num = randint(1,5)
print(num)
chute = int(input('Digite um número de 0 a 5 e tente adivinhar o número que o computador está pensando'))
print(num)

if num==chute:
    print('Você ganhou. O número é {}'.format(num))
else:
    print('Você perdeu. O número é {}'.format(num))