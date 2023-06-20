produtos = ('Macarrão', 6.50, 'Gelatina 150g', 5.99, 'Ketchup', 6.25, 'Maioenese', 7
            , 'Pão integral', 10, 'Chocolate', 3.99, 'Nescau', 5, 'Presunto', 6)
opcao = 1

for c in range(0, len(produtos), 2):

    print(f'{produtos[c]:.<50}' + f'{produtos[c+1]:^7.2f}')




# :^ centraliza
# :> pro lado
# :< pro outro
# >2.f ponto flutuante
# :>, ou :< ou :^ com caracter antes da setinha para fazer o preenchimento