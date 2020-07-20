valor = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
prazo = int(input("Quantos anos de financiamento? "))

parcela = valor / (prazo * 12)
parcela_maxima = salario * 0.3

print(f"Para pagar uma casa de R${valor:.2f} em {prazo} anos a prestação será de R${parcela:.2f}.")
if parcela <= parcela_maxima:
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NEGADO!")
