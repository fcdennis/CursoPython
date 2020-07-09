from math import hypot
cateto_oposto = float(input("Comprimento do cateto oposto: "))
cateto_adjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa = hypot(cateto_adjacente, cateto_oposto)
print(f"A hipotenusa é {hipotenusa}")
