from random import choice
from time import sleep

opcao = int(input(f'{"OPÇÕES":^10}\n'+'='*10+'\n[1]PEDRA\n[2]PAPEL\n[3]TESOURA\n'+'='*10+'\nEscolha a opção desejada: '))
opcao = opcao - 1
escolha = ['PEDRA','PAPEL','TESOURA']

usuario = escolha[opcao]
computador = choice(escolha) #Invez de fazer essa putaiada aqui, dava de ter feito sem isso e utilizado os numeros, dai mais embaixo botar prints em cada desvio. Invez de associar os numeros aos elementos

print('PEDRA!')
sleep(0.500)
print('PAPEL!')
sleep(0.500)
print('TESOURA!')
sleep(0.500)

vencedor = None
if usuario == 'PEDRA':
    if computador == 'TESOURA':
        vencedor = 'usuario'
    elif computador == 'PAPEL':
        vencedor = 'computador'
elif usuario == 'PAPEL':
    if computador == 'PEDRA':
        vencedor = 'usuario'
    elif computador == "TESOURA":
        vencedor = 'computador'
elif usuario == 'TESOURA':
    if computador == 'PEDRA':
        vencedor = 'computador'
    elif computador == 'PAPEL':
        vencedor = 'usuário'

if usuario == computador:
    print('='*10,f'\nEMPATE! Ambos vocês jogaram {usuario}')
else:
    print('='*10,f'\nO VENCEDOR È O {vencedor.upper()}!\nVocê jogou {usuario.upper()} e o computador {computador.upper()}')