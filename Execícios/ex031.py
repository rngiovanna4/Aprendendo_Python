'''Leia uma distância de uma viagem em km. Viagens de até 200km cobra R$0,50 por km, viagens acima disso cobre R$0,45 por km'''
km = int(input('Digite a distância da sua cidade de origem até a sua cidade destino\n'))
if km<=200:
    taxa = 0.5
else:
    taxa = 0.45
print('O valor da sua viagem é R$ {:.2f}'.format(km*taxa))