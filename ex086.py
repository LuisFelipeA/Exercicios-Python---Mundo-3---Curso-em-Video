# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[],[],[]]

for linha in range(3):
    for coluna in range(3):
        n1 = float(input(f"Digite um valor para adicionar na matriz: "))
        matriz[linha].append(n1)


print("-"*30)

for linha in range(3):
    for coluna in range(3):
        print(f"[{matriz[linha][coluna]:^7}]", end=" ")
    print()

print("-"*30)