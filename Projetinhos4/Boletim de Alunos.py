arquivo, aluno, nota = [], [], []
contador = pos = 0
while True:
    aluno.append(str(input('Digite o nome do aluno: ')))
    nota.append(float(input('Digite a primeira nota do aluno: ')))
    nota.append(float(input('Digite a segunda nota do aluno: ')))
    confirmacao = str(input('Quer inserir outro aluno? [S/N]: ')).upper()

    arquivo.append(aluno[:])
    arquivo[contador].append(nota[:])
    aluno.clear(), nota.clear()
    contador += 1
    if confirmacao in ['NÃO', 'N', 'NAO']:
        break
print('=-'*17)
print(f"\033[4mPOS. ALUNO {'MÉDIA':>18}\033[m")
for pos, registro in enumerate(arquivo):
    print(f"{ pos:< 5}{registro[0]:<15}{sum(registro[1]) / 2:>8}")
while True:
    al = int(input('Visualizar nota de: '))
    if al == 999 or al > pos:
        break
    print(f'As notas de {arquivo[al][0]} são {arquivo[al][1]}')
