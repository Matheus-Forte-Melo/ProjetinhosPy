from time import sleep
from random import randint
resultado, jogo = [], {}
quantidade = int(input('Quantos jogadores?: '))

for c in range(quantidade):  # Inserindo o nome dos jogadores
    nome = str(input(f'Digite o nome do {c+1}° jogador: '))
    jogo[nome] = randint(1, 6)  # Dá de inserir mais paradas, só botar o identificador entre caixolas.

print('-+=-=+'*2, 'RESULTADOS', '+=-=+-'*2)  # Printando os resultados
for c, v in jogo.items():
    print(f'O(a) {c} tirou {v}!')
    sleep(0.35)

print('-+=-=+'*2, 'RANKING', '+=-=+-'*2)  # Organizando e printando o ranking
pos, resultado = 0, sorted(jogo.items(), key=lambda item: item[1], reverse=True)
for n in range(len(resultado)):
    if n == 0:
        print(f'{n+1}°: {resultado[n][0]} | {resultado[n][1]}')
    else:
        if resultado[n][1] == resultado[n-1][1]:
            print(f'{resultado[n][0]} | {resultado[n][1]} ')
        else:
            print(f'{n+1}°: {resultado[n][0]} | {resultado[n][1]}')

