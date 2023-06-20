from time import sleep


def contador(inicio, fim, passo):
    print(f'== Contagem de {inicio} -> {fim} de {passo} em {passo} ==')
    if inicio < fim:
        for c in range(inicio, fim+1, passo):
            if c == fim:
                print(c, end='.')
            else:
                print(c, end=', ')
            sleep(0.30)
    else:
        for c in range(inicio, fim-1, passo*-1):
            if c == fim:
                print(c, end='.')
            else:
                print(c, end=', ')
            sleep(0.30)
    print('')


contador(0, 10, 1)
contador(10, 0, 2)
print(f'{" PERSONALIZE SUA CONTAGEM ":=^30}')
i = int(input('Inicio: '))
f = int(input('   Fim: '))
p = int(input(' Passo: '))
contador(i, f, p)
