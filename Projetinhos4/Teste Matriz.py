from random import randint
'''
matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for l in range(0, 5):
    for c in range(0,4):
        matriz[l][c] = randint(0, 100)
        print(f'[{matriz[l][c]:^6}]', end='')
    print()'''
linhas = int(input('Digite o numero de linhas da matriz: '))
colunas = int(input('Digite o numero de colunas da matriz:'))
matriz = [[0 for c in range(0, colunas)]for l in range(0, linhas)] # matriz [[0,0,0,0], [0,0,0,0]]

min = int(input('Digite o número minimo de numeros: '))
max = int(input('Digite o número maximo de numeros: '))

for l in range(linhas):
    for c in range(colunas):
        matriz[l][c] = randint(min,max)
        print(f'[{matriz[l][c]:^5}]', end='')
    print()




