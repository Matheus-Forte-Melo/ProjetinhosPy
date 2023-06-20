from math import sqrt
print('+=+=+= Distância entre dois pontos +=+=+=')
X1 = int(input('Digite a cordenada do primeiro X: '))
Y1 = int(input('Digite a cordenada do primeiro Y: '))
X2 = int(input('Digite a segundo do primeiro X: '))
Y2 = int(input('Digite a segundo do primeiro Y: '))
distancia = sqrt((X1 - X2) ** 2 + (Y1 - Y2) ** 2)

print('=+'*10, f'\nEm um plano cartesiano onde:\nPonto A = ({X1},{Y1})\nPonto B = ({X2},{Y2})')
print(f'A distância entre ponto A e ponto B é de \033[32;1m{distancia} unidades!\033[m\n' + '+=' * 10)
# Programa feito inicialmente com a bunda -> usando Vars toscas e substituiveis pela formula acima

