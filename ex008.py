""""Escreva um programa que leia um valor em metros e o exiba convertido em centímetros
 e milímetros"""
n = float(input('Digite o valor em metros: '))
print('Kilometros: {}km'.format(n / 1000))
print('Hectometros: {}hm'.format(n / 100))
print('Decametros: {}dam'.format(n / 10))
print('Decímetros: {}dm'.format(n / 10))
print('Centímetros: {}cm'.format(n / 1000 ))
print('Milímetros: {}mm'.format(n / 10000))
