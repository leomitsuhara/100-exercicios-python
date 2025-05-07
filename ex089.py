"""Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta. No final, mostre um
boletim contendo a média de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente."""

lista = []

while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1:"))
    nota2 = float(input("Nota 2:"))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    r = str(input("Deseja continuar?[S/N]")).upper().strip()[0]
    if r in "N":
        break
print("-=" * 30)
print(f"{"No.":<4}{"NOME":<10}{"MÉDIA":>8}")
print("-=" * 26)
for i, a in enumerate(lista):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
while True:
    print("-" * 35)
    notas_aluno = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if notas_aluno == 999:
        print("FINALIZANDO...")
        break
    if notas_aluno <= len(lista) -1:
        print(f"Notas de {lista[notas_aluno][0]} são {lista[notas_aluno][1]}")
print("<<< VOLTE SEMPRE >>>")



