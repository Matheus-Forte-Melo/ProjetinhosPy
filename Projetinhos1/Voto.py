

def voto(ano):
    import datetime
    idade = datetime.date.today().year - ano
    if idade >= 18 and idade < 65:
        return f'Com {idade} anos: Obrigatório'
    elif idade in [16, 17] or idade >= 65:
        return f'Com {idade} anos: Voto Opcional'
    else:
        return f'Com {idade} anos: Voto Negado'


nasc = int(input('Digite seu ano de nascimento: '))
print(voto(nasc))
