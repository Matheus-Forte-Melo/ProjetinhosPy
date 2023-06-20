num = int(input('Digite um numero: '))
contador = 0

for c in range(1, num+1):
    if num % c == 0:
        print(f'\033[1;32m{c}\033[m', end=' ')
        contador += 1
    else:
        print(f'\033[1;33m{c}\033[m', end=' ')

print('\n' + '='*45)

if contador == 2:
    print(f'\nO numero {num} é primo!\nPois é divisivel por apenas 2 numeros!')
else:
    print(f'\nO numero {num} não é primo!\nPois é divisivel por mais de 2 numeros!')