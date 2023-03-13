nome = str(input("Qual o seu nome?"))
if nome == 'Giovanna':
	print("Que nome bonito, {}!".format(nome))
elif nome == "Pedro" or nome == "Maria" or nome == "José":
	print("Seu nome é bem popular no Brasil, {}.".format(nome))
elif nome in 'Davi, Nete, Cecé':
	print("Você mora na Lagoa Grande, {}".format(nome))
else:
    print("Você tem um nome normal, {}".format(nome))
print('Tenha um bom dia!')