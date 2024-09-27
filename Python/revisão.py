
import datetime

data = datetime.datetime.now()

Dia = data.day
Mês = data.month
Ano = data.year


ano_atual = data.year

nome = input('Escreva seu nome ao lado:')
sobrenome = input('Escreva seu sobrenome ao lado:')


print ('Digite seu ano de nascimento:')
Data_nascimento = int(input())

idade = ano_atual - Data_nascimento
print('Olá, seja bem-vindo(a)',nome, sobrenome)

print('Estamos no ano de', ano_atual, 'por tanto, você tem', idade, 'anos')


if idade >= 1 and idade <= 5:
    print('A criança pode entrar para a escolinha')
elif idade >= 4 and idade <= 6:
    print('A criança está no ensino fundamental I')
elif idade >= 6 and idade <= 15:
    print('A pessoa está no ensino fundamental II')
elif idade == 15 or idade == 18:
    print('A pessoa está no ensino médio')
elif idade > 18:
    print(' Ou a pessoa está finalizando o ensino médio, ou ela reprovou de ano, ou ela esta entrando para a faculdade')
else:
    print('A pessoa é não estuda')
 
