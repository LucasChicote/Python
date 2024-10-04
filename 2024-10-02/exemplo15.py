texto1 = 'bom dia'
texto2 = 'bom dia, estamos na aula de computational thinking'

for caractere in texto1:
    print(texto1)

a = 0 
for caractere in texto2:
    if caractere == ' ':
        a += 1

print('O texto2 tem', a, 'as')