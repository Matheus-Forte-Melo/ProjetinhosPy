from UtilidadesCeV import TXT, arq
from time import sleep
lista = ['Criar Arquivo', 'Ver Pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema']
opcao = 0

# PROGRAMA - > Dá de transoformar arquivo de texto em linha aparentemente
if arq.arquivoExiste():
    print('Arquivo existe')
else:
    print('Arquivo não existe')
while True:
    TXT.titulo('SISTEMA DE CADASTROS', 4)
    opcao = TXT.menu(lista)
    if opcao == 1:
        TXT.titulo('   CRIAR ARQUIVO   ')
        arq.criarArq()
        sleep(3.5)
    elif opcao == 2 :
        TXT.titulo('PESSOAS CADASTRADAS')
        arq.lerArq()
        sleep(3.5)
    elif opcao == 3:
        TXT.titulo('CADASTRAR NOVA PESSOA')
        try:
            arq.modArq()
        except:
            print('HOUVE ERRO!')

    elif opcao == 4 or opcao == 'FLAG':
        print('SAINDO...')
        break
    else:
        print('\033[31mPor favor, digite uma opção válida!\033[m')
