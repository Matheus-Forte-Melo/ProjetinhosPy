from datetime import date
dados = {}

dados['nome'] = str(input('Digite seu nome: ')).title()
dados['idade'] = int(input('Digite seu ano de nascimemento: '))
dados['idade'] = date.today().year - dados['idade']
dados['sexo'] = str(input('Digite seu sexo [M|F]: ')).upper()
dados['carteira de trabalho'] = int(input('Digite sua carteira de trabalho: '))

if dados['carteira de trabalho'] != 0:
    dados['ano de contratação'] = int(input('Digite o ano de contratação: '))
    dados['salário'] = float(input('Digite seu salário: '))
    if dados['sexo'] == 'F':
        dados['aposentadoria'] = dados['idade'] + 30
    else:
        dados['aposentadoria'] = dados['idade'] + 35

print('-=+'*7)
for c, v in dados.items():
    print(f'{c} tem valor de {v}')
print(dados)