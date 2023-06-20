soma = 0
homemVelho = ''
idadeHomem = 0
contadorMulher = 0


for c in range(1, 5):
    print(f' {c}ª PESSOA '.center(35,'='))
    nome = str(input('Digite o nome da pessoa: ')).strip()#Garante que não vão ficar espaços vazios depois ou antes.
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()

    soma = soma + idade

    if sexo == 'M':
        if idade > idadeHomem:
            idadeHomem = idade
            homemVelho = nome
    elif sexo == 'F' and idade < 20:
        contadorMulher += 1

if contadorMulher > 1 or contadorMulher == 0:
    print(f'A media de idade é de {soma/4} e o homem mais velho é {homemVelho}, existem {contadorMulher} menores de 20 anos')
else:
    print(f'A media de idade é de {soma / 4} e o homem mais velho é {homemVelho}, existe {contadorMulher} menor de 20 anos')