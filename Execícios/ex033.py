'''Lê três números e vê qual o menor e qual o maior'''
a = int(input('Digite o 1º número\n'))
b = int(input('Digite o 2º número\n'))
c = int(input('Digite o 3º número\n'))

'''
==================================MINHA SOLUÇÃO===============================================
if a>b and a>c and b>c:
    print('O maior é {} e o menor é: {}'.format(a,c))
elif a>b and a>c and c>b:
     print('O maior é {} e o menor é: {}'.format(a,b))
elif b>a and b>c and a>c:
     print('O maior é {} e o menor é: {}'.format(b,c))
elif b>a and b>c and c>a:
     print('O maior é {} e o menor é: {}'.format(b,a))   
elif c>a and c>b and b>a:
     print('O maior é {} e o menor é: {}'.format(c,a))  
elif c>a and c>b and a>b:
     print('O maior é {} e o menor é: {}'.format(c,b)) 
else:
    print('ocorreu um erro') #Caso dois ou três números sejam iguais 
print('os números digitados foram:',a,b,c)'''

'''==================================SOLUÇÃO DO PROF==============================================='''
menor = a
if b < a and b < c :
     menor = b
if c < b and c < a :
     menor = c

maior = a
if b > a and b > c :
     maior = b
if c > b and c >a :
     maior = c

if menor == maior :
     print('Os valores são iguais')
else :
     print('O menor valor é {} e o maior é {}'.format(menor, maior))