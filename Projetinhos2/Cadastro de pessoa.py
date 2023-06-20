dados = {}
arquivo = []
somaIdade = 0
while True:
    dados['nome'] = str(input('Digite o nome: '))
    dados['idade'] = int(input('Digite a idade: '))
    somaIdade += dados['idade']
    while True:
        dados['sexo'] = input('Digite o sexo [M|F]: ').upper()
        if dados['sexo'] in ['M', 'F']:
            break
        print(f'ERRO! VOCÊ DIGITOU {dados["sexo"]}!')

    while True:
        confirm = str(input('Cadastrar outro? [S|N]: ')).upper()
        if confirm in ['S', 'N', 'SIM', 'NAO', 'NÃO']:
            break
        print(f'ERRO! VOCÊ DIGOU {confirm}')
    arquivo.append(dados.copy())
    if confirm in ['N', 'NÃO', 'NAO']:
        break

print('=-'*15)
print(f'A) Existem {len(arquivo)} cadastros.\nB) A média de idade é de {somaIdade / len(arquivo)}\nC) Mulheres: ', end='')
for n in range(len(arquivo)):
    if arquivo[n]['sexo'] == 'F':
        print(f'[{arquivo[n]["nome"]}]', end=' ')

print('\nD) Pessoas acima da média de idade: ')
for dicionario in arquivo:
    if dicionario['idade'] > somaIdade / len(arquivo):
        print(f'Nome == {dicionario["nome"]} | Sexo == {dicionario["sexo"]} | Idade == {dicionario["idade"]}')
print('>>>>>FIM<<<<<')  # for c, v in dicionario.items dai dava de usar {c} == {v}

