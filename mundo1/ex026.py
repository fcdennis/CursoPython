frase = input("Digite uma frase: ").upper().strip()
print(f"A letra A aparerece {frase.count('A')} vezes.")
print(f"A letra A apararece pela vez na posição {frase.find('A') + 1}")
print(f"A letra A aparece pela última vez na posição {frase.rfind('A') + 1}")
