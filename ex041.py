"""A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 20 anos: Sênior
- Acima: MASTER"""

#Importando o datetime
from datetime import date

#Pegando o ano atual
ano_atual = date.today().year

ano_nascimento = int(input("Digite o ano de nascimento:"))
idade = ano_atual - ano_nascimento
if idade <= 9:
    print("MIRIM")
elif idade <= 14:
    print("INFANTIL")
elif idade <= 19:
    print("JUNIOR")
elif idade <= 20:
    print("SÊNIOR")
else:
    print("MASTER")
