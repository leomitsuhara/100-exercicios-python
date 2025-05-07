"""Crie um programa que faça o computador jogar jokenpô com você."""

from  random import randint

itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogador = int(input('Qual é a sua jogada? '))
print(f"Computador jogou {itens[computador]}")
print(f"jogador jogou {itens[jogador]}")
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("JOGADOR PERDE")
    else:
        print("Opção invalida!")

if computador == 1: #computador joga PAPEL
    if jogador == 0:
        print("JOGADOR PERDE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("Opção invalida!")

if computador == 2: #computador joga TESOURA
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("JOGADOR PERDE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("Opção invalida!")