'''#print(lancheT[-2:])  # Tudo depois de pizza
#print(lancheT[:-2])  # Tudo antes de pizza

lancheT = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for ponteiro in range(0, len(lancheT)):
    print(f'Vou comer {lancheT[ponteiro]} no prato {ponteiro+1}')
print('Puta merda comi pra karalho.\n'+'+=' *25)

#  Usar esse metodo caso precise mostrar a posição
#  Usar o metodo FOR PONTEIRO IN LANCHET para caso não precise.

for ponteiro in lancheT[3:]:
    print(ponteiro)
for ponteiro in lancheT[:3]:
    print(ponteiro)
for ponteiro in lancheT[:-1]:
    print(ponteiro)
for ponteiro in lancheT[2]:
    print(ponteiro)

for c in enumerate(lancheT):
    print(c)
for pos, c in enumerate(lancheT):
    print(c, pos)
for pos, c in enumerate(lancheT[1]):
    print(c, pos)
for pos, c in enumerate(lancheT[1:4]):
    print(c, pos)

print(sorted(lancheT))
print(lancheT)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b

print(c)  # Ou print(a + b)
print(sorted(a + b))

print(c.count(5))  # Conte quantos '5's
print(c.index(2))  # Posição do numero 2
print(c.index(2,1))  # Posição do numero 2 a partir do primeiro 'index?
pessoa = ('Matheus', 39, 'M', 62.50)
print(pessoa)

for c in range(0, len(pessoa)):
    print(pessoa[c])

for c in range(len(pessoa)-1, -1, -1):
    print(pessoa[c])

for c in pessoa[2:]:
    print(c)
'''
#A tupla é imutável, menos para ser apagada. del(pessoa)

lancheT = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for c, c1 in enumerate(lancheT):
    print(c, c1)
