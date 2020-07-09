dias = float(input("Quantos dias alugados? "))
km = float(input("Quantos km rodados? "))
print(f"Andando {km}km por {dias} dias, o preço total será R${((km * 0.15) + (dias * 60)):.2f}.")
