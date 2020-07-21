contador = n = soma = 0
while n != 999:
    soma += n
    contador += 1
    n = int(input('Digite um número [999 para parar] '))
print(f'Você digitou {contador - 1} números e a soma entre eles foi {soma}')
