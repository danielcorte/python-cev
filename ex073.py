# Exercício Python 073: Crie uma tupla preenchida com os 20
# primeiros colocados da Tabela do Campeonato Brasileiro de
# Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athlético-PR', 'Atlético-MG',
         'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá',
         'Ceará SC', 'Atlético-GO', 'Avaí', 'Juventude')
print('-=' * 15)
print(f"Lista de times do Brasileirão: {times}")
print('-=' * 15)
print(f"Os cinco primeiros: {times[0:5]}")
print('-=' * 15)
print(f"Os últimos 4 colocados: {times[-4:]}")
print('-=' * 15)
print(f"Times em ordem alfabética: {sorted(times)}")
print('-=' * 15)
print(f"O Corinthians está na {times.index('Corinthians') +1}ª posição")
print('-=' * 15)