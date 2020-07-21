maiores = homens = mulheres_menores = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = input('Sexo: [F/ M] ').upper().strip()[0]
    while sexo not in 'FfMm':
        sexo = input('Sexo: [F/ M] ').upper().strip()[0]
    if idade >= 18:
        maiores += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulheres_menores += 1
    flag = input('Quer continuar? [S/N] ').upper().strip()[0]
    while flag not in 'SsNn':
        flag = input('Quer continuar? [S/N] ').upper().strip()[0]
    if flag in 'Nn':
        break
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres_menores} mulher com menos de 20 anos.')
