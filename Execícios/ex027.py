'''Leia um nome inteiro e mostre 
nome = Giovanna
último = Nascimento'''
nome = input('Digite seu nome completo').strip()
num = len(nome)-1
print(num)
print('Nome: {}\nÚltimo nome: {}'.format(nome[0],nome[num]))