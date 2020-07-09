dias = float(input("Quantos dias alugados? "))
km = float(input("Quantos km rodados? "))
preco = (km * 0.15) + (dias * 60)
print(f"Andando {km}km por {dias} dias, o preço total será R${preco:.2f}.")
