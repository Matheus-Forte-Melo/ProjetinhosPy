extenso = ('um', 'dois', 'três', 'quatro', 'cinco', 'ceis', 'sete', 'oito', 'nove', 'dez'
           , 'onze', 'doze', 'trze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número entre 0 e 20: '))
while num > 20 or num < 0:
    num = int(input('Tente denovo! Digite um numero entre 0 e 20: '))
print(f'\033[34;1mParabéns!\033[m Você sabe ler e escreveu o numero {extenso[num-1]}!')

# Poderia também utilizar o input dentro de um while infinito e fazer um if statement, seria mais legivel porém fodase?.
