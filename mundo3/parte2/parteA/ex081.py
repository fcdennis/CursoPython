lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    flag = ' '
    while flag not in 'SsNn':
        flag = input('Quer continuar? [S/N] ').upper().strip()[0]
    if flag in 'Nn':
        break
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são: {sorted(lista, reverse = True)}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista')
