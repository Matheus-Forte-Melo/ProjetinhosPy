pessoas = []
dados = []
while True:
    dados.append(str(input('Digite o nome do usuário: ')))
    dados.append(float(input('Digite o peso do usuário: ')))
    pessoas.append(dados[:])
    if len(pessoas) == 1:
        leve = pesado = dados[1]
    if dados[1] > pesado:
        pesado = dados[1]
    if dados[1] < leve:
        leve = dados[1]
    dados.clear()

    confirmacao = str(input('Quer adicionar outro usuário? [S/N]')).upper()
    if confirmacao in ('NÃO', 'N', 'NAO'): break
    elif confirmacao not in ('SIM', 'S'): print('\033[1;31mERRO:\033[m Digita certo CARALHO')
print('=-'*25)
print('As pessoas mais pesadas são:', end=' ')

for pessoa in pessoas:
    if pessoa[1] == pesado:
        print(f'[{pessoa[0]}]', end=' ')
print('\nAs pessoas mais leves são:', end=' ')

for pessoa in pessoas:
    if pessoa[1] == leve:
        print(f'[{pessoa[0]}]', end=' ')
print(f'\nVocê inseriu {len(pessoas)} usuário(s)!')
