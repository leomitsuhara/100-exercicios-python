"""95. Aprimore o DESAFIO 093 para que ele funcione com vários
jogadores, incluindo um sistema de visualização de detalhes
do aproveitamento de cada jogador."""
time = list()  # Lista para armazenar os dados de todos os jogadores
jogador = dict()  # Dicionário para armazenar os dados de um jogador individualmente
partidas = list()  # Lista para armazenar a quantidade de gols em cada partida

while True:  # Loop principal para cadastro de jogadores
    jogador.clear()  # Limpa o dicionário antes de armazenar novos dados

    jogador["nome"] = str(input("Nome do Jogador: "))  # Solicita o nome do jogador

    # Solicita o número de partidas jogadas
    tot = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    partidas.clear()  # Limpa a lista de gols antes de armazenar novos dados

    # Loop para registrar os gols de cada partida
    for c in range(0, tot):
        partidas.append(int(input(f"   Quantos gols na partida {c + 1}? ")))

    # Armazena os dados no dicionário do jogador
    jogador["gols"] = partidas[:]  # Copia a lista de gols
    jogador["total"] = sum(partidas)  # Calcula o total de gols
    time.append(jogador.copy())  # Adiciona uma cópia do jogador à lista 'time'

    while True:  # Validação para continuar ou não
        resp = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resp in "SN":
            break
        print("ERRO! Responda apenas S ou N.")  # Mensagem de erro para resposta inválida

    if resp == "N":
        break  # Sai do loop principal

print("-=" * 30)  # Linha decorativa

# Exibição do cabeçalho da tabela
print("cod ", end="")
for i in jogador.keys():  # Pega os nomes das chaves do dicionário 'jogador'
    print(f"{i:<15} ", end="")
print()
print("-" * 40)

# Exibição dos dados de todos os jogadores cadastrados
for k, v in enumerate(time):  # Percorre a lista de jogadores
    print(f"{k:>3} ", end="")  # Exibe o índice (código do jogador)
    for d in v.values():  # Exibe os valores de cada chave do dicionário
        print(f"{str(d):<15}", end="")
    print()
print("-" * 40)

# Consulta de dados individuais de jogadores
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if busca == 999:
        break  # Sai do loop se o usuário quiser parar

    if busca >= len(time):  # Verifica se o código digitado é válido
        print(f"ERRO! Não existe jogador com código {busca}!")
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:")
        for i, g in enumerate(time[busca]["gols"]):
            print(f"   No jogo {i + 1} fez {g} gols.")
    print("-" * 40)

print("<<< VOLTE SEMPRE >>>")  # Mensagem de encerramento
