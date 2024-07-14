# Split e Join
# Split é uma função que separa os espaços de uma string em uma lista de strings.
frase = 'Olá, bem-vindo a este treinamento!'
print(frase.split()) # ['Olá,', 'bem-vindo', 'a', 'este', 'treinamento!']

# Posso passar por split qualquer informação para separar algo
# no exemplo, quero encontrar uma virgula que separe uma frase
print(frase.split(',')) # ['Olá', ' bem-vindo a este treinamento!']

# Vou encontrar um traço '-' que está na frase
print(frase.split('-')) # ['Olá, bem', 'vindo a este treinamento!']

# Note que ele não separa os que não tem espaço como Amanda e Jefferson.
nomes = 'Jhonatan, Rafael, Carol, Amanda,Jefferson'
print(nomes.split()) # ['Jhonatan,', 'Rafael,', 'Carol,', 'Amanda,Jefferson']

# Se eu usar o separador de vírgulas ele vai separar todas as ocorrências
# aonde foram encontradas vírgulas
print(nomes.split(','))# ['Jhonatan', ' Rafael', ' Carol', ' Amanda', 'Jefferson']

# vou usar a variável hashtag 
# Vou usar o split sem passar nenhum parâmetro
hashtag = '#music #guitar #gamer #coder #python'
print(hashtag.split()) # vai separar os espaços em branco: ['music', '#guitar', '#gamer', '#coder', '#python'] 

# Vou usar os espaços com parâmetro
print(hashtag.split('#')) # Vai separar conforme segue: ['music ', 'guitar ', 'gamer ', 'coder ', 'python'] 
'''
Caro eu queira parametrizar para que ele faça separação até um certo ponto e depois pare,
eu posso passar um segundo parâmetro para essa função split o separador que usará e 
quantas ocorrências ele deve procurar antes de parar.
'''
# Note que a última ocorrência estão juntas.
print(hashtag.split('#', 3)) # ['music ', 'guitar ', 'gamer ', 'coder #python']

'''Como concatenar (combinar) juntar novamente colocando algo entre eles
por exemplo: vírgula, espaço, ponto etc.'''

# Primeiro vou usar um espaço como separador.
hashtag_separadas_por_espaco = hashtag.split(' ')
print(hashtag_separadas_por_espaco) # ['music', '#guitar', '#gamer', '#coder', '#python']

# Usando o join
# Quero que entre cada ítem da lista seja inserido uma vírgula
print(','.join(hashtag_separadas_por_espaco)) # juntou e separou por vírgula: #music,#guitar,#gamer,#coder,#python

# Usando ponto
print('.'.join(hashtag_separadas_por_espaco)) # #music.#guitar.#gamer.#coder.#python

# usando espaço
print(' '.join(hashtag_separadas_por_espaco)) # #music #guitar #gamer #coder #python

# DESAFIO
frase1 = 'Desafio manipulação de strings'
frase2 = 'Jhonatan,Rafael,Carol,Camila'
'''
DESAFIO 1
Transforme a frase1 em uma lista de palavras e guarde o resultado em uma variável chamada
palavras1.
'''
palavras1 = frase1.split() # ['Desafio', 'manipulação', 'de', 'strings']
print(palavras1)
'''  
DESAFIO 2
Transforme a frase2 em uma lista de palavras e guarde o resultado em uma variável chamada
palavras2
'''
palalavras2= frase2.split(',') # ['Jhonatan,Rafael,Carol,Camila']
'''
DESAFIO 3
Pegue o palavras1 e transforme elas no seguinte String: "Desafio,manipulação,de,strings".
Imprima o resultado no console.  
'''
print(','.join(palavras1)) # Desafio,manipulação,de,strings

'''
Desafio 4
Pegue o palavras2 e transforme elas no seguinte String:
frase2 = "Jhonatan & Rafael & Carol & Camilla". Imprima o resultado no console.
'''
print(' & '.join(palalavras2))