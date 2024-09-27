X = 1

if X < 0:
    print('A')
elif 1 <= X <= 3:
    print('B')
elif X < 10:
    print('C')
else:
    print('D')


'''
A ordem dos if/ elif/ elif importa!
A primeira condição verdadeira é aquela que terá o bloc de codigo associado executado.

Nesse caso, com x = 2, a primeira condição verdadeira é "x >= 1 and x <= 3".
portanto, o programa irá printar a letra B.
'''