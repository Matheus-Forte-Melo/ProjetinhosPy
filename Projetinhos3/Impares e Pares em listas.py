lista = []
impares = []
pares = []

while True:
    lista.append(int(input('Digite um valor: ')))
    confirm = str(input('Quer continuar? [S / N]: ')).upper()
    if 'N' in confirm:
        break

for valor in range(len(lista)):
    if lista[valor] % 2 == 0:
        pares.append(lista[valor])
    elif lista[valor] % 2 == 1:
        impares.append(lista[valor])

print(lista)
print(pares)
print(impares)

