soma = 0
contadorPar = 0

for c in range(1, 7):
    num = int(input(f'Digite o {c}° numero: '))
    if num % 2 == 0:
        soma += num
        contadorPar += 1

print('='*45)

if soma != 0 and contadorPar > 1:
    print(f'Foram detectados {contadorPar} numeros pares.\nA soma de todos esses numeros é igual a {soma}!')
elif contadorPar == 1:
    print(f'Foi detectado apenas um numero par.\n\033[1;33mERRO\033[m:Não é possivel fazer soma com apenas um elemento.')
else:
    print(f'\033[1;33mERRO\033[m:Nenhum numero inserido é par!!!')
