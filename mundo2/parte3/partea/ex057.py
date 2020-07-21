sexo = input('Informe seu sexo: [F/M] ').strip().upper()[0]
while sexo not in 'FfMm':
    sexo = input('Informe seu sexo: [F/M] ').strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
