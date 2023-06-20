def leiaINT(msg):
    while True:
        if msg.isnumeric():
            return int(msg)
        msg = input('ERRO, DIGITE NOVAMENTE: ')


numero = leiaINT(input('Digite um numero: '))
print('Digitastes o numero', numero)