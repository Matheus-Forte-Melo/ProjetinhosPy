lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
print(lanche)
lanche[3] = 'Picolé'
print(lanche[3])
lanche.append('Cookie')
print(lanche)
lanche.insert(2, 'Fandangos')
print(lanche)
lanche.pop()
print(lanche)
lanche.pop(0)
print(lanche)
lanche.remove('Pizza')
print(lanche)
del lanche[-1]
print(lanche)

if 'z   uco' in lanche:
    lanche.remove('Suco')
else:
    print('Não encontrei tal valor, seu burro.')

#  INSERIR ----
#  Append = Botar no final
#  Insert() = Botar em posição definida. Tecnicamente falando, cria um espaço a mais no final do vetor, passa todos os
#  elementos para frente e insere na posição remanescente definida.
#  DELETAR ----
#  del lanche[indice] // Elimina pelo indice, reposiciona a contagem dos índices.
#  lanche.pop(indice) // Elimina o ultimo elemento, porém parâmetros podem ser passados
#  lanche.remove(valor) // Eliminar pelo conteudo

#  ATENÇÃO ---> Tentar remover elementos da lista inexistentes resultará em ERRO do codigo, é possivel evitar isso
#  Utilizando UM IF com IN // EX: if 'Pizza' in lanche -> lanche.remove('Pizza'), ou lanche.remove(variavel) SLA.

valores = list(range(2, 9, 1))  # Ou tuple
print(valores)
valores2 = list(range(2, 9, 2))  # Ou tuple
print(valores2)
valores3 = list(range(10, 0, -1))  # Ou tuple
print(valores3)
valores4 = list(range(10, 0, -2))  # Ou tuple
print(valores4)
valoresSorted = [1, 7, 12, 7, 82, 2, 9, 4, 44, 51, 31, 21, 11]
valoresSorted.sort()
# ValoresSorted.sort(reverse='True') # Reverso
print(valoresSorted)
print(len(valoresSorted))

listaVazia = []  # ou list()

for v, c in enumerate(range(1, 6)):
    listaVazia.append(int(input(f'{v} Digite um valor: ')))

for pos, valor in enumerate(listaVazia):
    if valor == listaVazia[-1]:
        print(pos, '->', valor, end='. \n')
    else:
        print(pos, '->', valor, end='; ')

a = [1, 2, 3, 6]
b = a  # A partir do momento que eu crio essa ligação, elas ficarão interligadas, oq eu mudar nessa muda na outra... EX:
print(a)
print(b)
b[2] = 8
print('\n-----\n')
print(a)
print(b)

#Para não criar uma ligação, tem que ser feito o seguinte: b = a[:]
