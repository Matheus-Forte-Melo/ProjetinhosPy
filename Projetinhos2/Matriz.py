import random
lin = int(input('Digite o número de linhas: '))
col = int(input('Digite o número de colunas: '))
matriz = []

for l in range(lin):  # Cria a matriz com base nas parada de cima
    matriz.append([])
    for c in range(col):
        matriz[l].append(0)

for l in range(lin):  # Insere valores randômicos e printa
    for c in range(col):
        matriz[l][c] = random.randint(0,101)
        print(f'[{matriz[l][c]:^4}]', end=' ')
    print()

'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for lin in range(3):
    for col in range(3):
        print(matriz[lin][col], end=' ')
    print()'''