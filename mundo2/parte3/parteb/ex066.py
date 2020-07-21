soma = contador = 0
while True:
    n1 = int(input("Digite um valor (999 para parar): "))
    if n1 == 999:
        break
    soma += n1
    contador += 1
print(f'A soma dos {contador} valores foi {soma}!')
