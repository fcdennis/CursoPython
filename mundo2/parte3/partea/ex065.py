continuar = 'S'
contador = soma = maior = 0
while continuar not in 'Nn':
    n1 = int(input('Digite um número: '))
    soma += n1
    contador += 1
    if maior == 0:
        maior = n1
        menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    continuar = input('Quer continuar? [S/N] ').upper().strip()[0]
print(f'Você digitou {contador} números, a média foi de {(soma/contador):.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
