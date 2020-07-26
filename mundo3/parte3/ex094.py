from operator import itemgetter
pessoa = dict()
grupo = list()
soma = 0
while True:
    pessoa['Nome'] = input('Nome: ')
    pessoa['Sexo'] = ' '
    while True:
        pessoa['Sexo'] = input('Sexo: [F/M] ').upper().strip()[0]
        if pessoa['Sexo'] in 'FfMm':
            break
        else:
            print('Por favor, digite apenas F ou M.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    grupo.append(pessoa.copy())
    flag = ' '
    while flag not in 'SsNn':
        flag = input('Quer continuar? [S/N] ').upper().strip()[0]
        if flag not in 'SsNn':
            print('Por favor, digite apenas S ou N.')
    if flag in 'Nn':
        break

media = soma / len(grupo)
print('=' * 50)
print(f'Ao todo temos {len(grupo)} pessoas cadastradas.')
print(f'A média de idade é de {media:.1f} anos de idade')
print('As mulheres cadastradas foram:', end=' ')
for pessoa in grupo:
    if pessoa['Sexo'] == 'F':
        print(pessoa['Nome'], end=' ')
print('\nLista das pessoas que estão acima da média de idade:')
for pessoa in grupo:
    if pessoa['Idade'] > media:
        for k,v in pessoa.items():
            print(f'        {k} = {v:15}', end=' ')
        print('')
