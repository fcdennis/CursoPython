import time as tm
def contador(a, b, c):
    if c == 0:
        c = 1
    else:
        c = abs(c)
    print(f'Contado de {a} até {b} no passo {c}')
    if a < b:
        while a <= b:
            print(a, end=' ', flush=True)
            a += c
            tm.sleep(0.3)
    elif a > b:
        while a >= b:
            print(a, end=' ', flush=True)
            a -= c
            tm.sleep(0.3)
    print('FIM!')


print('=' * 50)
contador(0, 10, 1)
print('=' * 50)
contador(10, 0, 1)
print('=' * 50)
print('Agora é sua vez de personalizar a contagem!')
x = int(input('Início: '))
y = int(input('Fim: '))
z = int(input('Passo: '))
contador(x, y, z)
