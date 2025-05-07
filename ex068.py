"""Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador Perder, Mostrando
o total de vitórias consecutivas que ele conquistou no final
do jogo."""
from random import randint
v = 0
while True:
    jogador = int(input("Digite um número: "))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("PAR OU ÍMPAR?[P/I]")).strip().upper()[0]
    print(f"Voce jogou {jogador} e o computador {computador}, total de {total}")
    if tipo == "P":
        if total % 2 == 0:
            print("você venceu!")
            v += 1
        else:
            print("Você perdeu!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Você venceu!")
            v += 1
        else:
            print("você perdeu!")
            break
    print("Vamos jogar novamente!")
print(f"GAME OVER!Você venceu {v} vezes.")





