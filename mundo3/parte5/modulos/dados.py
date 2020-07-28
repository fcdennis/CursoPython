def currency(msg):
    valor = ''
    while True:
        valor = input(msg).strip()
        contador = 0
        valido = True
        for c in valor:
            if c.isalpha():
                valido = False
            elif c in ',.':
                contador += 1
                if contador > 1:
                    valido = False
        if valido:
            valor = valor.replace(',', '.')
            break
        else:
            print('ERRO! Digite um preço valido!')
    return float(valor)
