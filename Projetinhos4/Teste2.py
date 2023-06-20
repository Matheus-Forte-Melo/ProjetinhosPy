pontos = [[], [], []]
for i in range(0, 3):
    pontos[i].append(int(input(f'Digite o ponto X{i+1}: ')))
    pontos[i].append(int(input(f'Digite o ponto Y{i+1}: ')))
print('-='*15)

matriz = [[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]

for l in range(0, 3):
    for c in range(0, 5):
        if c < 2:
            matriz[l][c] = pontos[l][c]
            print(f'[{matriz[l][c]:^3}]', end='')
        elif c == 2:
            print(f'[{1:^3}]|', end='')
        if c > 2:
            matriz[l][c] = pontos[l][c-3]
            print(f'{matriz[l][c]:^3}', end='')
    print()

a, b, c, determinante = 0, 1, 2, 0
for x in range(0, 3):
    determinante += matriz[0][a] * matriz[1][b] * matriz[2][c]
    a, b, c = a+1, b+1, c+1

a, b, c = 4, 3, 2
for x in range(0, 3):
    determinante -= matriz[0][a] * matriz[1][b] * matriz[2][c]
    a, b, c = a-1, b-1, c-1

print('O resultado é', determinante)
if determinante == 0: print(f'Os 3 pontos estão alinhados!')
else: print(f'Os 3 pontos não estão alinhados!')
