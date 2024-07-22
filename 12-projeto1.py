# Objetivo do Projeto
'''
| Criando um módulo de login do aplicativo, e devo obter as seguintes informações do usuário:

Módulo 1 - Gerar registro do funcionário
Funcionalidade do módulo 1 
1- Obtenha o nome do funcionário
2- Obtenha a idade do funcionário
3- Registrar de forma automática a data do cadastro do funcionário usando a data que foi registrado
como Data do Registro.
4- Para cada novo funcionário que é registrado na empresa, ele recebe um dos seguintes cartões, que 
é sorteado de forma aleatória:
cartoes = ['R$50,00', R$250,00','R$120,00']
5- Guarde informações sobre a data de aniversário do funcionário (dd/mm/aaaa)
'''
from datetime import datetime # Para data/hora
from datetime import date
import random
from math import floor

print('\n******************************** CADASTRO ********************************\n')
nome = input('Digite o seu nome completo:\n')
#input('Digite a sua idade: ')
#data_aniversario = datetime.strptime(input('Digite a data do seu aniversário: '), '%d/%m/%Y')

"""
 Retorna a idade em anos, meses e dias com base na data de nascimento fornecida.
 Parâmetros:
 - data_nascimento (datetime): Data de nascimento no formato datetime.
 Retorna:
 - str: Uma string formatada com a idade em anos, meses e dias vividos.
 Exemplo:
 >>> data_nascimento = datetime.strptime('14/10/2021', '%d/%m/%Y')
 >>> calcula_idade(data_nascimento)
 'Voce tem: 1 ano de idade, 18 meses e 575 dias vividos.'
 """
def calcula_idade(data_nascimento):
 
 anos = (datetime.now() - data_nascimento).days // 365
 meses = floor(((datetime.now() - data_nascimento).days / 365) * 12)
 dias = (datetime.now() - data_nascimento).days
 if anos == 1:
    return f'Você tem: {anos} ano de idade, {meses} meses e {dias} dias vividos.'
 else:
    return f'Você tem: {anos} anos de idade ou {meses} meses e {dias} dias vividos.'
 
data_nascimento = datetime.strptime(
  input('Informe a data de nascimento (formato dd/mm/AAAA): '), "%d/%m/%Y")
nascimento = (calcula_idade(data_nascimento))

data_atual = date.today()
data_de_cadastro = data_atual.strftime('%d/%m/%Y')

# Sorteio para os Cadastrados
cartoes = ['R$50,00','R$250,00','R$120,00']
sorteio = random.choice(cartoes)

'''
| Módulo 2 - Gerar apresentação do Usuário

Funcionalidade do módulo 2 - Mensagem de Boas-vindas!
Usando os dados obtidos do módulo 1, exiba as seguintes informações:

1- Olá (nome do funcionário), seu registro foi concluido com sucesso no dia (data de cadastro no 
formato dd/mm/aaaa).
Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de valor sorteado.
'''
print(f'\nOlá {nome}, você tem {nascimento} \nSeu registro foi concluido com sucesso no dia {data_de_cadastro}. '
      f'\nParabéns, houve um sorteio e você ganhou um cartão de compras no valor de {sorteio}')