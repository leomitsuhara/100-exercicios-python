"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições
na lista."""
listanum = []
maior = 0
menor = 0
for c in range(0, 5): # contador que ai de 0 a 4.
    listanum.append(int(input(f"Digite um valor para a posição {c}:"))) #.append adiciona elementos, então vira uma variavel composta.
    if c == 0: #Se o contador começar com 0.
        maior = menor = listanum[c] #Todos são iguais / listanum na posição c
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print(f"Você digitou os valores {listanum}")
print(f"O maior valor digitado foi {maior} nas posições ",end="")
for i, v in enumerate(listanum):
    if v == maior:
        print(f"{i}...", end="")
print()
print(f"O menor valor digitado foi {menor} nas posições ", end="")
for i, v in enumerate(listanum): #para o indice e o valor em enumerate da listanum
    if v == menor:
        print(f"{i}...", end="")
print()
