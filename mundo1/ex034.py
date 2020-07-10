base = float(input("Qual é o salário do funcionário? R$"))
if base > 1250:
    novo = base + (base * 10 / 100)
else:
    novo = base + (base * 15 / 100)
print(f"Quem ganhava R${base:.2f} passa a ganhar R${novo:.2f}")
