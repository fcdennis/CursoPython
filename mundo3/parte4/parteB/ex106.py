def pyHelp (cmd):
    print('\033[41m', end='')
    help(cmd)
    print('\033[m', end='')
def cabeçalho1(msg):
    print('\033[102m~' * 40)
    print(f'{msg:^40}')
    print('~' * 40)
    print('\033[m')
def cabeçalho2(msg):
    print('\033[44m~' * 40)
    print(f'{msg:^40}')
    print('~' * 40)
    print('\033[m')


while True:
    cabeçalho1('SISTEMA DE AJUDA PyHELP')
    ajuda = input('Função ou Biblioteca > ').lower().strip()
    if ajuda.upper() == 'FIM':
        break
    else:
        cabeçalho2(f'Acessando o manual do comando {ajuda}')
        pyHelp(ajuda)
