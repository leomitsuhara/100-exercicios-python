"""94. Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os
dicionários em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas
b) A média de idade do grupo.
c) Uma lista com todas as mulheres.
d) Uma lista com todas as pessoas com idade acima da média."""

galera = list()  # Lista para armazenar os dicionários de cada pessoa
pessoa = dict()  # Dicionário para armazenar os dados de cada pessoa temporariamente
soma = média = 0  # Variáveis para armazenar a soma das idades e a média

while True:  # Loop infinito para cadastrar múltiplas pessoas
    pessoa.clear()  # Limpa o dicionário antes de cada novo cadastro

    pessoa["nome"] = str(input("Nome: "))  # Solicita o nome da pessoa e armazena no dicionário

    while True:  # Loop para garantir que o usuário digite apenas 'M' ou 'F' para o sexo
        pessoa["sexo"] = str(input("Sexo: [M/F] ")).upper()[0]  # Pega apenas a primeira letra e converte para maiúscula
        if pessoa["sexo"] in "MF":  # Verifica se o sexo é válido
            break  # Sai do loop se for válido
        print("ERRO! Por favor, digite apenas M ou F.")  # Mensagem de erro em caso de entrada inválida

    pessoa["idade"] = int(input("Idade: "))  # Solicita e armazena a idade da pessoa
    soma += pessoa["idade"]  # Soma a idade para calcular a média depois

    galera.append(pessoa.copy())  # Adiciona uma cópia do dicionário à lista

    while True:  # Loop para garantir que o usuário digite apenas 'S' ou 'N' para continuar ou não
        resp = str(input("Quer continuar? [S/N] ")).upper()[0]  # Pega apenas a primeira letra e converte para maiúscula
        if resp in "SN":  # Verifica se a resposta é válida
            break  # Sai do loop se for válida
        print("ERRO! Responda apenas S ou N.")  # Mensagem de erro em caso de entrada inválida

    if resp == "N":  # Se o usuário optar por não continuar, sai do loop principal
        break

print("-=" * 30)  # Linha decorativa
print(f"Ao todo temos {len(galera)} pessoas cadastradas.")  # Exibe o número total de pessoas cadastradas

média = soma / len(galera)  # Calcula a média de idade
print(f"A média de idade é de {média:5.2f} anos.")  # Exibe a média de idade formatada com 2 casas decimais

print("As mulheres cadastradas foram ", end="")
for p in galera:  # Percorre a lista de pessoas cadastradas
    if p["sexo"] in "Ff":  # Verifica se a pessoa é do sexo feminino
        print(f"{p['nome']} ", end="")  # Exibe o nome das mulheres cadastradas
print()  # Quebra de linha

print(f"Lista de pessoas que estão acima da média: ")
for p in galera:  # Percorre novamente a lista de pessoas cadastradas
    if p["idade"] >= média:  # Verifica se a idade da pessoa é maior ou igual à média
        print("   ")  # Este print parece desnecessário e pode ser removido
    for k, v in p.items():  # Percorre os itens do dicionário (chave e valor)
        print(f"{k} = {v}; ", end="")  # Exibe os dados da pessoa
    print()  # Quebra de linha

print("<<< ENCERRADO >>>")  # Mensagem final

