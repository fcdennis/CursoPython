from datetime import date
ano_nasc = int(input("Ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

if idade < 18:
    print(f"Ainda faltam {18 - idade} anos para o alistamento.")
    print(f"Seu alistamento será em {ano_nasc + 18}.")
elif idade > 18:
    print(f"Você já deveria ter se alistado há {idade - 18} anos.")
    print(f"Seu alistamento foi em {ano_nasc + 18}.")
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
