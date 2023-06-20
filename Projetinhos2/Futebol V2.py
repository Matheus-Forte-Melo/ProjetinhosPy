dados, kills, time = {}, [], []
pos = 0

while True:
    dados['nome'] = str(input('Digite o nome do jogador: '))
    qntd_partida = int(input('Quantas partidas?: '))
    print('=+='*8)
    for c in range(qntd_partida):
        kills.append(int(input(f'Kills na {c+1}° partida: ')))
    print('=+='*8)
    dados['kills'] = kills[:]
    dados['total'] = sum(kills)
    time.append(dados.copy())
    kills.clear()
    while True:
        confirm = str(input('Adicionar outro jogador? [S|N]:')).upper()
        if confirm in ['S','N','SIM','NÃO','NAO']:
            break
        print('ERRO! RESPONDA NOVAMENTE!')
    if confirm in ['N', 'NÃO', 'NAO']:
        break
print('=+='*8)
print('COD. NOME      KILLS                TOTAL')
for pos, valor in enumerate(time):
    print(f' {pos:<2}  {valor["nome"]:<10}{str(valor["kills"]):<20} {valor["total"]:}')  # !s:<15s
print('=+='*8)

while True:
    busca = int(input('Digite o jogador à visualizar: '))
    if busca != 999 and busca < len(time):
        print(f'   ->Levantamento de kills de {time[busca]["nome"]} ')
        for partida, c in enumerate(time[busca]["kills"]):
            print(f'      Na {partida} fez {time[busca]["kills"][partida]} kills!')
    elif busca == 999:
        print('Encerrando!', '=+=' * 8)
        break
    if busca > len(time) and busca != 999:
        print(f'Jogador {busca} inválido!')
        print('=='*12)


