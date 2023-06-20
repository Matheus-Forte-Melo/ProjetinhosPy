expressao = str(input('Digite uma expressão matemática: '))
apenasParenteses = []

for elemento in expressao:
    if elemento == '(' or elemento == ')':
        apenasParenteses.append(elemento)

abertoQuant = apenasParenteses.count('(')
fechadoQuant = apenasParenteses.count(')')

if abertoQuant != fechadoQuant or apenasParenteses[0] == ')' or apenasParenteses[-1] == '(':
    print('A expressão está incorreta!')
else:
    print('A expressão está correta!')

#(a+b)) a + b (