print('➛'*30, '\n', '10 TERMOS DE UMA PA'.center(45), '\n' + '➛'*30)

pTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

for c in range(pTermo, pTermo + 10 * razao, razao): #for c in range(25,-25,5) o -25 não entra pq o elemento é aberto, diferente do 25.
    print(f'{c} ➛ ',end='')

print('Acabou!')
