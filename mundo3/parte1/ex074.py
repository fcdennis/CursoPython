from random import randint

numeros = randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9)
print('Os números sorteados foram:', end=' ')
for n in numeros:
    print(n, end=' ')
print(f'\nO maior é {max(numeros)}')
print(f'O menor é {min(numeros)}')
