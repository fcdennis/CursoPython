print('-' * 50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('-' * 50)
produtos = 'Lápis', '1,75', 'Borracha', '2,00', 'Caderno', '15,90', 'Estojo', '25,00', 'Transferidor', '4,20', 'Compasso', '9,99', 'Mochila', '120,32', 'Canetas', '22,30', 'Livro', '34,90'
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'\033[36m{produtos[c]:~<40}\033[m', end=' \033[33mR$')
    else:
        print(f'{produtos[c]:>7}\033[m')
