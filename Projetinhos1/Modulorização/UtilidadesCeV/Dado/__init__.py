

def leiaAmbos(val=''):
    while True:
        val = str(input('Digite um valor positivo: ')).strip()
        if ',' in val:
            val = val.replace(',', '.')

        if val.replace('.', '').isnumeric():
            return float(val)
        else:
            if val == '':
                print(f'\033[;31;01mERRO | VOCÊ NÂO DIGITOU NADA!\033[m')
            else:
                print(f'\033[;31;01mERRO | VOCÊ DIGITOU {val}!\033[m')


def leiaInt(val=0):
    while True:
        try:
            val = int(input('Digite um valor inteiro: '))
        except (TypeError, ValueError):
            print('\033[31mValor inválido, tente novamente!\033[m')
            continue  # Pula para o proximo loop
        except KeyboardInterrupt:
            print('\n\033[31mO usuário escolheu não digitar o valor.\033[m')
            return 0
        else:
            return val


def leiaReal(val=0.0):
    while True:
        try:
            val = float(input('Digite um valor real: '))
        except (TypeError, ValueError):
            print('\033[31mValor inválido, tente novamente!\033[m')
            continue  # Pula para o proximo loop
        except KeyboardInterrupt:
            print('\n\033[31mO usuário escolheu não digitar o valor.\033[m')
            return 0
        else:
            return val


''' 
qlqr = leiaAmbos()
inteiro = leiaInt()
real = leiaReal()

print(f'O numero inteiro foi: {inteiro}; O numero real foi {real} e o número qualquer foi {qlqr}')
'''

