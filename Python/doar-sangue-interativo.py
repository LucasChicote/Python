print('Qual sua idade?')
idade = int(input())

if idade >= 70 or idade < 16:
    print('Não pode doar sangue')

elif idade == 16 or idade == 17:
    print('Você tem autorização dos pais?  (S/N)')
    resposta = input()
    if resposta == 's' or resposta == 'S': 
        print('Pode doar sangue.')
elif idade >= 18:
    print('Pode doar sangue')
if idade >= 69:
    print('A pessoa pode doar sangue, porém, precisa ser um doador já registrado')
    if resposta == 'n' or resposta == 'N':
        print('A pessoa não pode doar sangue sozinha')
    
         