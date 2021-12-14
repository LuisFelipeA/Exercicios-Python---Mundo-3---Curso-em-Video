# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.

# B) Em que posição foi digitado o primeiro valor 3.

# C) Quais foram os números pares.

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n3 = int(input("Digite um numero: "))
n4 = int(input("Digite um numero: "))

tupla = (n1, n2, n3, n4)

nove = 0

for i in range(len(tupla)):
    n = tupla[i]

    if n == 9:
        nove += 1 


print(f"Apareceu o valor nove {nove} vezes")

if 3 in tupla:
    print(f"Foi digitado o primeiro valor tres na posição {tupla.index(3)}")

else:
    print("O valor tres não foi digitado")

print(f"Numeros pares:", end =' ')
for i in range(len(tupla)):

    if tupla[i]%2 == 0:
        print(tupla[i], end=' ')

