'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programados vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.'''
print('ANALISE DE EMPRÉSTIMO BANCÁRIO')
casa = float(input('Digite o valor da casa que pretende comprar\n'))
salario = float(input('Digite o valor do seu salário\n'))
mes = int(input('Em quantos meses você pretende pagar?\n'))

trintaporcento = salario*0.3
parcela = casa/mes 
if trintaporcento >= parcela:
    print('\033[32mEMPRÉSTIMO APROVADO\nParcelas de R$ {:.2f}, durante {} meses'.format(parcela,mes))
else:
    print('\033[31mEMPRÉSTIMO NEGADO') 
