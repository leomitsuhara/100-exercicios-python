"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com
sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date  # Importa a biblioteca para trabalhar com datas

# Obtém o ano atual
ano_atual = date.today().year

# Entrada do ano de nascimento
ano_nascimento = int(input("Digite o ano de nascimento: "))

# Calcula a idade
idade = ano_atual - ano_nascimento

# Exibe as mensagens de acordo com a idade
print(f"Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.")

if idade < 18:
    anos_restantes = 18 - idade
    ano_alistamento = ano_atual + anos_restantes
    print(f"Você ainda não tem 18 anos. Faltam {anos_restantes} ano(s) para o alistamento.")
    print(f"Seu alistamento será em {ano_alistamento}.")
elif idade == 18:
    print("Você tem 18 anos. É hora de se alistar ao serviço militar!")
else:
    anos_atrasados = idade - 18
    ano_alistamento = ano_atual - anos_atrasados
    print(f"Você já deveria ter se alistado há {anos_atrasados} ano(s).")
    print(f"Seu alistamento foi em {ano_alistamento}.")
