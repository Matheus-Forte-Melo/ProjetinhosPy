cores = ['\033[m', '\033[31m', '\033[32m',
         '\033[34m', '\033[35m', '\033[36m']


def leiaInt(txt='', val=0):
    while True:
        try:
            val = int(input(f'{txt}'))
        except (TypeError, ValueError):
            print('\033[31mValor inválido, tente novamente!\033[m')
            continue  # Pula para o proximo loop
        except KeyboardInterrupt:
            print('\n\033[31mO usuário escolheu não digitar o valor.\033[m')
            return 'FLAG'
        else:
            return val


def titulo(txt='', cor=0, char='='):
    tamanho = len(txt) + 4
    print(f'{char}' * tamanho)
    print(f'{cores[cor]}{txt:^{tamanho}}{cores[0]}')
    print(f'{char}' * tamanho)


def menu(txt):
    for pos, e in enumerate(txt):
        print(f'{cores[2]}{pos + 1}{cores[0]}', '-', e)
    linha()
    opcao = leiaInt('Digite a opção: ')
    return opcao


def linha(tam=24, char='-'):
    print(char * tam)
