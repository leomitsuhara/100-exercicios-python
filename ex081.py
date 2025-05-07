"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A)Quantos números foram digitados.
B)A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""
cont = 0
lista = []
while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    lista.sort(reverse=True)
    cont += 1
    if n == 5:
        print("O valor 5 foi digitado.")
    else:
        print("Não encontrei o número 5.")
    r = str(input("Quer digitar mais um número?[S/N]")).strip().upper()[0]
    if r in "N":
        break
print(f"Foram digitados {cont} números.")
print(f"Foram digitados os números {lista}")
