dicionario = {}

dicionario['Aluno'] = str(input('Digite o nome: '))
dicionario['Média'] = float(input('Digite a media do aluno: '))

if dicionario['Média'] >= 6:
    dicionario['Situação'] = 'Aprovado'
else:
    dicionario['Situação'] = 'Reprovado'
if dicionario['Média'] > 10 or dicionario['Média'] < 0:
    dicionario['Situação'] = 'Inválida'


for c, e in dicionario.items():
    print(f'{c} é igual a {e}')