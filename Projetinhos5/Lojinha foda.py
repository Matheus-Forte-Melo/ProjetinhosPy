print(' VENDA DO MELÃO 12 '.center(55,'='))#desconto = int(0)
preço = float(input('Digite o preço de suas compras: '))

print('='*55 + '\n[1]À vista em dinheiro (10% de desconto)\n[2]À vista no cartão (5% de desconto)\n[3]Parcelado (Preço normal até 2x | Adiante 20% de juros)\nDigite a opção desejada: ', end= '')

opcao = int(input(''))
print('='*55,f'\nPreço inicial = R${preço}')

if opcao == 1: #Dava de ter feito direto no print, mas queria guardar a info na var pq fodase aparentemente.
    preço = preço - ((preço * 10) / 100)
    print(f'Preço com 10% de desconto = R${preço}')
elif opcao == 2:
    preço = preço - ((preço * 5) / 100)
    print(f'Preço com 5% de desconto = R${preço}')
elif opcao == 3:
    parcelas = int(input('Digite o total de parcelas: '))

    if parcelas > 2:
        preço = preço + ((preço * 20) / 100 )
        print(f'Com {parcelas} parcelas, você pagará no total R${preço}. Cada parcela custará R${preço / parcelas}')
    else:
        None
        print(f'Com {parcelas} parcelas, você pagará no total R${preço}. Cada parcela custará R${preço / parcelas}')
else:
    print(f'Preço final = R${preço}')
