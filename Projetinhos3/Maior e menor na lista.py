lista = []
booleano = False

for pos, num in enumerate(range(0, 5)):
    lista.append(int(input(f'Digite um numero para a posição {pos}: ')))

    if not booleano:
        maior = menor = lista[num]
        booleano = True

    if lista[num] > maior:
        maior = lista[num]
    if lista[num] < menor:
        menor = lista[num]

print(15*'+=', f'\nVocê digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} na(s) posições', end=' ')
for pos, num in enumerate(lista):
    if num == maior:
        print(pos, end=' ')

print(f'\nO menor valor digitado foi {menor} na(s) posições', end=' ')
for pos, num in enumerate(lista):  # for blablabla in enumarte(lista )
    if num == menor:
        print(pos, end=' ')
