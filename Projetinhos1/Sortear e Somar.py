from random import randint


def sorteiaLista(lst):
    print(f'Sorteando os valores: ', end='')
    for c in range(5):
        lst.append(randint(1, 10))
        print(f'[{lst[c]}]', end=' ')
    print(f'\nLista = {lst}')


def somaPar(lst):
    soma = 0
    for e in lista:
        if e % 2 == 0:
            soma += e
    print(f'A soma dos pares da lista é igual a {soma}!')


# Programa Principal //Reminder -> Tudo oq faço em lst, copia para lista
lista = []
sorteiaLista(lista)
somaPar(lista)