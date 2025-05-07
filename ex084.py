"""Faça um programa que leia o nome e peso de várias pessoas,
guardando tudo em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com pessoas mais leves."""
temporária = []
principal = []
maior = menor = 0
while True:
    temporária.append(str(input("Nome: ")))
    temporária.append(float(input("Peso: ")))
    if len(principal) == 0:
        maior = menor = temporária[1]
    else:
        if temporária[1] > maior:
            maior = temporária[1]
        if temporária[1] < menor:
            menor = temporária[1]
    principal.append(temporária[:])
    temporária.clear()
    resp = str(input("Deseja continuar?[S/N]")).strip().upper()[0]
    if resp in "N":
        break
print(f"Ao todo, você cadastrou {len(principal)} pessoas. ")
print(f"O maior peso foi de {maior}kg. Peso de ", end="")

for p in principal:
    if p[1] == maior:
        print(f"{p[0]}", end="")
print()
print(f"O menor peso foi de {menor}kg. Peso de ", end="")
for p in principal:
    if p[1] == menor:
        print(f"{p[0]} ", end="")
print()