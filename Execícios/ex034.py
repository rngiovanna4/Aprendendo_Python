'''Lê o salário de um funcionário e calcula o seu aumento.
sal>1250,00 aumenta 10%; sal<=1250 o aumento é de 15%'''
sal= float(input('digite o seu salário\n'))

if sal>1250:
    sal=+(sal + sal*0.10)
else:
    sal=+(sal + sal*0.15)

print('Seu novo salário é')
print('{:.2f}'.format(sal))