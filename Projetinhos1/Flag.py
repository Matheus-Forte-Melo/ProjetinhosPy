

def score(player='<desconhecido>', kills=0):
    print(f'O player {player} fez {kills} kills!')


# Programa principal
nome = str(input('Digite o nome do jogador: '))
kills = str(input('Digite as kills do jogador: '))

# Verificando kills
if kills.isnumeric():  # Checa se é numérico
    kills = int(kills)  # Se numérico, transforma a string em número
else:
    kills = 0  # Senão, define como 0 int

# Verificando nome e imprimindo
if nome.strip() == '':
    score(kills=kills)  # Se o nome for nulo, ele só indica o paramêtro de KILLS
else:
    score(nome, kills)  # Se não, ele indica ambos os parâmetros
