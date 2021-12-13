#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.

# b) Os últimos 4 colocados.

# c) Times em ordem alfabética.

# d) Em que posição está o time da Chapecoense.

tabela = ("Atlético-MG", "Flamengo", "Palmeiras", "Fortaleza", "Corinthians", "Bragantino", "Fluminense", "América-MG", "Atlético-GO", "Santos", "Ceará", "Internacional", "São Paulo", "Athletico-PR", "Cuiabá", "Juventude", "Grêmio", "Bahia", "Sport", "Chapecoense")

print("-"*5)


print("5 primeiros:")
posicao = 1
for c in range(5):
    print(f"{posicao}º colocado: {tabela[c]}")
    posicao += 1

print("-"*5)

print("4 ultimos:")
tabela_invertida = tabela[::-1]
posicao = 20
for c in range(4):
    print(f"{posicao}º colocado: {tabela_invertida[c]}")
    posicao -= 1

print("-"*5)

ordenada = sorted(tabela)
print(f"Lista em ordem alfabetica: {ordenada}")

print("-"*5)

pos_chapeco = tabela.index("Chapecoense")+1
print(f"Chapecoense esta na {pos_chapeco}ª posição")

print("-"*5)
