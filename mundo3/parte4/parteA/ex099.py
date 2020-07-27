from time import sleep
def maiorLista(*lista):
    print('=-' * 30)
    if not lista:
        print('Nenhum parametro atribuido! Não há valores para definir qual é o maior!')
    else:
        lst = lista
        for c in lst:
            print(c, end=' ', flush=True)
            sleep(0.5)
        print(f'Foram informados {len(lst)} valores ao todo.')
        print(f'O maior valor informado foi {max(lst)}')
    


maiorLista(2, 9, 4, 5, 7, 1)
maiorLista(4, 7, 0)
maiorLista(1, 2)
maiorLista(6)
maiorLista()
