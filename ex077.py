#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ("Cachorro", "Pedra", "Carro", "Garrafa", "Teclado")

for i in range(len(palavras)):

    print(f"\nNa palavra {palavras[i].upper()} contem as vogais:", end=" ")
    palavra_atual = palavras[i]
    
    for letra in palavra_atual:
        if letra.upper() in "AEIOU":
            print(letra, end=" ")

