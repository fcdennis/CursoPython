from random import randint
print('=-' * 13)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 13)
placar = 0
while True:
    computador = randint(0, 9)
    jogador = int(input('Diga um valor? '))
    total = computador + jogador
    pergunta = input('Par ou Ímpar? [P / I] ')
    while pergunta not in 'PpIi':
        pergunta = input('Par ou Ímpar? [P / I] ')
    print(f'O computador jogou {computador} e você jogou {jogador}.')
    print(f'O total é {total}.')
    if pergunta in 'Pp' and total % 2 == 0 or pergunta in 'Ii' and total % 2 != 0:
        print('Você VENCEU!')
        placar += 1
    else:
        print('Você PERDEU')
    continuar = input('Quer jogar de novo? [S/N] ')
    while continuar not in 'SsNn':
        continuar = input('Quer jogar de novo? [S/N] ')
    if continuar in 'Nn':
        break
print(f'GAME OVER! Você venceu {placar} vezes.')
