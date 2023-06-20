arquivo, nota = [], []
while True:
    aluno = str(input('Digite o nome do aluno: '))
    notaQnt = int(input('Quantas notas?: '))
    if notaQnt < 1:
        notaQnt = 1  # Para não dar erro.

    for c in range(notaQnt):
        nota.append(float(input(f'Digite a {c + 1}° nota do aluno: ')))
        if nota[c] < 0 or nota[c] > 10:
            print('ERRO: VOLTANDO!')
            nota[c] = 404  # Flag para não cadastrar nulo
            break

    confirmacao = str(input('Quer inserir outro aluno? [S/N]: ')).upper()
    if 404 not in nota:
        arquivo.append([aluno, nota[:]])
    nota.clear()
    if confirmacao in ['NÃO', 'N', 'NAO']:
        break

print('=-' * 17, f"\n\033[4mPOS. ALUNO {'MÉDIA':>18}\033[m")
for pos, registro in enumerate(arquivo):
    print(f"{pos:< 5}{registro[0]:<15}{sum(registro[1]) / len(registro[1]):>8.1f}")
print('=-' * 17)
while True:
    al = int(input('Visualizar nota de: '))
    if al == 999 or al > len(arquivo):
        break
    print(f'As notas de {arquivo[al][0]} são {arquivo[al][1]}')


