'''lista = []

nome = str(input('Digite o nome: '))
idade = int(input('Digite sua idade: '))
nota1 = int(input('Digite sua nota: '))
nota2 = int(input('Digite sua nota: '))

lista.append([nome, idade, [nota1, nota2]])

print(lista)'''
'''dados = {'nome': 'Maria', 'idade': 19 }

print(dados['nome'])
print(dados['idade'])

dados['sexo'] = 'F'
print(dados['sexo'])

del(dados['idade'])
print(dados)'''
"""
filme = {'nome': 'Hacksaw Ridge',
         'ano': 2016,
         'diretor': 'Mel Gibson'}

print(filme.values())
print(filme.keys())
print(filme.items())

#  for teste in filme.values():
#  print(teste)

for chave, valor in filme.items():
   print(f'O {chave} é {valor}')

lista = []

lista.append(filme)
print(lista)

filme = {'nome': 'Batman',
         'ano': 2022,
         'diretor': 'Jonathan Leonard'}

lista.append(filme)
print(lista)

print(lista[1]['diretor'])"""
'''pessoas = {'nome': 'Matheus', 'idade': 17}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos!')
# del pessoas['nome']

for chaves, valores in pessoas.items():
    print(chaves, valores)'''
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Santa Catarina', 'sigla': 'SC'}
brasil.append(estado1), brasil.append(estado2)
print(brasil[0]['uf'])
'''brasil = []
estados = {'uf': '', 'sigla': ''}

quant = int(input('Quantos dados?: '))
for c in range(quant):
    estados['uf'] = str(input('Unidade federativa: '))
    estados['sigla'] = str(input('Digite a sigla: '))
    brasil.append(estados.copy())
print(brasil)'''
