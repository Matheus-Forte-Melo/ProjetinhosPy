dados, gols = {}, []

dados['nome'] = str(input('Digite o nome do jogador: '))
qntd_partida = int(input('Quantas partidas?: '))
print('=+='*8)
for c in range(qntd_partida):
    gols.append(int(input(f'Gols na {c+1}° partida: ')))
print('=+='*8)
dados['gols'] = gols
dados['total'] = sum(gols)

for c, v in dados.items():
    print(f'O campo {c} tem o valor {v}')
print('=+='*8, f'\nO jogador {dados["nome"]} jogou {qntd_partida} partidas!')

for n, gols in enumerate(dados['gols']):
    print(f'      Na partida {n+1} fez {gols} gols.')
print(f'Totalizando {sum(dados["gols"])} gols!')



