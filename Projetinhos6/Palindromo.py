from string import punctuation

frase = str(input('Digite uma frase: '))
frase = frase.lower().split()
frase = ''.join(frase)
frase = frase.translate(str.maketrans('', '', punctuation))

igual = False
ponteiro2 = len(frase) - 1

# Enquanto C e PONTEIRO2 não se cruzarem, o laço continua executando sua função, que é de analisar as duas extremidades
# da frase. Utilizando de dois ponteiros, um para o fim, e um para o começo, se as extremidades forem iguais, o escopo diminui, e assim por
# diante, até chegarem ao meio.

for c in range(0, ponteiro2, 1):
    if ponteiro2 > c:
        if frase[c] == frase[ponteiro2]:
            igual = True
        else:
            igual = False
            break
    ponteiro2 -= 1

if igual == True:
    print(f'A frase digitada é um palíndromo!')
else:
    print(f'A frase digitada não é um palíndromo!')
