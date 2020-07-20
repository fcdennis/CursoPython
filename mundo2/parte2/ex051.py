print('=' * 25)
frase = '10 termos de uma PA'
print(f'{frase:^25}')
print('=' * 25)

pt = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for c in range(0, 10):
    pa = pt
    pt = pt + razao
    print(pa, end=' → ')
print('ACABOU')
