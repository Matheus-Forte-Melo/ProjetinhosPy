from random import randint

print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")
print("Digite 1 para Pedra, 2 para Papel, ou 3 para Tesoura.")

player_choice = int(input("Qual é a sua escolha? "))
player_choice = player_choice - 1
computer_choice = randint(0, 2)

lista = ['PEDRA','PAPEL,','TESOURA']

if player_choice == computer_choice:
    print("Empate!")
elif player_choice == 1 and computer_choice == 3:
    print("Você ganhou! Pedra vence Tesoura.")
elif player_choice == 2 and computer_choice == 1:
    print("Você ganhou! Papel vence Pedra.")
elif player_choice == 3 and computer_choice == 2:
    print("Você ganhou! Tesoura vence Papel.")
else:
    print("Você perdeu! Tente novamente.")
    print(f'Pois {lista[computer_choice]} vence de {lista[player_choice]}')

print("O computador escolheu: ", lista[computer_choice], f" e você escolheu {lista[player_choice]}")