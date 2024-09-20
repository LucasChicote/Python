# Programa -> critério de idade para dorar sangue

# Para doar sangue, a pessosa precisa ter idade de 16 até 69 anos.

#OBS: se é menor de idade (< 18 anos), precisa de autroização dos pais/responsaveis
#OBS: se é maior de 60 anos (>= 60 anos), precisa já ser doador.

#Exemplo:

ANO_ATUAL = 2024

import datetime

data  = datetime.datetime.now()
ANO_ATUAL = data.year

print('Em que ano você nasceu?')
ano_nascimento = int(input())

idade = ANO_ATUAL - ano_nascimento

print('Estamos no ano', ANO_ATUAL)
print('Portanto você fez o fará', idade, 'anos neste ano')


#Primeiro pergunto o ano de nascimento para calcular a idade


nome = input('Digite o seu nome:')
sobrenome = input('Digite o seu sobrenome:')
peso = int(input('Qual o seu peso?'))
altura = float(input('Qual a sua altura?'))

print('Seja bem vindo', nome, sobrenome)
print('Esse é seu peso ?', peso, 'Essa é sua altura?', altura)

print('Qual o seu ano de nascimento?')
ano_nascimento = int(input())
idade = ANO_ATUAL - ano_nascimento 

print('Sua idade é', idade, 'ano')

if idade >= 18 and idade <= 59: #ou tambem posso escrever 16 <= idade <= 69
    print('Pode doar sangue')
elif idade == 16 or idade == 17:
    print('Pode doar sangue se tiver autorização dos pais')
elif idade >= 60 and idade <= 69:
    print('Pode doar sangue contanto que seja doador já resgistrado.')    
else:
    print('Não é possivel doar sangue com essa idade')
    
