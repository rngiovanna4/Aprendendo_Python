'''Comandos e funções estudados nas aulas 04 a 06 de python'''

'''USE # NOS COMANDO QUE NÃO DESEJA EXECUTAR'''


'''Os tipos primitivos são: 
1- int (números inteiros ex:10)
2- float (números reais ex:0,75)
3- bool (valores lógicos True ou False)
4- str (palavras e caracteres)
'''

'''lendo e imprindo um valor'''
nome = input('Digite o seu nome\n' )
print('Olá', nome)

'''A váravel sempre é recebida como string, por isso é importante convertes desde a entrada:'''
numero1= int(input('Digite um número: '))
numero2= float(input('Digite um número com duas casas decimais: '))
s= numero1+numero2

'''---------------------Utilize as sintaxe a seguir para imprimir:---------------------------------'''
print('A soma vale {}'.format(s))
print('Seu nome é: {}, sua idade é {}, e sua altura é {}'.format(nome,numero1,numero2))
print('Sua altura é: {:.3f}'.format(s)) #Para formatar a quantidade de casas decimais
print('iphone', 3) #Imprimindo letra e número

'''Truques de formatação'''
print('Olá, {:>20}!'.format(nome)) # Olá,             Giovanna!
print('Olá, {:<20}!'.format(nome)) # Olá, Giovanna            !
print('Olá, {:_^20}!'.format(nome)) # Olá, ______Giovanna______!
print('Olá, {: ^20}!'.format(nome)) # Olá,       Giovanna      !

'''Para imprimir dois prints lado a lado:'''
print('Oi usuário.', end=' ' )
print('Tudo bem?')  #Oi usuário. Tudo bem?

'''-----------------------Funções para dissecar uma váriavel---------------------------------------'''
n = input('Digite algo: ')

'''Há espaço na string? É vazio?'''
n.isspace() 
'''É número? (negativo ou décimal)'''
n.isnumeric()
'''É letra?'''
n.isalpha()
'''É número e/ou letra?'''
n.isalnum()
'''É um número inteiro, tipo digito, sem - ou ,?'''
n.isdigit()
'''É MAIÚSCULA?'''
n.isupper()
'''é minúscula?'''
n.islower()
'''É Capitalizada? Primeira Letra Maiúscula?'''
n.istitle()

