salario_base = float(input("Qual é o salário do Funcionário? R$"))
print(f"Um funcionário que ganhava R${salario_base:.2f}, com 15% de aumento, passa a receber {(salario_base + ((salario_base * 15) / 100)):.2f}")
