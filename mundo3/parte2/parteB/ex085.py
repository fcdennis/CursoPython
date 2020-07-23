numeros = [[], []]

for c in range(0, 7):
    x = int(input(f'Digite o {c + 1} valor: '))
    if x % 2 == 0:
        numeros[0].append(x)
    else:
        numeros[1].append(x)

print(f'Os valores pares digitados foram {sorted(numeros[0])}')
print(f'Os valores impares digitados foram {sorted(numeros[1])}')
