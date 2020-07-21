n1 = int(input('Digite um número para calcular seu fatorial: '))
fator = n1
fatorial = 1
print(f'Calculando {n1}! =', end=' ')
while fator > 0:
    print(fator, end='')
    print(' X ' if fator > 1 else ' = ', end='')
    fatorial *= fator
    fator -= 1
print(fatorial)
