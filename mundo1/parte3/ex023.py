n1 = int(input("Informe um número: "))
n2 = n1 // 10
u = n1 % 10
n3 = n2 // 10
d = n2 % 10
c = n3 % 10
m = n3 // 10

print(f"Unidade {u}")
print(f"Dezena {d}")
print(f"Centena {c}")
print(f"Milhar {m}")
