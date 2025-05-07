"""109. Modifique as funções que foram criadas no desafio 107 para que elas aceitem
um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado
pela função moeda(), desenvolvida no desafio 108. """
import moeda3
preço = float(input("Digite o preço: R$"))
print(f"A metade de {moeda3.moeda(preço)} é {moeda3.metade(preço, True)}")
print(f"O dobro de {moeda3.moeda(preço)} é {moeda3.dobro(preço, True)}")
print(f"Aumentando 10%, temos {moeda3.aumentar(preço, 10, True)}")
print(f"Reduzindo 13%, temos {moeda3.diminuir(preço, 13, True)}")