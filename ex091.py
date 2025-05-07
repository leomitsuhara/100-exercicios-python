"""91. Crie um programa onde 4 jogadores joguem um dado e tenham
resultados aleatórios. Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem, sabendo que o vencedor
tirou o maior número no dado."""
# Importação das bibliotecas necessárias
from random import randint  # Para gerar números aleatórios entre 1 e 6 (simulando um dado)
from operator import itemgetter  # Para ordenar os valores de um dicionário com base em um item específico

# Criando um dicionário chamado "jogadores" e atribuindo um número aleatório (1 a 6) para cada jogador
jogadores = {
    "Jogador 1": randint(1, 6),
    "Jogador 2": randint(1, 6),
    "Jogador 3": randint(1, 6),
    "Jogador 4": randint(1, 6)
}
# Criando uma variável para armazenar o ranking (inicialmente vazia)
ranking = ()
# Exibindo os valores sorteados de cada jogador
print("Valores sorteados:")
for k, v in jogadores.items():
    print(f"{k} tirou {v} no dado.")  # Mostra o nome do jogador e o número que ele tirou
# Ordenando os jogadores com base no valor do dado (do maior para o menor)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
# Exibindo o ranking dos jogadores após a ordenação
for i, v in enumerate(ranking):
    print(f"{i+1}° lugar: {v[0]} com {v[1]} no dado.")  # Exibe a posição, o nome do jogador e o valor do dado
