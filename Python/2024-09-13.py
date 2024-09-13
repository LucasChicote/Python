'''
Este programa lê o nome e o sobrenome do usuário e o cumprimento 

'''

nome = input('Insire o nome:')
sobrenome = input('Insire o sobrenome:')

print('Olá,', nome, sobrenome, ',Bom dia')

cor = input('Insire a sua cor favorita:')
comida = input('Qual a sua comida predileta ?')

print('Essa cor é boa', cor, comida, 'Eu adoro essa comida também hehe')



print('Em que ano você nasceu ?')
ano_nascimento = int(input())

idade = 2024 - ano_nascimento
print('Sua idade é no máximo', idade, 'anos')

if ano_nascimento >= 2000 and ano_nascimento <= 1901:
    print('Você nasceu no século XX')
elif ano_nascimento >= 2001 and ano_nascimento <= 2100:
    print('Você nasceu no século XXI')
else:
    print('...sério?')
    
# idade - 2024 - ano_nascimento
# print('Sua idade é no máximo', idade, 'anos')


nome2 = input('Coloque seu nome secundário:')
sobrenome2 = input('Coloca ai seu sobrenome, se tiver:')

print('Bom dia', nome2, sobrenome2, 'Seja bem vindo ao menicomio')





