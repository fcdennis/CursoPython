expressao = input('Digite uma expressão: ')
abrir = fechar = 0
validar = True

for elemento in expressao:
    if elemento == '(':
        abrir += 1
    elif elemento == ')':
        fechar += 1
    if fechar > abrir:
        validar = False

if validar and abrir == fechar:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está invalida!')
