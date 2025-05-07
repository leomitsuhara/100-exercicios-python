"""Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
 só que agora utilizando um laço for."""

tabuada = int(input("Digite um número inteiro: "))
for n in range(1, 11):
    print(tabuada * n)