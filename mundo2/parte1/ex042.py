print('-=' * 40)
print('Analisador de Triângulos')
print('-=' * 40)
l1 = float(input("Primeiro segmento: "))
l2 = float(input("Segundo segmento: "))
l3 = float(input("Terceiro segmento: "))

if abs(l2 - l3) < l1 < l2 + l3 and abs(l1 - l3) < l2 < l1 + l3 and abs(l1 - l2) < l3 < l1 + l2:
    print('Os segmentos acima PODEM FORMAR triângulo ', end='')
    if l1 == l2 and l2 == l3:
        print('EQUILÁTERO!')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('ISÓCELES!')
    else:
        print('ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo!')
