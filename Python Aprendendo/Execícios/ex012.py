#Leia o preço de um produto e mostre o seu novo preço com 5% de desconto

price = float(input('Digite o valor do produto: R$ '))
newprice = price-(price*0.05)

print('o valor do produto com 5% de desconto é: R${:.2f}'.format(newprice))
