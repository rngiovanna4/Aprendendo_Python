'''Leia um nome  e mostre na tela se o nome começa ou não com o nome Santo'''
city = input('Digite o nome da sua cidade:\n').strip()
first= city.split()
#print(first)
if(first[0].upper()=='SANTO'):
    print('Inicia com Santo')
else :
    print('Não inica com Santo')