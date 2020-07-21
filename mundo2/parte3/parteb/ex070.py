print('-' * 30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-' * 30)

total = contador = pechincha = 0.0
while True:
    produto = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    if total == 0 or preco < pechincha:
        pechincha = preco
        n_pechincha = produto
    total += preco
    if preco >= 1000:
        contador += 1
    flag = ' '
    while flag not in 'SsNn':
        flag = input('Quer continuar? [S/N] ').upper().strip()[0]
    if flag in 'Nn':
        print('-' * 10, 'FIM DO PROGRAMA', '-' * 10)
        break
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {contador} produtos custando mais do que R$1000,00')
print(f'O produto mais barato foi {n_pechincha} que custa R${pechincha:.2f}')
