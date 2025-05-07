"""108. Adapte o código do desafio 107, criando uma função adicional chamada moeda()
que consiga mostrar os valores como um valor monetário formatado."""

import moeda2
preço = float(input("Digite o preço: R$"))
print(f"A metade de {moeda2.moeda(preço)} é {moeda2.moeda(moeda2.metade(preço))}")
print(f"O dobro de {moeda2.moeda(preço)} é {moeda2.moeda(moeda2.dobro(preço))}")
print(f"Aumentando 10%, temos {moeda2.moeda(moeda2.aumentar(preço))}")