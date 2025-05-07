"""90. Faça um programa que leia nome e média de um aluno, guardando
também a situação em um dicionário. No final, mostre o conteúdo
da estrutura na tela."""

aluno = dict()  # Dicionário para armazenar os dados do aluno

# Solicita o nome do aluno
aluno["nome"] = str(input("Nome: "))

# Solicita a média do aluno e armazena no dicionário
aluno["média"] = float(input(f"Média de {aluno['nome']}: "))

# Determina a situação do aluno com base na média
if aluno["média"] >= 7:
    aluno["situação"] = "Aprovado"
elif 5 <= aluno["média"] < 7:
    aluno["situação"] = "Recuperação"
else:
    aluno["situação"] = "Reprovado"

print("-=" * 30)  # Linha decorativa

# Exibe os dados armazenados no dicionário
for k, v in aluno.items():
    print(f"  - {k} é igual a {v}")
