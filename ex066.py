"""Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
 quando o usuário digitar o valor 999, que é a condição de parada. No final mostre quantos
 números foram digitados e qual foi a soma entre eles(desconsiderando aa flag)"""

n = soma = cont = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    soma += n
    cont += 1
print(f"Foram digitados {cont} números e a soma entre eles foi de {soma}")