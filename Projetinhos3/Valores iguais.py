lista = []
confirmacao = ''

while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Inserção negada. Valor já inserido.')
    else:
        print('Valor inserido com sucesso.')
        lista.append(valor)

    while confirmacao not in ('nao', 'sim', 'n', 's'):
        confirmacao = str(input('Deseja inserir outro valor? [S/N]')).lower()
    if confirmacao in ('nao', 'n'):
        break
    confirmacao = ''

print(15*'=*',f'\nValores únicos adicionados: {lista}.')