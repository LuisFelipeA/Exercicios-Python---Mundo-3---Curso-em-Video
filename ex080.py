# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []

for i in range(5):
    n = float(input("Digite um valor para adicionar na lista: "))

    if i == 0 or n >= lista[-1]:
        lista.append(n)
      
    else:
        posicao = 0
        while posicao < len(lista):
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                break
        posicao += 1

print(f"Lista ordenada: {lista}")
