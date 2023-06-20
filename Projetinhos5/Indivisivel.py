num = float(input('Digite o numero à ser dividido: '))
divisor = float(input('Digite o numero divisor:'))

if num % divisor == 0:
    print(f'\nO numéro {num} é divisivel por {divisor}')
else:
    print(f'\nO numero {num} é NÃO é divisivel por {divisor}')

#estrutura de repetição que pega o resultado da divisão e fica somando a si proprio (como uma tabuada), dai ele analisa se tal resultado passou o 'num' (Usar While pq n sei o numero de repetições necessarias)
#essa estrutura while só vai parar quando ele + ele mesmo for maior que num. (obviamente, isso so vai acontecer casó for indivisivel.)

print('\nVale ressaltar que um numero INDIVISIVEL não significa que não pode ser dividido. Mas sim, um que não pode ser divido INTEIRAMENTE')
print(f'Resultado da divisão: {num / divisor}| Resultado da divisão INTEIRA {num // divisor}| Resto da divisão {num % divisor}')