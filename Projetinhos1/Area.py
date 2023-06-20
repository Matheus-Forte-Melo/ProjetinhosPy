def area(largura, comprimento):
    print(f'A área do terreno {largura}x{comprimento}M   é de {largura*comprimento} M²')


# Programa principal
print('Calculo de área!')
print('=+'*7)
l = float(input('Digite a largura do terreno (m): '))
c = float(input('Digite o comprimento do terreno (m): '))
area(l, c)