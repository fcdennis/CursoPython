print('Gerador de PA v.2')
print('-=' * 9)
pa = primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termos = 0
while termos < 10:
    print(pa, end=' → ')
    pa = primeiro_termo + razao
    primeiro_termo = pa
    termos += 1
print('FIM')
