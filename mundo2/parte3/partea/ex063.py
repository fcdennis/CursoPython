print('-' * 22)
print('Sequência de Fibonacci')
print('-' * 22)
termos = int(input('Quantos termos você quer mostrar? '))
n1 = 0
n2 = 1
contador = 0
print('~' * (5 * termos))
while contador < termos:
    print(n1, end=' → ')
    aux = n1 + n2
    n1 = n2
    n2 = aux
    contador += 1
print('FIM')
print('~' * (5 * termos))
