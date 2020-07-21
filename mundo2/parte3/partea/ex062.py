print('Gerador de PA v.3')
print('-=' * 9)
pa = primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termos = int(input('Quantos termos quer mostrar? '))
contador = 0
while termos != 0:
    for c in range(0, termos):
        print(pa, end=' → ')
        pa = primeiro_termo + razao
        primeiro_termo = pa
        contador += 1
    print('PAUSA')
    termos = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
print(contador)
