print('Qual a tabuada desejada?')
n = int(input())
multiplo = 1
while multiplo < 11:
    print(n, 'x', multiplo, '=', n*multiplo)
    multiplo += 1
    
for n in range(1,11):
    print('Vou mostrar a tabuada do',n)
    for multiplo in range(1, 11):
        print(n, 'x', multiplo, '=', n*multiplo)
        
    print('\n-------------\n')