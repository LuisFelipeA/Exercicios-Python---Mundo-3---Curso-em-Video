# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até dez. Seu programa deverá ler um número pelo teclado (entre 0 e 10) e mostrá-lo por extenso.

extenso = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenova", "vinte")

while True:
    
    n = int(input("Digite um numero entre 0 e 20: "))
    if n >= 0 and n <=20:
        print(f"O numero digitado foi {extenso[n]}")
        
    continua = input("Deseja continuar? [S/N]: ").upper()[0]
    if continua == "N":
        break