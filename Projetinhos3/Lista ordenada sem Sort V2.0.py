lista = []

for c in range(0, 5):
    valor = int(input('Digite o valor: '))
    posicao = 0
    for n in range(len(lista)):
        if valor > lista[n]:
            posicao = n + 1
        else:
            break
    lista.insert(posicao, valor)
    print(f'O valor digitado foi {valor} na posição {posicao}.')

print(f'Lista ordernada = {lista}')
