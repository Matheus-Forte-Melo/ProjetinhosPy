matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = somaCol3 = maiorValor2 = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor na posição [{linha}][{coluna}]: '))

print('=-'*25)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somaPar += matriz[linha][coluna]
        if coluna == 2:  # matriz[linha][coluna] == matriz[linha][2]
            somaCol3 += matriz[linha][coluna]
        if linha == 1:
            if coluna == 0:
                matriz[linha][coluna] = maiorValor2
            if matriz[linha][coluna] > maiorValor2:
                maiorValor2 = matriz[linha][coluna]
    print()

print(somaPar, somaCol3, maiorValor2)

