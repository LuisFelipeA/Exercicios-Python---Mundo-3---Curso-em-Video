# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random
import time

palpite = []

qtdJogos = int(input("Digite a quantidade de jogos que sera gerado: "))

for jogo in range(qtdJogos):
    jogoAtual = []
    while True:
        numero = random.randint(1,60)
        if numero not in jogoAtual:
            jogoAtual.append(numero)
        if len(jogoAtual) == 6:
            break
    palpite.append(jogoAtual)

print("-"*32)
print("Criador de palpites da MEGA SENA")
print("-"*32)

for i in range(qtdJogos):
    print(f"Jogo {i + 1}: {palpite[i]}")
    time.sleep(1)

print("-"*32)
print("-"*11, "Boa Sorte", "-"*10)
print("-"*32)
