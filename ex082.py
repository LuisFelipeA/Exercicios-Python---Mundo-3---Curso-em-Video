# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
par = []
impar = []

while True:
    n = float(input("Digite um numero para adicionar na lista: "))
    lista.append(n)

    continua = input("Deseja continuar? S/N ").upper()[0]
    if continua == "N":
        break

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        par.append(lista[i])

    else:
        impar.append(lista[i])

print(f"Lista: {lista}")
print(f"Lista de Par: {par}")
print(f"Lista de Impar: {impar}")