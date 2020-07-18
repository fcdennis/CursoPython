from datetime import date
current_year = date.today().year
born_year = int(input("Ano de Nascimento: "))
idade = current_year - born_year

print(f"O atleta tem {idade} anos.")
print('Clacificação: ', end="")
if idade < 9:
    print('MIRIM\n')
elif idade < 14:
    print('INFANTIL\n')
elif idade < 19:
    print('JÚNIOR\n')
elif idade < 25:
    print('SÊNIOR\n')
else:
    print('MASTER\n')
