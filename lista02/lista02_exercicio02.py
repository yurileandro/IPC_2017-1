#---------------------------------------------------------------------
#Introdução a Programação dos Computadores - IPC
#Universidade do Estado do Amazonas - UEA
#Prof. Jucimar Jr.
#Adham Lucas da Silva Oliveira           1715310001
#Enrique Leão Barbosa Izel               1715310048
#Erik Atilio Silva Rey                   1715310059
#Ulisses Antonio Antonino da Costa       1515090555
#Guilherme Silva de Oliveira             1715310034
#
#Desenhar um polígono com 3 lados iguais. Cada lado uma cor diferente.
#---------------------------------------------------------------------
import turtle  
t = turtle.Pen() 
turtle.bgcolor("purple") 
for x in range(1):
    t.pensize(20) 
    t.pencolor("red")
    t.forward(200) 
    t.left(120) 
    t.pencolor("blue")
    t.forward(200) 
    t.left(120) 
    t.pencolor("black")
    t.forward(200) 
    t.left(120) 
