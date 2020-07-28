def jogador(nome, gols):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato'


nome = input('Nome do Jogador: ')
if not nome.isalpha():
    nome = '<desconhecido>'
gols = input('Número de Gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

print(jogador(nome, gols))
