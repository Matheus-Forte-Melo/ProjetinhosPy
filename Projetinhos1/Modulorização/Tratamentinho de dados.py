from UtilidadesCeV import Dado
from UtilidadesCeV import Moeda

valor = Dado.leiaDin()
escolha = str(input('Dolar ou Real?: ')).strip().lower()

if escolha in ('dolar', 'dol', 'd', 'dolár', 'dolares'):
    moeda = '$'
else:
    moeda = 'R$'
aum = int(input('Digite a porcentagem de aumento: '))
desc = int(input('Digite a porcentagem de desconto: '))
Moeda.resumo(valor, aum, desc, moeda)





