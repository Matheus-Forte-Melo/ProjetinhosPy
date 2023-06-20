quantidade = int(input('Digite a quantidade valores: '))
print('Caso queira cancelar a inserção, digite o codigo 12125')
lista = []
for c in range(quantidade):
    valor = int(input(f'Digite o valor: [{c + 1}/{quantidade}]: '))
    if valor != 12125:
        lista.append(valor)
    else:
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista) } numeros.\nA lista decrescente é igual a: {lista}')
if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')
