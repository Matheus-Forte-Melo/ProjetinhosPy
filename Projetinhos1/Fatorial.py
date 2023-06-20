

def fatorial(val=1):
    result = 1
    for c in range(val, 0, -1):
        result *= c
    return result


f1 = fatorial(4)
f2 = fatorial(10)
f3 = fatorial(  )

print(f1, f2, f3)
'''
valor = int(input('Digite um valor: '))
print(f'O fatorial de {valor} é igual a: {fatorial(valor)}')
'''