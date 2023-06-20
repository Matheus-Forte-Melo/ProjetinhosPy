#  Calcula a metade de um dado valor. Contém uma parametro adicional de retorno (Meio besta, só pelo teste)
def metade(valor=0, retorno=True):
    if retorno:
        return str(f'R${valor / 2}')
    else:
        print(f'A metade de R${valor} é {valor / 2}')


#  Calcula o dobro de um dado valor. Contém uma parametro adicional de retorno (Meio besta, só pelo teste)
def dobro(valor=0, retorno=True):
    if retorno:
        return str(f'R${valor * 2}')
    else:
        print(f'O dobro de R${valor} é {valor * 2}')


#  Calcula o aumento de um dado valor com uma porcentagem. Contém uma parametro adicional de retorno (besta)
def aumentar(porcent=0, valor=0, retorno=True):
    if retorno:
        return str(f'{valor + ((valor / 100) * porcent)}')
    else:
        print(f'O aumento de {porcent}% no valor R${valor} é igual a R${valor + ((valor / 100) * porcent)}')


#  Calcula o desconto de um dado valor com uma porcentagem. Contém uma parametro adicional de retorno (besta)
def diminuir(porcent=0, valor=0, retorno=True):
    if retorno:
        return str(f'{valor - ((valor / 100) * porcent)}')
    else:
        print(f'O desconto de {porcent}% no valor R${valor} é igual a R${valor - ((valor / 100) * porcent)}')
