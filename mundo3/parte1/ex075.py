tupla = int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite um terceiro número: ')), int(input('Digite um último número: '))
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 aparece {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O valor 3 aparece na {tupla.index(3) + 1}ª posição.')
print('Os valores pares digitados foram: ', end='')
for numero in tupla:
    if numero % 2 == 0:
        print(numero, end=' ')
