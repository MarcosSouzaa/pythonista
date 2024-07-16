#Datetime e Tempo

# Tomar decisão de quando o programa deve rodar
# Vou importar o módulo datetime

from datetime import datetime

print(datetime.now()) # 2024-07-15 20:44:26.916658
print(datetime.now().day) # 15
print(datetime.now().month) # 7
print(datetime.now().year) # 2024

# Como criar uma data de lançamento de um aplicatvo
data_de_lancamento = datetime(2024, 7, 15, 14) #Data de lançamento do aplicativo :  2024-07-15 14:00:00
print(f'Data de lançamento do aplicativo :  { data_de_lancamento}')

'''
- Quero receber informação vinda do usuário
- Qual a data de lançamento o usuário sugere
- como o retorno será sempre uma string, preciso converter para o type datetime
- como segundo parâmetro, vou passar qual o tipo de formatação eu espero para essa data:
15/07/2024
'''
data_de_lancamento = datetime.strptime(input('\nQuando devemos lançar o aplicativo?\n'), '%d/%m/%Y')
print(type(data_de_lancamento))
print(data_de_lancamento)

# Vamos supor que eu precise calcular o intervalo entre uma data e outra
# Ex. quanto tempo possuo até a data do lançamento
data_atual = datetime.now()
prazo = data_de_lancamento - data_atual
print(f'Dias que faltam para o lançamento: {prazo.days}')

#Calcule quantos dias faltam até o seu aniversário

data_aniversário = datetime.strptime(input('\nDigite a data do seu aniversário:\n'), '%d/%m/%Y')
print(f'Data de aniversário: {data_aniversário}' )

data_de_hoje = datetime.now()
periodo = data_aniversário - data_de_hoje
print(f'Faltam {periodo.days} dias para seu aniversário')

# Outra forma
aniversario = datetime(2024,9,19)
dias_para_aniversario = aniversario - datetime.now
print(dias_para_aniversario)