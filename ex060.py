"""Faça um programa que leia um número qualquer e mostre o seu fatorial
ex: 5!=5x4x3x2x1=120"""
n = int(input("Digite um número: "))
c = n
f = 1
while c > 0:
    print(f"{c}", end='')
    print(" x " if c > 1 else " = ", end="")
    f = f * c
    c= c - 1
print(f"{f}")
