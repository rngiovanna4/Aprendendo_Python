'''Comandos e funções estudados nas aulas 07 de python'''

'''USE # NOS COMANDO QUE NÃO DESEJA EXECUTAR '''


'''----------------------------Operadores Aritiméticos---------------------------------
1- Adição +
2- Subtração -
3- Multiplicação *
4- Divisão /
5- Divisão Inteira //
6- Potência **
7- Resto da divisão %
8- Raiz quadrada ou cubica n**(1/2) ou n**(1/3)
'''
Divisão = 5/2
Potencia = pow(5,2) # ou 5**2
DiviInteira = 5//2
RestodaDivi = 5%2
RaizQuadrada = 25**(1/2)
RaizCubica = 125**(1/3)
print('Divisão de 5 para 2: {}\nPotência de 5 elevado 2: {}\nDivisão Inteira de 5 por 2: {}\nResto da divisão de 5 por 2: {}\nRaiz quadrada de 25: {}\nRaiz cubica de 125: {}'.format(Divisão,Potencia,DiviInteira,RestodaDivi,RaizQuadrada,RaizCubica))

'''Operadores nas strings'''
print('a'*70)
print('oi'+'olá')

'''
Ordem de procedência:
1º ()
2º **
3º * ou / ou // ou %
4º + ou -
'''
'''Há uma diferença nos comandos a seguir:'''
print('7'+'4')
print(7+4)
