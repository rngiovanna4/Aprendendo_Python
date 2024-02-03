import turtle, math
bob = turtle.Turtle()

def arc(t,r, angle):
    '''Desenha um arco. t é um método turtle, r é o raio do arco e angle é o ângulo desse raio'''
    step = (2*math.pi*r)/360
    for i in range(angle):
        t.fd(step)
        t.lt(1)

def flower(t, n_petals, len_petals, angle):
    '''desenha uma flor segundo as variaveis t, para o tamanho dela, n_petals, para o número de petalas e angle, para definir o tamanho da petala. quanto mais próximo de 360 maior o formato da pétala.  '''
    for i in range(n_petals):
        for i in range(2):
            arc(t,len_petals, angle)
            t.lt(180-angle)
        t.lt(360/n_petals)


flower(bob, 7,100,90)
turtle.mainloop()




