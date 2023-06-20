import random
tupla = (random.randint(0, 25), random.randint(0, 100), random.randint(0, 100),
         random.randint(0, 100), random.randint(0, 100))
print('Os valores sorteados foram: ', end='')
for num in tupla:
    if num == tupla[4]:  # Se o num for == ao numero na posição 4 da tupla.
        print(num, end='.')
    else:
        print(num, end=', ')
print(f'\nO maior entre eles é {max(tupla)} e o menor {min(tupla)}')
