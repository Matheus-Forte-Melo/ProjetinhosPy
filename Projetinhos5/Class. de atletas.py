from datetime import date

#Criando as variaveis
anoNasc = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - anoNasc

print('='*65,'\n',f'Você tem {idade} anos!'.center(60)) #f'Você tem {idade^65} anos!', ou usando o .format do mesmo modo sem o \n

if idade <= 9:
    classficacao = 'MIRIM'
elif idade <= 14:
    classficacao = 'INFANTIL'
elif idade <= 19:
    classficacao = 'JUNIOR'
elif idade <= 25:
    classficacao = 'SENIOR'
else:
    classficacao = 'MASTER'

print(f'Com base em sua idade, você foi colocado na classificação \033[4m{classficacao}\033[m!')

#MODO ALTERNATIVO
#mirim = range(0, 10)
#infatil = range(10, 15)
#junior = range(15, 20)
#senior = 20

