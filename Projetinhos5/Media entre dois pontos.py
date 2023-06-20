print('+=+=+= Ponto médio entre dois pontos +=+=+=')
X1 = int(input('Digite a cordenada do primeiro X: '))
Y1 = int(input('Digite a cordenada do primeiro Y: '))
X2 = int(input('Digite a segundo do primeiro X: '))
Y2 = int(input('Digite a segundo do primeiro Y: '))

pontomedioX = (X1 + X2)
pontomedioY = (Y1 + Y2)

if pontomedioX % 2 != 0:
    pontomedioX = str(pontomedioX) + '/2'
else: pontomedioX /= 2
if pontomedioY % 2 != 0:
    pontomedioY = str(pontomedioY) + '/2'
else: pontomedioY /= 2

print(f'Ponto médio = ({pontomedioX};{pontomedioY})')
