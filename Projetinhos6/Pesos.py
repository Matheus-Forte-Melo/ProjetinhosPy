maior = 0.0
menor = 0.0
peso = 0.0
for c in range(1, 6):

    peso = float(input(f'Digite o peso da {c}ª pessoa [Em KG]: '))

    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(menor, maior)
