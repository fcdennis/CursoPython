soma = 0
contador = 0
for c in range(0, 6):
    n = int(input("Digite um número inteiro: "))
    if n % 2 == 0:
        soma += n
        contador += 1
print(f'Você informou {contador} números pares e a soma foi {soma}.')
