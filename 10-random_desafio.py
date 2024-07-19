import random

# DESAFIO 1
'''
Você quer simular a opção de jogar uma moeda e resultar em cara ou coroa. Jogue as opções dentro de
uma lista e depois crie um programa que imprime cara ou coroa na tela.
'''
moedas = ['cara','coroa']
input('Escolha cara ou coroa: ')
print(random.choice(moedas))

# DESAFIO 2
'''
Você quer fazer um sorteio entre 5 nomes em uma lista de nomes. Crie uma lista de 5 nomes e sorteie
um nome de dentro dessa lista e exiba na tela.
'''
nomes = ['Gisele','Alice','Letícia','Sinira','Silvia']
print(random.choice(nomes))

# DESAFIO 3
'''
Você quer escolher aleatóriamente um número de 10 - 100. Imprima na tela um valor aleatório entre 
10 e 100.
'''
print(random.randint(10, 100))