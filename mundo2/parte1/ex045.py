from time import sleep
from random import randint

computador = randint(1, 3)
print('Suas opções: ')
print('[1] PEDRA')
print('[2] PAPEL')
print('[3+] TESOURA')
humano = int(input("Qual é a sua jogada? "))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print("-=" * 20)
print('Computador jogou ', end='')
if computador == 1:
    print('PEDRA')
elif computador == 2:
    print('PAPEL')
else:
    print('TESOURA')
print('Jogador jogou ', end='')
if humano == 1:
    print('PEDRA')
elif humano == 2:
    print('PAPEL')
else:
    print('TESOURA')
print("-=" * 20)

if computador == 1 and humano == 3 or computador == 2 and humano == 1 or computador == 3 and humano == 2:
    print('COMPUTADOR VENCE')
elif computador == 1 and humano == 2 or computador == 2 and humano == 3 or computador == 3 and humano == 1:
    print('JOGADOR VENCE')
else:
    print('EMPATE!')
