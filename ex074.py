"""Crie um programa que vai girar cinco números aleatórios
e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique
o menor e o maior valor que estão na tupla."""
from random import randint
números = (randint(1,10),randint(1,10),randint(1,10),
           randint(1,10),randint(1,10))
print(f"Os números gerados foram {números}")
print(f"O maior número foi {max(números)} e o menor foi {min(números)}")