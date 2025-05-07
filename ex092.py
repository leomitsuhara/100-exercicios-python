"""92. Crie um programa que leia nome, ano de nascimento e carteira
de trabalho e cadastre-os (com idade) em um dicionário se por
acaso a CTPS dor diferente de ZERO, o dicionário receberá também
 o ano de contratação e o salário. Calcule e acrescente, além
 da idade, com quantos anos a pessoa vai se aposentar."""
from datetime import datetime  # Importa a biblioteca para trabalhar com datas

dados = dict()  # Dicionário para armazenar as informações da pessoa

# Solicita o nome da pessoa
dados["nome"] = str(input("Nome: "))

# Solicita o ano de nascimento e calcula a idade
nasc = int(input("Ano de Nascimento: "))
dados["idade"] = datetime.now().year - nasc  # Obtém o ano atual e calcula a idade

# Solicita o número da Carteira de Trabalho (CTPS)
dados["CTPS"] = int(input("Carteira de Trabalho (0 não tem): "))

# Se a pessoa tiver carteira de trabalho, solicita mais informações
if dados["CTPS"] != 0:
    dados["contratação"] = int(input("Ano de Contratação: "))
    dados["salário"] = float(input("Salário: R$"))

    # Calcula a idade de aposentadoria considerando 35 anos de trabalho
    dados["aposentadoria"] = dados["idade"] + (dados["contratação"] + 35) - datetime.now().year

print("-=" * 30)  # Linha decorativa

# Exibe os dados armazenados no dicionário
for k, v in dados.items():
    print(f" - {k} tem o valor {v}")  # Corrigido erro de sintaxe na última linha
