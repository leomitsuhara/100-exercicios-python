"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um
 dos digitos separados.
 EX: Digite um número: 1834
 Unidade: 4 dezena: 3 centena: 8 milhar: 1"""

# Este programa decompõe um número inteiro de até quatro dígitos em suas unidades, dezenas, centenas e milhares.

num = int(input('Informe um número: '))  # Solicita ao usuário um número inteiro e o armazena na variável 'num'

# Calcula os algarismos de cada posição:
u = num // 1 % 10  # Algarismo das unidades
d = num // 10 % 10  # Algarismo das dezenas
c = num // 100 % 10  # Algarismo das centenas
m = num // 1000 % 10  # Algarismo dos milhares

# Imprime os resultados na tela de forma organizada
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))