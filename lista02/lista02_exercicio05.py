# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Edson de Lima Barros                      1715310043
# Gabriel Nascimento de Oliveira            1715310052
# Luiz Daniel Raposo Nunes de Mello	        1715310049
# Renan de Almeida Campos                   0825060036
# Tiago Ferreira Aranha 	                1715310047
# Wilbert Luís Evangelista Marins           1715310055
# Mackson Garcez Moreno de Oliveira júnior  1215090300
#
# 5 - Desenhar uma estrela de 5 pontas
# ----------------------------------------------------------

import turtle

lados_estrela = 5

p = turtle.Pen()

for x in range(lados_estrela):
    p.forward(40)
    p.left(360/lados_estrela)
    p.forward(40)
    p.right(360/lados_estrela*2)
