def fatorial(n = 0, show = False):
    """
    -> Calcula o Fatorial de um numero inteiro.
    :param n: Número inteiro a ser calculado fornecido pelo usuario;
    :param show: imprime os passos realizados para o cálculo do fatorial de n.
    :return: O valor do Fatorial de um numero N Inteiro qualquer fornecido pelo usuario.
    """
    if show == True:
        for c in range(n, 0, -1):
            print (f'{c} =' if c == 1 else f'{c} X', end=' ')
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
    

help(fatorial)
