# Valores aleatórios com random
import random

# Gera um valor de 0.0 a 1.0 cada vez que rodar
print(random.random()) # 0.06042763388356531 etc.

# Gera um valor decimal de valor Mínimo ao Máximo
print(random.uniform(4, 10)) # 9.25919849658331, 7.826848318293036 etc.

# Gera um valor inteiro de valor Mínimo ao Máximo
print(random.randint(4, 10)) # 7, 8, 9 etc.

# Lista de nomes, cores etc.
# Escolhe cores aleatóriamente
cores = ['Verde', 'Vermelho', 'Azul'] 
print(random.choice(cores))

# Posso escolher mais de uma cor usando choices e  k= a quantidade 
print(random.choices(cores, k=2))

# Embaralhar valores
cartas_de_baralho = ['Dama','Copa','Paus','Ouro']
print(random.shuffle(cartas_de_baralho)) # Aqui ele só embaralha
print(cartas_de_baralho) # Aqui ele imprime na tela o que embaralhou


