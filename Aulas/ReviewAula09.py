#Comandos e funções apresentados na aula 09 de python

'''USE # NOS COMANDO QUE NÃO DESEJA EXECUTAR '''

phrase = 'Giovanna está estudando'
alphabet= "abcdefghijklmnopqrstuvwxyz"

#Fatiamento de String
print(phrase[7]) #seleciona apenas o catactere na posição 7
print(phrase[0:7]) # seleciona do carctere 0 até o 7-1
print(alphabet[3:8:2]) #seleciona do 3 ao 8-1 pulando de 2 em 2
print(alphabet[2::4]) #seleciona do 2 até o fim da string pulando de 4 em 4
print(phrase[:8]) #seleciona do caractere na posição 0 até a posição 8
print(phrase[8:]) #seleciona do caractere 8 até o final
print(phrase[9::13]) #seleciona do caractere 9 e vai até o final pulando de 3 em 3

#Analise de String
len(phrase) #número de caracteres da string
phrase.count('n') #conta quantas vezes a letra n aparece na string
phrase.count('o',0,10) #a mesma função, mas com um intervalo definido
phrase.find('anna') #apresenta o caractere onde começa o 'anna'
phrase.find('Android') #quando a string apresentada não existe é apresentado -1
print('Giovanna' in phrase) #Se existir a palavra apresentada o operador retorna True

#Transformção de String
print(phrase.replace('Giovanna', 'Mariana')) #Ele coloca Mariana no lugar de Giovanna, mas é preciso salvar   
phrase.upper() #deixa tudo em MAIÚSCULO
phrase.lower() #deixa tudo minúsculo
phrase.capitalize() #deixa a 1º letra da string em Maíusculo
phrase.title() #Deixa A 1º Letra De Cada Palavra Da String Em Maíusculo
testedostrip = '  oi com espaços no inicio e fim   '
testedostrip.strip() #Remove espaços do inicio e do fim
testedostrip.rstrip() #Remove espaços só no fim
testedostrip.lstrip() #Remove espaços só no inicio

#Divisão de String
phrase.split() #a ideia é dividir a string em palavras

#Junção de Strings
'-'.join(phrase) #reune as strings e coloca - onde seria os espaços


