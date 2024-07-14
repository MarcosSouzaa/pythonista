# input
# Recebendo dados do usuário
# Vamos supor que eu quisesse receber a senha do usuário

senha = input('Digite sua senha: ')
print('Você digitou: ' + senha)

# O tipo recebido é sempre uma string
print(type(senha)) # <class 'str'>

# Se eu quiser qualquer outro tipo, tenho que fazer a conversão
quantidade_filmes = int(input('Quantos filmes você já viu esse mês?\n '))      
print(type(quantidade_filmes))#  

