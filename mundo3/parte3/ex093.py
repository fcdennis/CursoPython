jogador = dict()
gol = list()
jogador['nome'] = input('Nome do Jogador: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, partidas):
    gol.append(int(input(f'     Quantos gols na partida {c + 1}: ')))
jogador['gols'] = gol.copy()
jogador['total'] = sum(gol)
print('=' * 50)
print(jogador)
print('=' * 50)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('=' * 50)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'    => Na partida {c + 1:2}, fez {gol[c]} gols.')
print(f'Foi um total de {jogador["total"]:2} gols.')
