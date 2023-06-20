from datetime import date

nascimento = int(input('Digite o ano em que nasceu: '))

hoje = date.today().year
idade = hoje - nascimento

print('='*40,f'\nVocê tem (ou vai fazer) \033[01;32m{idade}\033[m anos.')

if idade < 18:
    print(f'Você precisa se alistar daqui \033[01;32m{18 - idade}\033[m ano(s). Em {nascimento + 18}')
elif idade == 18:
    print('Você já tem 18 anos! aliste-se ASSIM QUE PUDER!')
else:
    print(f'Ja se passou o tempo de você se alistar! já fazem \033[01;32m{(18 - idade) * -1}\033[m ano(s).\nVocê se alistou em {nascimento + 18}')







