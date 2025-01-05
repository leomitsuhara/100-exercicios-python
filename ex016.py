""""Crie um programa que leia um número real qualquer pelo teclado e mostre na
tela a sua porçõo inteira"""
""""EX: Digite um número:6.127
 O número 6.127 tem a aparte inteira 6"""
from math import trunc
numero = float(input('Digite um número:'))
print('O número {} tem a parte inteira {}'.format(numero, trunc(numero)))