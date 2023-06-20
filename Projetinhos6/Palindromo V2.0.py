frase = str(input('Digite uma frase: ')).lower().split()
frase = ''.join(frase)
frasePal = '' # frase[::-1]

for letra in range(len(frase) -1, -1, -1): # len(frase) = fechado, logo entra. -1 aberto, n entra (vai até 0)
    frasePal = frasePal + frase[letra]

print(frasePal)

#Temos que lembrar que em python, toda string é basicamente uma array, por isso coisas como esta acima é possivel. (refazer de cabeça)

