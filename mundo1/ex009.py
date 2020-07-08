base = int(input("Digite um número para ver sua tabuada: "))
print('-' * 20)
for c in range(1, 11):
    print(f"{base:2} X {c:2} = {c*base:3}")
print('-'*20)
