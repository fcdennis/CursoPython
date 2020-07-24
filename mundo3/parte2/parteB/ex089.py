classe = []
aluno = []

while True:
    aluno.append(input('Nome: ').capitalize())
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    aluno.append(n1)
    aluno.append(n2)
    aluno.append((n1 + n2) / 2)
    classe.append(aluno[:])
    aluno.clear()
    flag = ' '
    while flag not in 'SsNn':
        flag = input('Quer continuar? [S/N] ').upper().strip()[0]
    if flag in 'Nn':
        break

print('=' * 31)
print('{:<4} {:<20} {:>5}'.format('N°', 'NOME', 'MÉDIA'))
print('-' * 31)
for c in range(0, len(classe)):
    nome = classe[c][0]
    media = classe[c][3]
    print(f'{c + 1:<4} {nome:<20} {media:>5}')

display = 0
while display != 999:
    display = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if display <= len(classe):
        print(f'Notas de {classe[display - 1][0]} são [{classe[display - 1][1]}, {classe[display - 1][2]}]')

print('FINALIZANDO...')
print('{:^25}'.format('<<< VOLTE SEMPRE >>>'))
