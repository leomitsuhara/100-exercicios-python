"""112. Dentro do pacote utilidadesCev que criamos no desafio 111, temos
um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz
de funcionar como a função input(), mas com uma validação de dados para aceitar
apenas valores que sejam monetários."""

from ex112.utilidadesCEV import moeda
from ex112.utilidadesCEV import  dados
preço = dados.leiaDinheiro("Digite o preço: R$")
moeda.resumo(preço, 20, 12)