"""Escreva um programa que leia um número n inteiro qualquer
e mostre na tela os n primeiros elementos de uma sequência
de Fibonacci
ex: 0 > 1 > 1 > 2 > 3 > 5 > 8 """

n = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1
print(f"{t1} → {t2}", end="")
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f"→ {t3}", end="")
    t1 = t2
    t2 = t3
    cont += 1
print("→ FIM")