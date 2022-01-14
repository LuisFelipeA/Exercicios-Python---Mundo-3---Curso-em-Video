# Aprimore o desafio anterior, mostrando no final:
# a) A soma de todos os valores pares digitados.
# b) A soma dos valores da terceira coluna.
# c) O maior valor da segunda linha.

matriz = [[],[],[]]

for coluna in range(len(matriz)):
    for linha in range(3):
        n1 = float(input(f"Digite um valor para adicionar na matriz: "))
        matriz[coluna].append(n1)


print("-"*30)

for coluna in range(len(matriz)):
    for linha in range(3):
        print(f"[{matriz[linha][coluna]:^7}]", end=" ")
    print()

print("-"*30)

pares = []

for coluna in range(len(matriz)):
    for linha in range(len(matriz[coluna])):
        if matriz[coluna][linha] % 2 == 0:
            pares.append(matriz[coluna][linha])

print(f"os numeros pares são {pares}")