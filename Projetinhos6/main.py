numero = int(input('Digite o numero incial: '))
numero2 = int(input('Digite o numero final: '))
resultado = int(0)


if numero > numero2:
        for c in range(numero, numero2-1, -1) :
         print(c)
        print(f'Os numeros foram imprimidos de trás para frente pois {numero} é maior que {numero2}')

else:
        for c in range(numero,numero2+1): #O primeiro numero é fechado, ou seja, ele entra. O segundo numero é aberto, ou seja, ele não entra
         # soma = int(input('Digite um valor: '))
         # resultado = resultado + soma
         print(c)
         #print('=',resultado)





