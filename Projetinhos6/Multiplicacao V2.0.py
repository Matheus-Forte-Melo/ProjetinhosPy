num = int(input('Digite um numero: '))
quant = int(input('Digite o numero de elementos da tabuada: '))

for c in range(1, quant):
    print(f'{num} X {c} = {num * c}')
