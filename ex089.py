# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = []

while True:
    addAluno = []
    
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    
    addAluno.append(nome)
    addAluno.append(nota1)
    addAluno.append(nota2)

    alunos.append(addAluno)

    continua = input("Deseja adicionar outro aluno? [S/N]").lower()[0]
    if continua == "n":
        break

print(" ")
print("*"*31)
print(f"|Nº |     Nome     ", "|   Média |")
print("-"*31)

for posicao in range(len(alunos)):
    print("|",posicao, end="  | ")
    print(f"{alunos[posicao][0]:^12}", end="  | ")
    media = (alunos[posicao][1] + alunos[posicao][2]) / 2
    print(f"  {media:.1f}  |")

print("*"*31)

while True:
    print(" ")
    separado = int(input("Deseja mostrar a nota de qual aluno? [999 para finalizar]: "))
    if separado == 999:
        break
    else:
        print(f"Notas de {alunos[separado][0]} são {alunos[separado][1]} e {alunos[separado][2]} ")
print(" ")
print("Programa Finalizado")
