nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

print('='*35,f'\nSua média nesta matéria é igual a {media}')
if media > 7.0:
    print('\033[1;32mAprovado!\033[m')
elif media < 6.7 and media > 5.0:
    print('Você tem direito à recuperação!')
else:
    print('\033[1;31mReprovado!\033[m')
