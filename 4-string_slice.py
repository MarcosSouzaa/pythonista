# Usando o índice para identificar valores dentro de uma string
instrumento = 'teclado teclado teclado teclado teclado teclado teclado'
print(instrumento[2]) # acesso a letra c
print(instrumento[4]) # acesso a letra a

# Acessando o último índice
print(instrumento[-1]) # acesso a letra o

# quero saber qual a posição de um caracter. Uso a função index()
tv = 'filmes'
print(tv.index('m')) # Acessa a posição 3

# Se eu quiser imprimir aonde está o índice m de forma dinâmica.
# Obs: Ele nunca inclui o último índice que vc passou
print(tv[tv.index('m')])
link = 'facebook.com/devaprender'
print(link[0]) # 0 é primeiro caracter = f
print(link[-1])# -1 é o último  caracter = r
print(link[0:5])# vai imprimir do índice 0 até 5 = faceb (não imprime o último)
print(link[0:])# como não especifiquei, ele vai imprimir do zero ao final
print(link[-5:])# da parte final da frase, ele vai voltar 5 índices e vai até o final
print(link[5:]) # Nesse caso, ele vai até o índice 5 e lê até o final
print(link[:-5]) # Caso eu não especifique o início, ele começa do zero e vai até o fim e retorna 5 caractéres

# Quando quiser buscar a última ocorrência de um caracter dentro de uma frase
frase = 'Clean Code'
print(frase.rindex('C')) # vai imprimir o último C da frase

 # DESAFIO 1 
 # Encontre o índice de "o" dentro da palavra Biblioteca
palavra = 'Biblioteca'
print(palavra.index('o')) # Vai imprimir o índice 5

 # Desafio 2 usando a frase: Desenvolvimento de Aplicações
 # Imprima apenas: de Aplicações
frase = 'Desenvolvimento de Aplicações'
print(frase[-13:]) # Vai imprimir: de Aplicações
