peso = float(input("Qual é o seu peso? (Kg) "))
altura = float(input("Qual é sua altura? (m) "))
imc = peso / (altura ** 2)

print(f"O IMC dessa pessoa é de {imc:.1f}")
print('Você está em ', end='')
if imc < 18.5:
    print('ABAIXO DO PESO.')
elif imc < 25:
    print('PESO IDEAL. PARABÉNS!')
elif imc < 30:
    print('SOBREPESO')
elif imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA, cuidado!')
