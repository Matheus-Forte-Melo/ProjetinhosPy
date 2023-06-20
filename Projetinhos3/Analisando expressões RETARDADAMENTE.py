expressao = str(input('Digite uma expressão matematica: '))
lista = []
for elemento in expressao:
    if elemento == '(':
        lista.append(elemento)
        print(lista)
    elif elemento == ')':
        if len(lista) > 0:
            lista.pop()
            print(lista)
        else:
            lista.append(')')
            print(lista)
            break
if len(lista) == 0:
    print('A expressão esta valida!')
else:
    print('A expressão não está valida.')
# Ele cria uma lista vazia e percorre a expressão matemática elemento por elemento. Se o elemento for um parêntese
# aberto, ele adiciona o parêntese à lista. Se o elemento for um parêntese fechado, ele verifica se a lista não está
# vazia (caso esteja, adiciona um parentese) e remove o último parêntese aberto adicionado à lista. Se a lista estiver
# vazia no final, significa que todos parênteses foram fechados, caso contrário, a expressão é considerada inválida.
