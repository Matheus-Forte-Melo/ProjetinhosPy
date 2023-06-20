num = int(input('Digite um numero inteiro postivo: '))
print('='*35,'\n[1]Converter para binário\n[2]Converter para octal\n[3]Converter para hexadecimal\n')

opcao = int(input('Digite a opção desejada: '))

if opcao == 1:
    print('='*35,f'\nO numéro {num} em \033[1;36mbinário\033[m é', bin(num)[2:])

elif opcao == 2:
    print('='*35,f'\nO numéro {num} em \033[1;32moctal\033[m é',oct(num)[2:])

else:
    print('='*35,f'\nO numéro {num} em \033[1;33mhexadecimal\033[m é',hex(num))

#Uma coisa que estou esquecendo é a parada de manipulação de strings.
#Posso utiliar o .format e :x :o OU :b para fazer tbm: EX = print(:x).format(264)