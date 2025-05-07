"""100. Faça um programa que tenha uma lista chamada números e
duas funções chamadas sorteio() e somaPar(). A primeira função
vai sortear 5 números e vai colocá-los dentro da lista e a segunda
função vai mostrar a soma entre todos os valores PARES
sorteados pela função anterior."""
from random import randint
def sorteia(lista):
    print(f"Sorteando 5 valores da lista: ", end=" ")
    for cont in range (0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f"{n}", end=" ")
def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"\nSomando os valores pares de {lista}, temos {soma}")


números = list()
sorteia(números)
somaPar(números)













