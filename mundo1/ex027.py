nome = input("Digite seu nome completo: ").strip()
palavras = nome.split()
print("Muito prazer em te conhecer!")
print(f"Seu primeiro nome é {palavras[0]}.")
print(f"Seu último nome é {palavras[len(palavras) - 1]}.")
