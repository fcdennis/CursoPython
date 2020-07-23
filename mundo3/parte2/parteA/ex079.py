lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    adicionado = True
    for e in lista:
        if lista.count(e) == 2:
            lista.pop()
            adicionado = False
    if adicionado:
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    flag = ' '
    while flag not in 'SsNn':
        flag = input('Quer continuar? [S/N] ').upper().strip()[0]
    if flag in 'Nn':
        break
print(f'Você digitou os valores {sorted(lista)}')
