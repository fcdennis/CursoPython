from random import randint
from time import sleep

def sorteio(num):
    lst = list()
    print(f'Sorteando {num} valores da lista', end=' ', flush=True)
    sleep(0.5)
    for c in range(0, num):
        lst.append(randint(0, 9))
    print(lst, end=' ')
    print('PRONTO!', flush=True)
    sleep(0.5)
    return lst


def somaPar(listagem):
    somaPar = 0
    for v in listagem:
        if v % 2 == 0:
            somaPar += v
    print(f'Somando os valores pares de {listagem}', end='', flush=True)
    sleep(0.5)
    print(f', temos {somaPar}.')


lista = sorteio(5)
somaPar(lista)
