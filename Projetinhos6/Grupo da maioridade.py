from datetime import date

quant = int(input('Digite a quantidade de pessoas: '))
hoje = date.today().year
contadorMenor = 0
contadorMaior = 0

for c in range(0, quant):
    idade = hoje - int(input(f'Ano de nascimento da {c+1}ª pessoa: '))
    if idade < 18:
        contadorMenor += 1
    else:
        contadorMaior += 1

if contadorMaior > 1 or contadorMaior == 0: print(f'Existem {contadorMaior} maiores de idade,', end=' ')
else: print(f'Existe {contadorMaior} maior de idade,', end='')
if contadorMenor > 1 or contadorMenor == 0: print(f'e {contadorMenor} menores de idade')
else: print(f'e {contadorMenor} menor de idade')
