from uteis import numeros

valor = int(input('Digite um valor: '))
fat = numeros.fatorial(valor)
print(f'O fatorial de {valor} é {fat}')
print(f'O dobro de {valor} é {numeros.dobro(valor)}')
print(f'O triplo de {valor} é {numeros.triplo(valor)}')
