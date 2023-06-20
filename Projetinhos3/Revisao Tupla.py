teste = ('opsts', 'alsos', 'pokrin')

for letras in teste:
    print('\n'+letras, end=' = ')
    tamanho = len(letras)
    ultimaLetra = letras[len(letras)-1]
    for letra in letras:
        if letra == ultimaLetra:  # Ou utilizar letras[-1]
            print(f"'{letra}'", end='.')
        else:
            print(f"'{letra}'", end=', ')

