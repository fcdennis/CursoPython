import csv

def leiaInt(msg):
    while True:
        try:
            numInt = int(input(msg))
        except:
            print('ERRO! Digite um número inteiro válido!')
        else:
            break
    return numInt


def addData():
    with open('cadastro.csv', 'a', newline='') as csv_file:
        fieldnames = ["Nome", "Idade"]
        write = csv.DictWriter(csv_file, fieldnames=fieldnames)

        nome = input('Digite o nome: ').capitalize()
        idade = leiaInt("Digite a idade: ")
        write.writerow({"Nome": nome, "Idade": idade})


def subtractData():
    print("Sorry! We still working on this function. Latter you'll have some news about it.")

def reader():
    with open('cadastro.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_reader.__next__()
        for row in csv_reader:
            print('Nome: ', row[0])
            print('Idade: ', row[1])
