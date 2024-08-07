#Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
"""a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense."""

times = ('Corinthians','Palmeiras','Santos','Grêmio','Cruzeiro','Flamengo','Vasco','Chapecoense',
'Atlético','Botafogo','Atlético-PR','Bahia','São Paulo','Fluminense','Sport Recife','EC Vitória',
'Curitiba','Avaí','Ponte preta','Atlético-GO')

print("=_="*30)
print(f"Os primeiro 5 times sao : {times[:5]} ")
print("=_="*30)
print(f"Os ultimos 4 colocados sao: {times[-4]}")
print("=_="*30)
print(f"Os times em ordem alfabetica ficam da seguinte maneira: {sorted(times)}")
print("=_="*30)
print(f"O Chapecoense esta na posicao {times.index('Chapecoense')+1}.")
