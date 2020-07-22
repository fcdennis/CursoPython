times = 'Liverpool', 'City', 'Chelsea', 'Leicester', 'United', 'Wolves', 'Tottenham', 'Sheffield', 'Burnley', 'Arsenal', 'Everton', 'Southampton', 'Newcastle', 'Crystal Palace', 'Brighton', 'West Ham', 'Aston Villa', 'Watford', 'Bournemouth', 'Norwich'
print(f'Lista de times do campeonato inglês {times} temporada 2019/ 2020')
print(f'Os cinco primeiros são: {times[:5]}')
print(f'Os quatro útimos são: {times[-4:]}')
print(f'Em ordem alfabética a relação é esta: {sorted(times)}')
print(f'O Wolves está em {times.index("Wolves") + 1}º posição')
