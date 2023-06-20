def linhas(msg):
    tamanmho = int(len(msg) + 4)
    print('=' * tamanmho)
    print(f'{msg:^{tamanmho}}')
    print('=' * tamanmho)


mensagem = str(input())
linhas(mensagem)

