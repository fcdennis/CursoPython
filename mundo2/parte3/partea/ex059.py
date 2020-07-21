from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
fim = True
while fim:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    opc = int(input('Qual é a sua opção? '))
    sleep(0.5)
    if opc == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}.')
        sleep(1)
    elif opc == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}')
        sleep(1)
    elif opc == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior é {n1}')
        else:
            print(f'Entre {n1} e {n2} o maior é {n2}')
        sleep(1)
    elif opc == 4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        sleep(1)
    elif opc == 5:
        fim = False
    else:
        print('Opção invalida!')
        sleep(1)
