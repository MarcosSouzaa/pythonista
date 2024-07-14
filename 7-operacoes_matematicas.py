# Operações Matemáticas
# Tipos de números que podem ser usados no Python:

a = 20
b = 20.5
print(type(a))# <class 'int'>
print(type(b))# <class 'float'>

# Operações matemáticas:

print(10 + 6) # 16
print(10 - 6) # 4
print(10 * 6) # 60
print(10 / 6) # 1.6666666666666667
print(10 // 6)# divisão de inteiro (só cabe 1 número 6 dentro de 10), não continua divisão
print(10 % 6) # Módulus (dentro de 10 ainda cabem 4 espaços), mostra o resto da divisão
print(10 ** 6)# Exponencial(10 elevado a 6) 1000000

# Atalho para atribuição mais rápida
a = 10
a += 5 # a = a + 5
print(a) # 15

b = 20
b -= 2
print(b) # 18

# Operações matemáticas comuns
# vou importar a biblioteca import math
import math

# Arredondamento para o mais próximo
print(round(5.7)) # 6

# Arredondamento para cima
print(math.ceil(2.2)) # 3
