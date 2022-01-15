# Aprimore o desafio anterior, mostrando no final:
# a) A soma de todos os valores pares digitados.
# b) A soma dos valores da terceira coluna.
# c) O maior valor da segunda linha.


# entrada de dados

matriz = [[],[],[]]

for linha in range(3):
    for coluna in range(3):
        n1 = float(input(f"Digite um valor para adicionar na matriz: "))
        matriz[linha].append(n1)

print("-"*30)

# mostrar matriz

for linha in range(3):
    for coluna in range(3):
        print(f"[{matriz[linha][coluna]:^7}]", end=" ")
    print()

print("-"*30)

# soma dos numeros pares

paresSoma = 0

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if matriz[linha][coluna] % 2 == 0:
            paresSoma = paresSoma + matriz[linha][coluna]

print(f"A soma dos numeros pares é {paresSoma}")

print("-"*30)

# soma dos numeros da terceira coluna

terceiraColuna = 0

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if matriz[linha][coluna] == matriz[linha][2]:
            terceiraColuna = terceiraColuna + matriz[linha][coluna]

print(f"A soma da terceira coluna é {terceiraColuna}")

print("-"*30)

# maior valor da segunda linha

maiorSegundaLinha = 0

for linha in range(len(matriz)):
    if matriz[linha] == matriz[1]:
            for coluna in range(len(matriz[linha])):

                if maiorSegundaLinha == 0:
                    maiorSegundaLinha = matriz[linha][coluna]

                else:
                    if maiorSegundaLinha <= matriz[linha][coluna]:
                        maiorSegundaLinha = matriz[linha][coluna]

print(f"O maior numero da segunda linha é {maiorSegundaLinha}") 

print("-"*30)