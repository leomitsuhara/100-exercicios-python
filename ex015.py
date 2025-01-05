"""Escreva um programa que pergunte a quantidade de Km percorridos por um carro
alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
 sabendo que o carro custa R$60 por dia e R$0,15 por km rodado"""
dias = int(input('Quantos dias você alugou?'))
diasAlugados = dias * 60
km = float(input("Quantos km você percorreu?"))
kmPercorrido = km * 0.15
print("Você vai pagar o valor de R${:.2f}".format(diasAlugados + kmPercorrido))
