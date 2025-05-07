"""107. Crie um módulo moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas
funções."""

from moeda import metade
from  moeda import dobro
from moeda import aumentar
from moeda import diminuir
preço = float(input("Digite o preço: R$"))
metade(preço)
dobro(preço)
aumentar(preço)
diminuir(preço)





