import datetime
#  help(datetime)


def contador(a=1, b=1, c=1):
    '''
    :param a: Inicio da contagem
    :param b: Onde a contagem deve parar
    :param c: O pulo de contagem
    :return: Caso erro. Retorno nulo.
    '''
    if b < 0 or c < 0:
        print('ERRO, VALORES 2 E 3 NÃO PODEM SER NEGATIVO')
        return
    cont = a
    while cont < b:
        print(cont, end=' ')
        cont += c

    print('FIM')

help(contador)





