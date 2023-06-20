from playsound import playsound

valCasa = float(input("Digite o valor da casa que deseja comprar: "))
salario = float(input("Digite seu salário atual: "))
anos = int(input("Por quantos anos deseja financiar esta casa: "))

prestacaoMensal = valCasa / (anos * 12)
maximo = (salario * 30) / 100

print('\n'+'='*20)

print(f'Após pagar a prestação com seu salário atual (por mês), Sobrarão {(salario - prestacaoMensal):.2f} reais.')
print(f'Para o empréstimo ser aceito, o valor da prestação mensal não pode exeder 30% de seu salario. se 30% de seu salário é R${maximo:.2f} e cada prestação é de R${prestacaoMensal:.2f}, logo:')

if prestacaoMensal <= maximo: #A cobrança/prestação mensal não pode exeder mais de 30% do salario

    print('Empréstimo \033[1;32maceito')
    playsound("C:\\Users\Melo\PycharmProjects\Sons\dinheiro.mp3")


else:
    print("Empréstimo \033[1;31mrecusado")
    playsound("C:\\Users\Melo\Downloads\\Nao apagar\Clash Royale Rage Sound Effect.mp3")

#Primeiramente o algoritmo espera a inserção de 3 dados; O valor da casa a ser comprada, o salário do usuario e o total de anos que ele pretende comprar tal casa
#Então o algorimo calcula o tanto que o usuario gastará em cada mês do ano (prestaçãoMensal)
#Logo o algoritimo calcula o valor "maximo" que cada prestação pode ocupar (até 30% do salario mensal)
#Se a prestaçãoMensal não exeder o limite, o empréstimo sera liberado. Senão, o emprestimo será recusado.
