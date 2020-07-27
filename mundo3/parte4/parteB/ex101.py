def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif idade < 18 or idade > 70:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


print('-=' * 15)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
print('-=' * 15)
