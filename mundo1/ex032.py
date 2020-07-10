from datetime import date
ano = int(input("Qual ano quer analisar? 0 = atual: "))
ano_atual = date.today().year
if ano == 0:
    ano = ano_atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é Bissesto")
else:
    print(f"O ano {ano} NÃO é Bissesto")
