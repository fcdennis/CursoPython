def leiaInt(msg):
    while True:
        try:
            numInt = int(input(msg))
        except:
            print('ERRO! Digite um número inteiro válido!')
        else:
            break
    return numInt
