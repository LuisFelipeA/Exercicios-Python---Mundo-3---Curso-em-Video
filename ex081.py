# Crie um programa que vai ler vários números e colocar em uma lista.                  Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    n = float(input("Digite um numero para adicionar na lista: "))
    lista.append(n)

    continua = input("Deseja continuar? S/N").upper()[0]
    if continua == "N":
        break

print(f"Foi digitado {len(lista)} numeros")

decrescente = sorted(lista, reverse=True)

print(f"Lista em ordem decrescente {decrescente}")

if 5 in lista:
    print("O numero 5 esta na lista")

else:
    print("O numero 5 não esta na lista")

