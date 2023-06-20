

def notas(*notas, situação=True):
    ficha = {}
    soma = media = 0
    maior = menor = notas[0]
    for c in range(len(notas)):
        # Somando
        soma += notas[c]
        # Analisando o maior e menor
        if notas[c] > maior:
            maior = notas[c]
        if notas[c] < menor:
            menor = notas[c]
    media = soma / len(notas)
    # Criando o dicionario
    ficha['total'] = soma
    ficha['maior'] = maior
    ficha['menor'] = menor
    ficha['média'] = media
    if situação:
        if media >= 6:
            ficha['situação'] = 'Nota em verde'
        else:
            ficha['situação'] = 'Nota em vermelho'
    return ficha


print(notas(1, 2, 10, -1, 5) )
