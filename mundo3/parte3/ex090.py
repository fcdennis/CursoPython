aluno = dict()
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] < 5:
    aluno['situação'] = 'Reprovado'
else:
    aluno['situação'] = 'Recuperação'

print('=' * 50)
for k, v in aluno.items():
    print(f'        → {k} é igual a {v}')
