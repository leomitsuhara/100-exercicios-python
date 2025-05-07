"""Crie um programa onde o usuário possa digitar vários
valores numéricos e cadastre-os em uma lista. Caso o número
já exista lá dentro, ele não será adicionado. No final, serão
exibidos todos os valores únicos digitados, em ordem crescente."""
lista = []

while True:
    valor = int(input("Digite um valor:"))
    if valor not in lista:
        lista.append(valor)
        print("Valor adicionado")
    else:
        print("Valor repetido.")
    r = str(input(f"Quer continuar? [S/N]")).upper().strip()[0]
    if r == "N":
        break
lista.sort()
print(f"Foram adicionados os valores {lista}")


