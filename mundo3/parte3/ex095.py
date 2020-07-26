jogador = dict()
gol = list()
time = list()
while True:
    jogador['nome'] = input('Nome do Jogador: ')
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, jogador['partidas']):
        gol.append(int(input(f'     Quantos gols na partida {c + 1}: ')))
    jogador['gols'] = gol.copy()
    jogador['total'] = sum(gol)
    time.append(jogador.copy())
    gol.clear()
    flag = ' '
    while True:
        flag = input('Quer continuar? [S/N] ').upper().strip()[0]
        if flag in 'SsNn':
            break
        else:
            print('Por favor, digite "S" ou "N".')
    if flag in 'Nn':
        break

print('=' * 50)
print('cod  Nome    Gols    total')
for c, jogador in enumerate(time):
    print(f'{c:>3} ', end=' ')
    for v in jogador.values():
        print(f'{str(v):<15}', end=' ')
    print('')
print('=' * 50)

