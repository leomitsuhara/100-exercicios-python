"""93. Crie um programa que gerencie o aproveitamento de um jogador
de futebol. O programa vai ler o nome do jogador e quantas partidas
ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo
o total de gols feitos durante o campeonato."""

jogador = dict()  # Dicionário para armazenar os dados do jogador
partidas = list()  # Lista para armazenar a quantidade de gols em cada partida

# Solicita o nome do jogador e armazena no dicionário
jogador["nome"] = str(input("Nome do Jogador: "))

# Solicita o número total de partidas jogadas
tot = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

# Loop para registrar os gols de cada partida
for c in range(0, tot):
    partidas.append(int(input(f"Quantos gols na partida {c+1}? ")))

# Armazena a lista de gols dentro do dicionário
jogador["gols"] = partidas[:]

# Calcula o total de gols e armazena no dicionário
jogador["total"] = sum(partidas)

# Exibe o desempenho do jogador em cada partida
for i, v in enumerate(jogador["gols"]):
    print(f"   => Na partida {i+1}, o jogador {jogador['nome']} fez {v} gols.")

# Exibe o total de gols marcados pelo jogador
print(f"Foi um total de {jogador['total']} gols.")
