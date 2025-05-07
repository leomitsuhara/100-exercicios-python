"""Crie uma tupla com os 20 primeiros colocados da tabela
do campeonato brasileiro de futebol, na ordem de colocação.
Depois mostre:
a) Apenas os 5 primeiros colocados.
b) Os últimos 4 colocados da tabela
c) Uma lista com os times em ordem alfabética.
d) Em que posição na tabela está o time da chapecoence"""


colocação = ("Santos", "Mirassol", "Sport", "Ceará", "Novorizontino", "Goiás", "Operário-PR",
            "América-MG", "Vila Nova", "Avaí", "Amazonas", "Curitiba", "Paysandu", "Botafogo-SP",
             "Chapecoense", "CRB", "Ponte Preta", "Ituano", "Brusque", "Guarani")
print(f"Os 5 primeiros são {colocação[:5]}")
print(f"Os quatro últimos são {colocação[16:20]}")
print(f"Os times em ordem alfabética {sorted(colocação)}")
print(f"O Chapecoence está na posição {colocação.index("Chapecoense")+1}")
