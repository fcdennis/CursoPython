salario_base = float(input("Qual é o salário do Funcionário? R$"))
reajuste = salario_base + ((salario_base * 15) / 100)
print(f"Um funcionário que ganhava R${salario_base:.2f}, com 15% de aumento, passa a receber {reajuste:.2f}")
