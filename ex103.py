"""103. Faça um programa que tenha uma função chamada ficha(), que
receba dois parâmetros opcionais: o nome de um jogador e quantos gols
ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
algum dado não tenha sido informado corretamente."""
def ficha(jog='<DESCONHECIDO>', gol=0):#Parâmetros opcionais
    print(f"O jogador {jog} fez {gol} gol(s) no campeonato.")




n = str(input("Nome do jogador: "))
g = str(input("Número de gols: "))#Botei str no número de gols por que assim o programa não se importa de ficar em branco
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)