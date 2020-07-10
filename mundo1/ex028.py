from random import randint
from time import sleep
print('=-' * 26)
print('Vou pensar em um número entre 1 - 5. Tente advinhar!')
print('=-' * 26)
numero = randint(1, 5)
tentativa = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(3)
if tentativa == numero:
    print(f"PARABÉNS! Você acerou, eu realmente pensei no número {numero}")
else:
    print(f"GANHEI! Pensei no número {numero} e não em {tentativa}")
