"""" Faça um algoritmo que leia o preço de um produto e mostre seu novo preço
com 5% de desconto."""
preco = float(input('Digite o preço: R$ '))
novoPreco= preco - (preco * 5/100)
print('Com o desconto de 5% o valor final será de R${}'.format(novoPreco))