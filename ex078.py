#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = []

for i in range(5):
    numeros.append(float(input("Digite um valor: ")))

posicao_menor = menor = posicao_maior = maior = numeros[0]

for posicao, valor in enumerate(numeros):
    if menor >= valor:
        menor = valor
        posicao_menor = posicao

    if maior <= valor:
        maior = valor
        posicao_maior = posicao

print(f"O maior numero digitado foi {maior} na posição {posicao_maior} e o menor foi {menor} na posição {posicao_menor}")