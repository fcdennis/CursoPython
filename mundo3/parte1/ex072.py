numeros = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    disclaimer = int(input('Digite um número entre 0 e 20: '))
    if 0 <= disclaimer < 21:
        print(f'Você digitou o número {numeros[disclaimer]}')
        break
