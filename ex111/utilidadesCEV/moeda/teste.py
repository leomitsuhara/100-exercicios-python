"""111. Crie um pacote chamado utilidadesCev que tenha módulos internos
chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro
pacote e mantenha tudo funcionando."""

from ex111.utilidadesCEV import moeda
from ex111.utilidadesCEV import  dados
preço = float(input("Digite o preço: R$"))
moeda.resumo(preço, 20, 12)