lista = list()
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {c}: ')))
print('=-' * 50)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições', end=' ')
for k, v in enumerate(lista):
    if v == max(lista):
        print(k, end='... ')
print(f'\nO menor valor digitado foi {min(lista)} nas posições', end=' ')
for k, v in enumerate(lista):
    if v == min(lista):
        print(k, end='... ')
