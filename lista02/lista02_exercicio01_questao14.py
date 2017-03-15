# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Aracille de Souza Barbosa           1315120206
# Felipe Eduardo Silva de Almeida     1715310031
# Kethelen Tamara Braga               1525212002
# Nayara da Silva Cedeira da Costa    1715310038
# Vitor Summer Oliveira Pantaleão     1715310042
# Yuri Leandro de Aquino Silva        1615100462
#
# João Papo-de-Pescador, homem de bem, comprou um
# microcomputador para controlar o rendimento diário
# de seu trabalho. Toda vez que ele traz um peso de peixes
# maior que o estabelecido pelo regulamento de pesca do
# estado de São Paulo (50 quilos) deve pagar uma multa de
# R$ 4,00 por quilo excedente. João precisa que você faça
# um programa que leia a variável peso (peso de peixes) e
# verifique se há excesso. Se houver, gravar na variável
# excesso e na variável multa o valor da multa que João
# deverá pagar. Caso contrário mostrar tais variáveis com
# o conteúdo ZERO.
# ----------------------------------------------------------

weight = float(input("Digite o peso: "))
limp = 50.00
excess = float (weight - limp)
if weight > limp:
	mulct   = (excess * 4)
	print ("excesso foi de ", excess)
	print ("a multa foi", mulct)
else:
	print ("Excesso = ZERO")
	print ("Multa = ZERO")
