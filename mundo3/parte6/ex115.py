import csv
from ex115 import formatacao
from ex115 import dados

cadastro = csv.open('cadastro.csv', 'a')
pessoaCadastrada = {'nome': "Dennis Costa", 'idade': 37}
grupoCadastrado = [pessoaCadastrada]
cadastro.writelines(grupoCadastrado)

formatacao.linha()
print('{:^30}'.format('MENU PRINCIPAL'))
formatacao.linha()

while True:
    formatacao.linha()
    print("1 - VER PESSOAS CADASTRADAS")
    print("2 - CADASTRAR NOVA PESSOA")
    print("3 - SAIR")
    formatacao.linha()
    opc = dados.leiaInt('Sua opção: ')
    if opc == 1:
        print(grupoCadastrado)
        break
    elif opc == 2:
        print('opc 2')
        break
    elif opc == 3:
        print('Obrigado e até a próxima!')
        break
    else:
        print('Digite uma opção válida.')
