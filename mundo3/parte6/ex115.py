from ex115 import fmt, dados

while True:
    opc = fmt.menuOpc()
    if opc == 1:
        dados.reader()
    elif opc == 2:
        fmt.dataManagement()
    elif opc == 3:
        print('Obrigado e até a próxima!')
        break
    else:
        print('Digite uma opção válida.')
