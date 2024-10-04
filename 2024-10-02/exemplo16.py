compras = ['Arroz', 'Banana', 'Tomate']

# a cada passo do "for", o item terá como valor um dos conteudos da listas
for item in compras:
    print('Preciso comprar', item)
    
    
compras.append('uva')
print('Agora a lista ficou assim:')
print(compras)




print('\n----\n')
for item in compras:
    print('Preciso adicionar', item)