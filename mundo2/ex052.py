n = int(input('Digite um número: '))
contador = 0
for c in range(1, n + 1):
    if n % c == 0:
        print(f'\033[33m{c}\033[m', end=' ')
        contador += 1
    else:
        print(f'\033[34m{c}\033[m', end=' ')
print(f'\nO número {n} foi dividido {contador} vezes.')
print('E por isso ele ', end='')
if contador == 2:
    print('\033[32mÉ PRIMO\033[m')
else:
    print('\033[31mNÃO É PRIMO\033[m')
