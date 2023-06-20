'''from time import sleep
import random
num = 0
lista, jogos = [], []
print(f"{'> SORTEIO DA MEGA SENA <':=^35}")
quantidade = int(input('Digite a quantidade de sorteios: '))

for n in range(quantidade):
    lista = random.sample(range(1, 61), 6)
    lista.sort()
    jogos.append(lista[:])
    lista.clear()

print('=-' * 2,' REALIZANDO SORTEIOS! ', '=-' * 2)

for jogo in jogos:
    print(jogo)
    sleep(0.5)
print(f"{' >BOA SORTE!< ':=^35}")'''  # Versão com Random Sample. (5 linhas a menos)
from time import sleep
from random import randint
contador = num = 0
lista, jogos = [], []
print(f"{'> SORTEIO DA MEGA SENA <':=^35}")
quantidade = int(input('Digite a quantidade de sorteios: '))

for n in range(quantidade):
    while contador < 6:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            contador += 1
    contador = 0
    lista.sort()
    jogos.append(lista[:])
    lista.clear()

print('=-' * 2,' REALIZANDO SORTEIOS! ', '=-' * 2)

for jogo in jogos:
    print(jogo)
    sleep(0.5)
print(f"{' >BOA SORTE!< ':=^35}")


