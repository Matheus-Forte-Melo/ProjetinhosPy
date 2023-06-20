tabelaTimes = ('Fluminense', 'Flamengo', 'Atlético-PR', 'Palmeiras', 'Botafogo', 'Bragantino',  'Corinthians', 'Chapecoense',
               'Grêmio', 'Internacional',  'Fortaleza', 'Bahia', 'Cruzeiro', 'Chapecoense', 'Atlético-MG',
               'Cuiabá', 'Santos', 'Goiás', 'Ámerica-MG', 'Coritiba')

print(tabelaTimes[:5])
print(tabelaTimes[-4:])
print(sorted(tabelaTimes))
pos = str(input('Digite um time da tabela: ')).capitalize()
print(f'O {pos} está na {tabelaTimes.index(pos)} posição')
# print(f'A chapecoense está na {tabelaTimes.index("Chapecoense", 8)} posição')


