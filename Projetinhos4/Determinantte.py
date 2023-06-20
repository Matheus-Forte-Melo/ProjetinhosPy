Xa = int(input('Digite o valor do ponto Xa: '))
Ya = int(input('Digite o valor do ponto Ya: '))
Xb = int(input('Digite o valor do ponto Xb: '))
Yb = int(input('Digite o valor do ponto Yb: '))
Xc = int(input('Digite o valor do ponto Xc: '))
Yc = int(input('Digite o valor do ponto Yc: '))
print('-='*15)
matriz = [[Xa, Ya, 1, Xa, Ya], [Xb, Yb, 1, Xb, Yb], [Xc, Yc, 1, Xc, Yc]]

for l in range(0, 3):
    for c in range(0, 5):
        if c < 3:
            print(f'[{matriz[l][c]:^3}]', end='')
        elif c == 3:
            print(f'| {matriz[l][c]:^3}', end=' ')
        else:
            print(f'{matriz[l][c]:^3}', end=' ')
    print()
a = determinante = teste = 0
b = 1
c = 2
for x in range(0, 3):
    determinante += matriz[0][a] * matriz[1][b] * matriz[2][c]
    a += 1
    b += 1
    c += 1
a = 4
b = 3
c = 2
for x in range(0, 3):
    determinante -= matriz[0][a] * matriz[1][b] * matriz[2][c]
    a -= 1
    b -= 1
    c -= 1

print('O resultado é', determinante)
if determinante == 0:
    print(f'Os 3 pontos estão alinhados!')
else:
    print(f'Os 3 pontos não estão alinhados!')
