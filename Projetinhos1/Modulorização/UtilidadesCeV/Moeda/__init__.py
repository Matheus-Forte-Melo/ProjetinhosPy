#  Calcula a metade de um dado valor. Contém uma parametro adicional de retorno (Meio besta, só pelo teste)
def metade(valor=0, retorno=True, format=True, mon='R$'):
    res = valor / 2
    if retorno:
        return res if format is False else moeda(res, mon)
    else:
        print(f'A metade de {valor} é {valor / 2}')


#  Calcula o dobro de um dado valor. Contém uma parametro adicional de retorno (Meio besta, só pelo teste)
def dobro(valor=0, retorno=True, format=True, mon='R$'):
    res = valor * 2
    if retorno:
        return res if format is False else moeda(res, mon)
    else:
        print(f'O dobro de {valor} é {valor * 2}')


#  Calcula o aumento de um dado valor com uma porcentagem. Contém uma parametro adicional de retorno (besta)
def aumentar(porcent=0, valor=0, retorno=True, format=True, mon='R$'):
    res = valor + ((valor / 100) * porcent)
    if retorno:
        return res if format is False else moeda(res, mon)
    else:
        print(f'O aumento de {porcent}% no valor {valor} é igual a {valor + ((valor / 100) * porcent)}')


#  Calcula o desconto de um dado valor com uma porcentagem. Contém uma parametro adicional de retorno (besta)
def diminuir(porcent=0, valor=0, retorno=True, format=True, mon='R$'):  # Format diz se deve ou não formatar monetariamente
    res = valor - ((valor / 100) * porcent)
    if retorno:
        return res if format is False else moeda(res, mon)
    else:
        print(f'O desconto de {porcent}% no valor {valor} é igual a {valor - ((valor / 100) * porcent)}')


# Formata o preço em determinada moeda
def moeda(val=0, moeda='R$'):
    return f'{moeda:}{val:.2f}'.replace('.', ',')


def resumo(val=0, aumento=0, reducao=0, monet='R$'):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^25}')
    print('-'*30)
    print(f'{"Preço analisado:":<20} {moeda(val, monet)}')
    print(f'{"Dobro do preço:":<20} {dobro(val, format=True, mon=monet)}')
    print(f'{"Metade do preço:":<20} {metade(val, format=True, mon=monet)}')
    print(f'{f"{aumento}% de aumento:":<20} {aumentar(aumento, val, format=True, mon=monet)}')
    print(f'{f"{reducao}% de redução:":<20} {diminuir(reducao, val, format=True, mon=monet)}')
    print('-'*30)


