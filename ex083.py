# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = input("Digite uma expressão: ")
abrindo = []
fechando = []

for i in range(len(expressao)):
    if expressao[i] == "(":
        abrindo.append(expressao[i])
    elif expressao[i] == ")":
        fechando.append(expressao[i])

if len(abrindo) == len(fechando):
    print(f"A expressão {expressao} é valida")
else:
    print(f"A expressão {expressao} não é valida")