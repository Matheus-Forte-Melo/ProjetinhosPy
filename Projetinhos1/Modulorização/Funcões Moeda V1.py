import moeda
import time

print('Bem vindo ao sistema de moedas!')

while True:
    erro = False
    print('=+'*11)
    print('[1] Dobrar valor\n[2] Dividir valor\n[3] Calcular aumento\n[4] Calcular desconto\n[5] Sair')
    print('=+' * 11)
    opcao = int(input('O que deseja fazer?: '))

    if opcao in (1, 2, 3, 4):
        valor = float(input('Digite o valor desejado: '))

    if opcao == 1:
        moeda.dobro(valor, retorno=True, format=True)
    elif opcao == 2:
        moeda.metade(valor, retorno=True, format=True)
    elif opcao == 3:
        porcentagem = int(input('Digite a porcentagem de aumento: '))
        moeda.aumentar(porcentagem, valor, retorno=True, format=True)
    elif opcao == 4:
        porcentagem = int(input('Digite a porcentagem de desconto: '))
        print(moeda.diminuir(porcentagem, valor, retorno=True, format=True))
    elif opcao == 5:
        break
    else:
        print('ERRO! TENTE NOVAMENTE')
        erro = True

    time.sleep(2.5)

# \t \n
