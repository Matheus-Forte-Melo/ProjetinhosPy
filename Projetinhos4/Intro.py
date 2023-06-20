'''teste = list()
teste.append('Matheus')
teste.append(16)
galera = []
galera.append(teste[:])
print(galera)
teste[0] = 'Maria'
teste[1] = 16
galera.append(teste[:])
print(galera)
#::-1
#:
#Da de usar as parada de manipulação
'''
'''

print('='*25)
people = [['Jhonny', 16], ['Lucas', 25], ['Robert', 14]]
print(people[2][0])
print(people[0][0])
print(people[1][1])
print(people[1])
print('='*25)
'''
'''galera = [["Robierto", 17], ["Ana", 12], ['Chupo', 45], ['Delguapan', 77]]
print(galera)
print(galera[-1][-2])

    # contador = 0
for pos, pessoa in enumerate(galera):
    # contador += 1
    # print(f'O individuo na posição {contador} da lista galera é {pessoa[0]} de {pessoa[1]} anos!')
    print(f'O individuo na posição {pos} da lista galera é {pessoa[0]} de {pessoa[1]} anos!')'''
maiorID = menorID = 0
galera = []
pessoa = []
num = int(input('Digite o numero de pessoas que deseja cadastrar: '))
for contador in range(0, num):
    print(f'fAgora cadastrando a {contador+1}° pessoa!')
    pessoa.append(str(input('Digite o nome: ')))
    pessoa.append(int(input('Digite a idade: ')))
    galera.append(pessoa[:])
    pessoa.clear()

for p in galera:
    if p[1] > 18:
        print(f'O(a) {p[0]} é maior de idade!')
        maiorID += 1
    else:
        print(f'O(a) {p[0]} é menor de idade.')
        menorID += 1
print('=-'*25, f'O total de maiores de idade é de: {maiorID}\n O total de menores de idade é de: {menorID}')

