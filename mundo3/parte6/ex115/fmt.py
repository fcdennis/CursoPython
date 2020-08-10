from ex115 import dados

def linha():
    print('-' * 30)


def menuOpc():
    linha()
    print('{:^30}'.format('MENU PRINCIPAL'))
    linha()
    print("1 - RELATÓRIO DOS CADASTROS")
    print("2 - MENU DE CADASTRO")
    print("3 - SAIR")
    linha()
    opc = dados.leiaInt('Sua opção: ')
    return opc


def dataManagement():
    linha()
    print('Você deseja:')
    print('[1] - ADICIONAR NOVA PESSOA')
    print('[2] - EXCLUIR PESSOA CADASTRADA')
    dataopc = dados.leiaInt('Sua opção: ')
    while True:
        if dataopc == 1:
            dados.addData()
            break
        elif dataopc == 2:
            dados.subtractData()
            break
        else:
            print('Digite uma opção válida')
