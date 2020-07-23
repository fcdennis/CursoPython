pessoas = list()
dados = list()

while True:
    dados.append(input('Nome: ').capitalize())
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    flag = ' '
    while flag not in 'SsNn':
        flag = input('Quer continuar? [S/N] ').upper().strip()[0]
    if flag in 'Nn':
        break
print(f'Ao todo você cadastrou {len(pessoas)}')

maior = menor = 0.0
nome_maior = list()
nome_menor = list()

for p in range(0, len(pessoas)):
    if p == 0:
        maior = menor = pessoas[p][1]
        nome_maior.append(pessoas[p][0])
        nome_menor.append(pessoas[p][0])
    else:
        if pessoas[p][1] > maior:
            maior = pessoas[p][1]
            nome_maior.pop()
            nome_maior.append(pessoas[p][0])
        elif pessoas[p][1]  == maior:
            nome_maior.append(pessoas[p][0])
        elif pessoas[p][1] < menor:
            menor = pessoas[p][1]
            nome_menor.pop()
            nome_menor.append(pessoas[p][0])
        elif pessoas[p][1] == menor:
            nome_menor.append(pessoas[p][0])
print(f'O maior peso foi de {maior:.1f}Kg. Peso de {nome_maior}')
print(f'O menor peso foi de {menor:.1f}Kg. Peso de {nome_menor}')
