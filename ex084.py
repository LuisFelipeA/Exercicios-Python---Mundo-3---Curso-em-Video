# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = []
dados = []
maior_peso = menor_peso = 0
pessoa_pesada = pessoa_leve = 0

while True:
    dados.append(input("Digite o nome: "))
    dados.append(float(input("Digite o peso: ")))
    pessoas.append(dados[:])
    dados.clear()

    continuar = input("Adicionar mais pessoas? S/N ").lower()[0]
    if continuar == "n":
        break




for p in pessoas:
    if menor_peso == 0:
        maior_peso = p[1]
        menor_peso = p[1]
    
    else:
        if p[1] > maior_peso:
            maior_peso = p[1]
            pessoa_pesada = p[0]
        
        if p[1] < menor_peso:
            menor_peso = p[1]
            pessoa_leve = p[0]





print(f"Foram cadastradas {len(pessoas)} pessoas")

print(f"O maior peso foi {maior_peso}Kg das pessoas:",end =" ")
for p in pessoas:
    if p[1] == maior_peso:
        print(f"[{p[0]}]", end=" ")

print()

print(f"O menor peso foi {menor_peso}Kg das pessoas:",end =" ")
for p in pessoas:
    if p[1] == menor_peso:
        print(f"[{p[0]}]", end=" ")