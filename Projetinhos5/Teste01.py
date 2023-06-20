from random import randint

lista = ['PEDRA', 'PAPEL','TESOURA']

jogador = int(input('Digite 1 para PEDRA, 2 para PAPEL e 3 para TESOURA'))
jogador = jogador -1

computador = randint(0,2)

if jogador == computador:
    print('Empate!')
elif jogador == 0 and computador == 2:
    print('Você venceu!')
    print(f'{lista[jogador]} ganha de {lista[computador]} ')
elif jogador == 1 and computador == 0 :
    print('Você venceu!')
    print(f'{lista[jogador]} ganha de {lista[computador]} ')
elif jogador == 2 and computador == 1:
    print('Você venceu!')
    print(f'{lista[jogador]} ganha de {lista[computador]} ')
else:
    print('Computador venceu!')
    print(f'{lista[computador]} ganha de {lista[jogador]} ')