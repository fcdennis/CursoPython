def dobro(num, formatado=False):
    if formatado:
        return f'R${num * 2:.2f}'
    else:
        return num * 2


def metade(num, formatado=False):
    if formatado:
        return f'R${num / 2:.2f}'
    else:
        return num / 2


def adicionar(num, index, formatado=False):
    if formatado:
        return f'R${num + (num / 100 * index):.2f}'
    else:
        return num + (num / 100 * index)


def descontar(num, index, formatado=False):
    if formatado:
        return f'R${num - (num / 100 * index):.2f}'
    else:
        return num - (num / 100 * index)


def cifrar(num):
    return f'R${num:.2f}'


def resumo(valor, aumento, desconto):
    print('-' * 40)
    print('{:^40}'.format('RESUMO DO VALOR'))
    print('¯' * 40)
    print('Preço analisado:', end='')
    print(f'{(cifrar(valor)):>24}')
    print('Dobro do Preço:', end='')
    print(f'{dobro(valor, True):>25}')
    print(f'Metado do Preço', end='')
    print(f'{metade(valor, True):>25}')
    print(f'{aumento}% de aumento:', end='')
    print(f'{adicionar(valor, aumento, True):>25}')
    print(f'{desconto}% de desconto:', end='')
    print(f'{descontar(valor, desconto, True):>24}')
    print('¯' * 40)
