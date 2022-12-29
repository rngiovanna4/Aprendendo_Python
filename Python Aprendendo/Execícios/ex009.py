#Tabuada de um número digitado pelo usuário
print('Digite um número para ver a sua tabuada')
number = int(input())
i = 0 
print('-'*15)
while(i<=10):
   print('{} X {:2} = {}'.format(number,i,number*i))
   i = i+1
print('-'*15)