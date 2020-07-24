matriz = [[], [], []]
somaPar = somaTerceira = 0
for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Digite um valor para [{l}, {c}]: '))
        matriz[l].append(n)
        if n % 2 == 0:
            somaPar += n
        if c == 2:
            somaTerceira += n
        if l == 1:
            if c == 0 or n > maiorSegunda:
                maiorSegunda = n

print('-=' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end=' ')
    print('')
print('-=' * 30)

print(f'A soma dos valores pares é {somaPar}')
print(f'A soma dos valores da terceira coluna é {somaTerceira}')
print(f'O maior valor da segunda linha é {maiorSegunda}')
