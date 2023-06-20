
def arquivoExiste():
    try:
        arquivo = open('cadastro.txt', 'x')
        arquivo.close()
    except FileExistsError:
        return True
    else:
        return False


def leiaInt(txt='',val=0):
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


def criarArq():
    try:
        arquivo = open('cadastro.txt', 'x')
        print('Arquivo criado!')
        arquivo.close()
    except FileExistsError:
        print('Arquivo já existe!')


def modArq():
    nome = str(input('Digite o nome: '))
    idade = leiaInt('Digite a idade: ')
    profissao = str(input('Digite a profissão: '))
    nacionalidade = str(input('Digite a nacionalidade:'))
    arquivo = open('cadastro.txt', 'a', encoding='utf8')
    arquivo.write(f'\n{nome} - {idade} - {profissao} - {nacionalidade}')
    arquivo.close()


def lerArq():
    with open('cadastro.txt') as arq:
        print(arq.read())


def teste():
    arq = open('cadastro.txt', 'r')
    for linha in arq:
        print(linha, end='')
    arq.close()