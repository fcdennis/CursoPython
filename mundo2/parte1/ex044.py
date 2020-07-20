print('=' * 8, 'LOJAS DENNIS', '='*8)
preco = float(input("Preço das compras: R$"))
print('FORMAS DE PAGAMENTO')
print('[1] à vista dinheiro')
print('[2] à vista no cartão')
print('[3] 2x no cartão')
print('[4] Parcelado no cartão')
opc = int(input("QUAL É A OPÇÃO? "))

if opc == 1:
    print(f"Sua compra de R${preco:.2f} vai custar R${(preco * 0.90):.2f} com desconto!")
elif opc == 2:
    print(f"Sua compra de R${preco:.2f} ficou no valor de R${(preco * 0.95):.2f}")
elif opc == 3:
    print(f"Sua compra de R${preco:.2f} vai ser paga em 2 parcelas de R${(preco / 2):.2f}.")
elif opc == 4:
    parc = int(input("Quantas parcelas? "))
    print(f"Sua compra de R${preco:.2f} vai ser paga em {parc} parcelas de R${((preco / parc) * 1.2):.2f}")
else:
    print('OPÇÃO INVÁLIDA!')
