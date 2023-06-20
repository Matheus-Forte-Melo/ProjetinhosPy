#Refazer essa merda

palavras = ('Pomba', 'Porto', 'Violão', 'Macaco', 'Goiaba', 'Gordon' )
contador = 0

for palavra in palavras:
    print(f'\nA palavra {palavra.upper()} tem as vogais: ', end='')
    for letra in palavra:
        if letra in ('âãaáeéêiíoõu'):
            print(letra, end=' ')
            contador += 1
    print(f'({contador} VOGAIS e {len(palavra) - contador} CONSOANTES)', end = '')  # Isso ta fora do primeiro laço,
    # por isso printa sempre no final. E isso tem o END no final porque o começo do laço começa com \n
    contador = 0

