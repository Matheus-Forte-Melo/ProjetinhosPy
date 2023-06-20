'''import random
linha = int(input('Digite o numero de linhas: '))
coluna = int(input('Digite o numero de colunas: '))

matriz = []  # Cria matriz vazia.
for i in range(linha):  # Repete com o número de linhas inseridas, se 4 lido, 4 repetições.
    linhaAUX = [0] * coluna  # Atribui a variavel linha uma lista repleta com zeros, cada zero é uma coluna
    matriz.append(linhaAUX)  # Insere o valor atribuido a matriz vazia.

min = int(input('Digite o min: '))
max = int(input('Digite o max: '))

for l in range(linha):
    for c in range(coluna):
        matriz[l][c] = random.randint(min, max)

print("Matriz criada:")
for linha in matriz:
    print(linha)'''
from random import randint
lista = []

for c in range(0, 6):
        num = randint(0, 6)
        if num not in lista:
            lista.append(num)
        elif num in lista:
            while True:
                num = randint(0, 6)
                if num not in lista:
                    lista.append(num)
                    break
print(lista)

