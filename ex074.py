# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

tupla = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))

print(f"Os valores sorteado foram: {tupla}")

print(f"O maior numero sorteado foi {max(tupla)}")
print(f"O menor numero sorteado foi {min(tupla)}")