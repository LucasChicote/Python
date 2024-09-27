# Menu para cadatro de dados de doador de sangue

nome = 'Não consta'
tipo_sanguineo = 'Não consta'


while continua_programa:
    print('Escolha uma opção:')
    print('1 - cadastrar nome:')
    print('2 - cadastrar tipo sanguineo:')
    print('3 - ecerrando programa...')

    comando = input()
    if comando == '1':
        print('Digite o nome')
        nome = input()
    elif comando == '2':
        tipo_sanguineo = input()
    elif comando == '3':
        continua_programa = input()
    else:
        print('Comando não reconhecido')


print('Informações do doador:')        
print('nome:', nome)        
print('Tipo sanguineo:', tipo_sanguineo)        