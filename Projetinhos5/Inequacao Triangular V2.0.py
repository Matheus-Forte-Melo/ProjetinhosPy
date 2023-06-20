m1 = float(input('Digite a primeira medida: '))
m2 = float(input('Digite a segunda medida: '))
m3 = float(input('Digite a terceira medida: '))
print('='*40)

if m1 < m2 + m3 and m2 < m1 + m3 and m3 < m1 + m2: # Verifica todas as medidas, se uma ou mais forem falsas, da erro!
    print('As medidas formam um triangulo', end=' ')

    if m1 == m2 == m3: #Ou m1 == m2 and m2 == m3
        print('equalátero!')

    elif m1 == m2 or m2 == m3 or m1 == m3: 
        print('isósceles')

    else: #Ou n1 != m2 != m3 != m1 (Ou usar AND's)
        print('escaleno')


else:
    print('As medidas não formam um triangulo')

#Esse programa verifica e compara todas as medidas com a soma das outras. por exemplo: Se a soma de m1 + m2 for maior que m3, um triangulo nao pode ser formado.

#Para determinar se três medidas dão origem a um triângulo, é necessário verificar se cada medida é menor que a soma das outras duas medidas. Esta é a regra do triângulo, também conhecida como "inequação triangular".

m1 = float(input(''))