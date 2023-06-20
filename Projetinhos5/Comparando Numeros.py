num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite outro numero inteiro: '))

if num1 > num2:
    print(f'O primeiro numero \033[1;32m({num1})\033[m é maior')
elif num2 > num1:
    print(f'O segundo numero \033[1;32m({num2})\033[m é maior')
else:
    print(f'Os numeros são iguais.')