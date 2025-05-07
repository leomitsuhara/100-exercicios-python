"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal"""


# Programa para conversão de bases numéricas

# Entrada do número inteiro
numero = int(input("Digite um número inteiro: "))

# Opções de conversão
print("Escolha uma das bases para conversão:")
print("1 - Converter para BINÁRIO")
print("2 - Converter para OCTAL")
print("3 - Converter para HEXADECIMAL")

# Lendo a escolha do usuário
opcao = int(input("Sua opção: "))

# Realiza a conversão com base na escolha
def converter(numero, opcao):
    if opcao == 1:
        return bin(numero)[2:]  # Remove o prefixo '0b'
    elif opcao == 2:
        return oct(numero)[2:]  # Remove o prefixo '0o'
    elif opcao == 3:
        return hex(numero)[2:].upper()  # Remove o prefixo '0x' e deixa em maiúsculo
    else:
        return None

resultado = converter(numero, opcao)

if resultado is not None:
    if opcao == 1:
        base = "BINÁRIO"
    elif opcao == 2:
        base = "OCTAL"
    else:
        base = "HEXADECIMAL"

    print(f"O número {numero} convertido para {base} é: {resultado}")
else:
    print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
