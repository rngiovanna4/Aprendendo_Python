'''Leia uma frase e:
quantas letras a
posição da primeira e última letra A'''
phrase = input('Digite uma frase:\n').strip().lower()
print('Tem {} letras a'.format(phrase.count('a')))
print('A primeira letra a esta na posição: {}'.format(phrase.find('a')+1))
print('A última letra a esta na posição: {}'.format(phrase.rfind('a')+1))
