"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
 em uma tupla. No final, mostre:
 a) Quantas vezes apareceu o valor 9.
 b) Em que posição foi digitado o primeiro valor 3.
 c) Quais foram os números pares."""
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))
n4 = int(input("Quarto número: "))
números = n1, n2, n3, n4
print(f"O número 9 apareceu {números.count(9)} Vezes.")
if 3 in números:
    print(f"O primeiro 3 aparece na posição {números.index(3)+1}")
else:
    print("O número 3 não foi digitado.")
print(f"Os números pares digitados foram ", end="")
for n in números:
    if n % 2 == 0:
        print(n, end="")