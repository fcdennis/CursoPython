def area(x, y):
    a = x * y
    print(f'A área de um terreno {x}x{y} é de {a:.1f}m².')

print('Controle de Terrenos')
print('-' * 50)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
