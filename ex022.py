""" Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minuscúlas.
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome."""

# Solicita ao usuário que digite o nome completo e remove espaços em branco no início e no fim
nome = str(input('Digite seu nome completo:')).strip()

# Converte todas as letras do nome para maiúsculas e imprime o resultado
print('Seu nome com todas as letras em MAIÚSCULO: {}'.format(nome.upper()))

# Converte todas as letras do nome para minúsculas e imprime o resultado
print('Seu nome com todas as letras em minúsculo: {}'.format(nome.lower()))

# Calcula o número total de letras no nome, desconsiderando os espaços em branco
# len(nome) calcula o comprimento total da string (incluindo espaços)
# nome.count(' ') conta o número de espaços em branco
print('Seu nome tem {} letras ao todo.'.format(len(nome)-nome.count(' ')))

# Encontra o índice da primeira ocorrência de um espaço em branco
# Isso indica o final do primeiro nome
# Se não houver espaços, find() retorna -1
print('O primeiro nome tem o total de {} letras.'.format(nome.find(' ')))