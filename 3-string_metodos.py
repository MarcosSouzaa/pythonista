# Alguns métodos comuns das Strings

nome_curso = 'Edição de Vídeo'

print(nome_curso.upper()) # Coloca tudo em maiúsculo
print(nome_curso.lower()) # Coloca tudo em minúsculo
print(nome_curso.capitalize()) # Coloca a primeira letra em maiúsculo   
print(nome_curso.title()) # Coloca a primeira letra de cada palavra em maiúsculo
print(nome_curso.strip()) # Remove espaço
print(nome_curso.lstrip()) # Remove espaços da esquerda
print(nome_curso.rstrip()) # Remove espaços da direita
print(nome_curso.find('ção'))# 
print(nome_curso.replace('Vídeo', 'Música')) # Substitui a palavra Vídeo por Música
print('https://sc.olx.com.br/?o=90&q=relogio'.replace('relógio', 'carro'))

#Exercício

a = 'é'
b ='MELHOR'
c = 'QUE'
d = 'feito'
e = 'perfeito'

print(f'{a.upper()} {b.lower()} {d.upper()} {c.lower()} {e.upper()}')
