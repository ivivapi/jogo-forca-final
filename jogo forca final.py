# -*- coding: utf-8 -*-
cont = "sim"
import random
arquivo = open("entrada.txt", encoding="utf-8")
palavras = arquivo.readlines()
for i in range(len(palavras)-1):
    palavras[i] = palavras[i].strip().upper() 
    if palavras[i] == '':
        del palavras[i]
    palavras[i] = palavras[i].strip().upper()
pa = random.choice(palavras)


import turtle          # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("lightblue")
window.title("Jogo Da Forca")
window.screensize(canvwidth=1600,canvheight=1600)

tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
tartaruga.speed(10)  # define a velocidade
tartaruga.penup()       # Remova e veja o que acontece
tartaruga.setpos(-250,-200)
tartaruga.pendown()
tartaruga.color("blue")

dist = 120

#funções
def cabeça():
    tartaruga.penup()   # cabeça
    tartaruga.setpos(-80,90)
    tartaruga.pendown()
    tartaruga.circle(40)
    tartaruga.penup()
    tartaruga.setpos(-40,50)
    tartaruga.penup()
    
    
def corpo():    
    tartaruga.penup()
    tartaruga.setpos(-40,50)
    tartaruga.pendown()   # corpo
    tartaruga.forward(150)
    tartaruga.penup()
    
def braço1():    
    tartaruga.penup()
    tartaruga.setpos(-40,-100)
    tartaruga.pendown()
    tartaruga.backward(125)   # braço 1
    tartaruga.left(60)
    tartaruga.forward(70)
    tartaruga.backward(70)
    tartaruga.penup()
    
def braço2():    
    tartaruga.penup()
    tartaruga.setpos(-40,25)
    tartaruga.pendown()
    tartaruga.right(125)    # braço2
    tartaruga.forward(70)
    tartaruga.backward(70) 
    tartaruga.penup()
    
def perna1():
    tartaruga.left(65)    # perna1
    tartaruga.forward(125)
    tartaruga.left(35)
    tartaruga.penup()
    tartaruga.setpos(-40,-100)
    tartaruga.pendown()
    tartaruga.forward(100)
    tartaruga.backward(100)
    tartaruga.penup()
    
def perna2():   
    tartaruga.penup()
    tartaruga.setpos(-40,-100)
    tartaruga.pendown()
    tartaruga.right(75)   # perna2
    tartaruga.forward(100)



tartaruga.forward(120) 
tartaruga.backward(60)
tartaruga.left(90)
tartaruga.forward(400)
tartaruga.left(270)
tartaruga.forward(150)
tartaruga.right(90)
tartaruga.forward(70)
tartaruga.penup()

espaço = len(pa)
i=0
acertos = 0

while i<= espaço-1:
    
    
    if pa[i] == (" "):
        acertos+=1
    else:
        tartaruga.setpos(35*i-5*espaço,-200)
        tartaruga.write("_ ",font=("arial",25))
        
    i+=1


erros=0
espaço = len(pa)
lista = []


while erros < 6 and   acertos < espaço:
    l = window.textinput("escolha uma letra", "escolha uma letra")
    l = l.upper() 
    
    i = 0
      
    while i < espaço:
        if l in pa[i] :
            lista.append(l)
            tartaruga.penup()
            tartaruga.setpos(35*i-5*espaço,-190)
            tartaruga.write(l,font=("arial",20))
            acertos+=1
        if l == 'a' and pa[i]=='ã' or pa[i] == 'â' or pa[i] == 'á':
            lista.append(l)
            tartaruga.penup()
            tartaruga.setpos(35*i-5*espaço,-190)
            tartaruga.write(pa[i],font=("arial",20))
            acertos+=1
        if l == 'i' and pa[i] == 'í':
            lista.append(l)
            tartaruga.penup()
            tartaruga.setpos(35*i-5*espaço,-190)
            tartaruga.write(pa[i],font=("arial",20))
            acertos+=1
        if l == 'o' and pa[i] == 'ó' or pa[i] == 'ô':
            lista.append(l)
            tartaruga.penup()
            tartaruga.setpos(35*i-5*espaço,-190)
            tartaruga.write(pa[i],font=("arial",20))
            acertos+=1
        i += 1
    tentativas = []
        
    if l not in pa and l not in tentativas:
        erros+=1
        x = l.upper()
        tentativas.append(x)
        tartaruga.penup
        tartaruga.setpos(35*erros,-250)
        tartaruga.pendown
        tartaruga.write(tentativas,font=("arial",15))
        if erros == 1:
            cabeça()
        if erros == 2:
            corpo()
        if erros == 3:
            braço1()
        if erros == 4:
            braço2()
        if erros == 5:
            perna1()
        if erros == 6:
            perna2()
            tartaruga.penup()
            tartaruga.setpos(-300,-100)
            tartaruga.color("red")
            tartaruga.pendown() 
            tartaruga.write("Perdeu Parça",font=("arial",70))
            
if acertos == espaço:
    tartaruga.clear() 
    tartaruga.setpos(-300,-100)
    tartaruga.write("Vem Monxtro",font=("Arial",70))
    



window.exitonclick()
