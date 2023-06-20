alturaM = float(input('Digite sua altura: ')) #Poderia dar em CM's e depois calcular CM / 100 para transformar em metro

if alturaM.is_integer():
    alturaM = alturaM / 100 #Ou == True

massaKg = float(input('Digite seu peso: '))

imc = massaKg / alturaM ** 2

print('='*55,'\n'+f'Seu Idice de Massa Corpórea é de {round(imc,2)}! = ',  end='')

if imc < 18.5:
    print('\033[1;34mBaixo peso\033[m')

elif imc < 24.9:
    print('\033[1;32mPeso normal\033[m')

elif imc < 29.9:
    print('\033[1;33mExesso de peso\033[m')

elif imc < 35.0:
    print('\033[1;32mObesidade\033[m')

else:
    print('\033[1;31mObesidade extrema!\033[m')




#pensei em fazer tipo uma barra representando o IMC por cores e tal, mas ainda n sei usar laços, então volto nesse cod dps

