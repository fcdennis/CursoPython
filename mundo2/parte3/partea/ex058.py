from random import randint
computador = randint(0, 10)
print('Sou seu computador...\nAcabei de pensar e um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
palpite = int(input('Qual é o seu palpite? '))
contador = 1
while palpite != computador:
    contador += 1
    if palpite > computador:
        print('Menos... Tente mais uma vez.')
        palpite = int(input('Qual é o seu palpite? '))
    else:
        print('Mais... Tente mais uma vez.')
        palpite = int(input('Qual é o seu palpite? '))
print(f'Acertou em {contador} tentativa. Parabéns!')
