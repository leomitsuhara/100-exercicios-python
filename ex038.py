"""Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma
mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais."""
print("Digite dois valores: ")
valor_1 = int(input("Primeiro valor: "))
valor_2 = int(input("Segundo valor: "))

if valor_1 > valor_2:
    print("O primeiro valor é maior que o segundo valor.")
elif valor_2  > valor_1:
    print("O segundo valor é maior que o primeiro valor.")
else:
    print("Não existe valor maior, os dois são iguais.")