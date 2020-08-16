#Testando a nova sintaxe := #

nome = input('Digite seu nome: ')

if(n := len(nome) < 23):
    imprimir = False
else:
    imprimir = True

if (imprimir):
    print('Nome curto')
else:
    print('Nome longo')
