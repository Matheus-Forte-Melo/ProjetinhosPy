'''def mostra():
    print('-='*10)


# Programa principal
mostra()
print('       Aiinnn')
mostra()
mostra()
print('       Zéeeee')
mostra()
mostra()
print('       Damanga')
mostra()'''
'''
def mensagem(msg):
    print('====================')
    print(f'{msg:^20}')
    print('====================')


mensagem('Half Life 3!')'''
'''def soma(a, b):
    print(f'A = {a}, B = {b}')
    s = a + b
    print(s)


# Programa Principal
soma(a=1, b=2)
soma(b=3, a=4)
soma(a=6, b=2)'''
'''
def contador(*num):
    cont = len(num)
    for c in num:
        print(f'[{c}]', end=' ')
    print(f'\nVocê inseriu {cont} números! ')


# Programa principal
contador(3,4,5,2,3,1)'''
'''
dicionario = {}
dicionario["dançakuduro"] = 'Ain'
dicionario["ximbas"] = 'Oin'

print(dicionario)

for c, v in dicionario.items():
    print(c,v)'''


def dobrador(amonguis):
    for pos in range(len(amonguis)):
        amonguis[pos] = amonguis[pos] * 2
    print(f'A lista dobrada é igual à: {amonguis}')


# Programa principal
lista = []
for c in range(5):
    lista.append(int(input('Digite um valor: ')))
dobrador(lista)

# Tudo que eu faço em AMONGUIS muda a lista.


