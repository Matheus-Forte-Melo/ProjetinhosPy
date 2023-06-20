cores = ['\033[;30;m',
         '\033[;30;41m',
         '\033[;30;44m',
         '\033[;30;47m',
         '\033[;30;42m']


def printCor(msg, cor=0):  # Dá de chamar função dentro de outra função (Duhh)
    tam = 0
    tam = len(msg) + 8
    print(cores[cor] + '~'*tam)
    print(f'{msg:^{tam}}')
    print('~'*tam, f'{cores[cor]:>300}')


# Programa Principal
comando = ''
printCor('Welcome to the PyHelp System!', 2)
while True:
    comando = str(input(f'{cores[0]}Type in a function or a library: ')).lower()
    if comando != '999':
        printCor(f'Acessing {comando} manual...', 4)
        print(cores[3])
        help(comando)
    else:
        break
printCor('Thanks for choosing PyHelp. Cya!', 2)
