for c in range(0, 5):
    peso = float(input(f"Peso da {c + 1} pessoa: "))
    if c == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso lido foi de {maior}kg.")
print(f"O menor peso lido foi de {menor}kg.")
