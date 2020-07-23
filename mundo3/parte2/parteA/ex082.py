listaCompleta = list()
listaPar = list()
listaImpar = list()

while True:
    listaCompleta.append(int(input('Digite um número: ')))
    flag = ' '
    while flag not in 'SsNn':
        flag = input('Quer continuar? [S/N] ').upper().strip()[0]
    if flag in 'Nn':
        break

for n in listaCompleta:
    if n % 2 == 0:
        listaPar.append(n)
    else:
        listaImpar.append(n)

print(f'A lista completa é {listaCompleta}')
print(f'A lista de pares é {sorted(listaPar)}')
print(f'A lista de impares é {sorted(listaImpar)}')
