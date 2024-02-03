import turtle, math
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()

def polygon(t, length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
    turtle.mainloop()

def circle(t,r):
    circumference = 2 * math.pi *r #calcula a circunferência do círculo
    n = 50 #quantidade de lados necessário para o "poligno" ser semelhante a um círculo
    length = circumference/n #tamanho de cada um desses lados
    polygon(t,  length, n) #essa função vai desenhar um polígno de 50 lados semelhante a um cículo

def circle2(t,r): 
    '''Versão melhorada da função circle que desenha n lados para um poligno semelhante a um círculo de raio r'''
    circumference = 2 * math.pi * r #
    n = int(circumference/3)+1 #a quantidade de lados necessários deixa de ser uma constante (50) e passa a mudar conforme o tamanho da circunferência para que não seja possível notas as retas que o formam.
    lenght = circumference/n
    polygon(t,lenght,n)
    
def arc(t,r, angle):
    for i in range(angle):
        t.fd(r)
        t.lt(1)
    turtle.mainloop()


#arc(turtle,2,180)
#polygon(turtle,70,7)
circle(turtle,1000)