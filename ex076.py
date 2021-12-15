# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

carros = ("Fusca", 2500, "Astra", 14000, "Golf", 25000, "Azera", 35000, "Corolla", 45000, "C 200", 65000, "535i", 100000)

qtd_carros = len(carros)

modelo = 0
preco = 1

print("-"*47)
print(f'{"Tabela de preços":^47}')
print("-"*47)

while True:
    print(f"  Modelo: {carros[modelo]:.<15} Preço: R${carros[preco]:.2f}")

    modelo += 2
    preco += 2

    if modelo == (len(carros)):
        break

print("-"*47)