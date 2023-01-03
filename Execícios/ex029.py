'''Um programa que recebe uma velocidade. Acima de 80km/h mostre uma mensagem que mostra o valor da multa. R$ 7,00 para cada km acima do limite'''
speel = int(input('Digite a velocidade do carro'))

if speel>80:
    print('Você foi multado.')
    print('Valor da multa: R$ {:.2f}'.format((speel-80)*7))
else:
    print('Você estava dentro do limite permitido.')