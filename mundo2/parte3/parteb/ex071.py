print('=' * 30)
print('{:^30}'.format('BANCO COSTA'))
print('=' * 30)

''' Minha solução gigante
while True:
    saque = int(input('Que valor você quer sacar? R$'))
    cem = saque // 100
    resto_cem = saque % 100
    cinquenta =  resto_cem // 50
    resto_cinquenta = resto_cem % 50
    vinte = resto_cinquenta // 20
    resto_vinte = resto_cinquenta % 20
    dez =  resto_vinte // 10
    resto_dez = resto_vinte % 10
    resto = cinco = dois = 0
    if resto_dez % 2 != 0:
        cinco = resto_dez // 5
        resto_cinco = resto_dez % 5
        dois =  resto_cinco // 2
        resto = resto_cinco % 2
    else:
        dois = resto_dez // 2

    flag = ' '
    if resto != 0:
        print('ESTE VALOR NÃO HÁ COMBINAÇÃO DE NOTAS PARA SAQUE.')
    else:
        if cem != 0:
            print(f'Total de {cem} nota de R$100,00')
        if cinquenta != 0:
            print(f'Total de {cinquenta} notas de R$50,00')
        if vinte != 0:
            print(f'Total de {vinte} notas de R$20,00')
        if dez != 0:
            print(f'Total de {dez} notas de R$10,00')
        if cinco != 0:
            print(f'Total de {cinco} notas de R$5,00')
        if dois != 0:
            print(f'Total de {dois} notas de R$2,00')
    while flag not in 'SsNn':
        flag = input('Deseja realizar outro saque? [S/N] ').upper().strip()[0]
    if flag in 'Nn':
        break'''

'''Solução alternativa do Guanabara'''
valor = int(input('Valor do saque? R$'))
total = valor
ced = 100
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao Banco Costa! Tenha um execelente dia!')
