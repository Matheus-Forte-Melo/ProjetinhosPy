def teste(b):
    #  global a
    a = 5
    b = b + 4
    print('DENTRO:')
    print(a, b)


a = 421
teste(a)
print('FORA:')
print(a)
