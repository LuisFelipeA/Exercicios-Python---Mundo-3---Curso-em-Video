# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = []

while True:
    n = float(input("Digite um numero: "))
    if n not in numeros:
        numeros.append(n)
    
    mais = input("Digitar mais numeros? S/N").upper()
    if mais == "N":
        break

print(f"Valores digitados: {sorted(numeros)}")