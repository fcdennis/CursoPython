from time import sleep
from random import randint
print('-' * 40)
print('{:^40}'.format('JOGA NA MEGA SENA'))
print('-' * 40)

numerosDaMega = list()
contador = 0
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
while contador < jogos:
    for c in range(0, 6):
        numerosDaMega.append(randint(1, 60))
    print(f'Jogo {contador + 1}: {sorted(numerosDaMega)}')
    numerosDaMega.clear()
    contador += 1
    sleep(0.7)

print('{:=^40}'.format(' < BOA SORTE! > ') )
