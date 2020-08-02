def leiaInt(msg):
    while True:
        try:
            numInt = int(input(msg))
        except:
            print('ERRO! Digite um número inteiro válido!')
        else:
            break
    return numInt


def leiaFloat(msg):
    while True:
        try:
            numFloat = float(input(msg))
        except:
            print('ERRO! Digite um número real válido!')
        else:
            break
    return numFloat


numeroInteiro = leiaInt('Digite um número inteiro: ')
numeroReal = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro: {numeroInteiro}')
print(f'Você acabou de digitar o número real: {numeroReal}')