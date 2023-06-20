lista = []
x = 1
o = contador = 0



while contador < 6:
    lista.append(int(input('Digite um valor: ')))

    for n in range(0, len(lista)-1):
        for i in range(o, len(lista)-1):
            if lista[o] > lista[x]:
                aux = lista[o]
                lista[o] = lista[x]
                lista[x] = aux
            x += 1
            o += 1
        x = 1
        o = 0
        contador += 1




print(lista)  # Esta solução está correta, porem existe uma solução menos consumivel e melhor que irei fazer na versão 2

