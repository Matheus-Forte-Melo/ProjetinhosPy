

def fatorial(val=1, show=True):
    '''
    :param val: O valor a ser inserido para o calculo do fatorial
    :param show: Se show=True: Mostra os passos do calculo | Se show=False retorna só o resultado
    :return: Retorna o resultado do fatorial em ambos casos
    '''
    result = 1
    cont = val
    for c in range(val, 0, -1):
        result *= c

        if show:
            if c != 1:
                print(c, end=' x ')
            else:
                print(f'{c} = ', end='')

    return result


print(fatorial(10, show=True))
print(fatorial(10, show=False))

