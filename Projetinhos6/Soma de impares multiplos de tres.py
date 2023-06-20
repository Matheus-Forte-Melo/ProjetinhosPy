soma = 0
contador = 0
contador1 = 0

for c in range(3,501,3):
    contador1 = contador1 + 1
    if c % 2 != 0:
        soma = soma + c
        contador = contador + 1


print(soma, contador, contador1)