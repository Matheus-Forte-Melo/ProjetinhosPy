numeros = [[], []]
num = 0
for c in range(0, 7):
    num = int(input(f'Digite o {c+1}° número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort(), numeros[1].sort()
print('=-'*25)
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores impares digitados foram: {numeros[1]}')