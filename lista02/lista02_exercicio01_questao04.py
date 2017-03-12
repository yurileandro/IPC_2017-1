# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# tiago ferreira aranha 	                1715310047
# Luiz Daniel Raposo Nunes de Mello	        1715310049
# Gabriel nascimento de Oliveira            1715310052
# Wilbert Luís Evangelista Marins           1715310055
# Mackson Garcez Moreno de Oliveira júnior  1215090300
# Edson de Lima Barros                      1715310043
# Renan de Almeida Campos                   0825060036
#
# 1.4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média
# ----------------------------------------------------------

nota_1 = input('Informe a sua nota do primeiro bimestre:')
nota_2 = input('Informe a sua nota do segundo bimestre:')
nota_3 = input('Informe a sua nota do terceiro bimestre:')
nota_4 = input('Informe a sua nota do quarto bimestre:')

media = (int(nota_1) + int(nota_2) + int(nota_3) + int(nota_4))/4

print ('Média dos quatro bimestres:', media)