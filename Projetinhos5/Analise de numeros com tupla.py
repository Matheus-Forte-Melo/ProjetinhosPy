# valores = tuple(int(input('Digite valores '))for c in range(1, 5))
'''num = (int(input('Digite um numero: ')),
       (int(input('Digite um numero: ')),
        (int(input('Digite um numero: ')),
         (int(input('Digite um numero: ')))))),

if num.count(9) == 1:
    print(f'O numero 9 apareceu uma vez')'''

a = int(input('Digite um valor: '))
b = int(input('Digite mais um valor: '))
c = int(input('Digite outro valor: '))
d = int(input('Digite o ultimo valor: '))
tupla = (a, b, c, d)

print('=*'*10, f'\nO número nove apareceu {tupla.count(9)} vez(es)')
if 3 in tupla:
    print(f'O 3 foi digitado na {tupla.index(3)+1} posição.')
print('Os numeros pares são: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')

#https://www.youtube.com/watch?v=1u7oA8ckjAc&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=93





