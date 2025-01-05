""""Crie um programa que leia quanto dinheiro uma  pessoa tem na carteira  e mostre
quantos dólares ela pode comprar.
Considere US$ 1,00 = R$ 3,27"""
numero = float(input('Quanto você tem carteira? '))
print('Segundo você tem na carteira R${}, você pode comprar US${:.2f}'.format(numero, numero / 3.27))