from time import sleep
while True:
    n1 = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 36)
    if n1 < 0:
        break
    for c in range(1, 11):
        print(f'{n1:2} X {c:2} = {n1 * c:3}')
    print('-' * 36)
    sleep(1)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
