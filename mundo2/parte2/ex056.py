soma = menor = velho = 0
for c in range(0, 5):
    print('-' * 5, f'{c + 1}ª PESSOA', '-' * 5)
    nome = input('Nome: ').capitalize()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    soma += idade
    if sexo in 'Ff' and idade < 20:
        menor += 1
    if sexo in 'Mm':
        if idade > velho:
            velho = idade
            nome_velho = nome
media = soma / 5
print(f"A média de idade do grupo é de {media:.1f} anos.")
if velho == 0:
    print('Não há homens na lista!')
else:
    print(f"O homem mais velho tem {velho} e se chama {nome_velho} ")
if menor == 0:
    print('Não há mulheres na lista!')
else:
    print(f"Ao todo são {menor} mulheres com menos de 20 anos de idade.")
