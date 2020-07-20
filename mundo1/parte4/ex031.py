distancia = float(input("Qual é a distância da sua viagem? "))
if distancia <= 200:
    print(f"Você está prestes a começar uma viagem de {distancia:.2f}Km.")
    print(f"E o preço da sua passagem será de R${distancia * 0.5:.2f}")
else:
    print(f"Você está prestes a começar uma viagem de {distancia:.2f}Km.")
    print(f"E o preço da sua passagem será de R${distancia * 0.45:.2f}")
