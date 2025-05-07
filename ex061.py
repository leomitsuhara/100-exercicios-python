"""Refaça o DESAFIO 051, lendo o primeiro termo e a razão
de uma PA, mostrando os 10 primeiros termos da progressão usando
a estrutura while"""

primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
termo = primeiro
cont = 1

while cont <= 10:
    print(termo)
    termo = termo + razão
    cont  += 1
print("FIM")
