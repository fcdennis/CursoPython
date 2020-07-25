from datetime import date
pessoa = dict()
pessoa['nome'] = input('Nome: ').capitalize()
nascimento = int(input('Ano de Nascimento: '))
pessoa['idade'] = date.today().year - nascimento
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = (pessoa['contratação'] - nascimento) + 35

for k, v in pessoa.items():
    print(f'    →{k} tem o valor {v}')
