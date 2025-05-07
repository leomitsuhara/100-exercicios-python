"""Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar. No final, mostre:

a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$ 1000.
c) Qual é o nome do produto mais barato."""
total = caro = cont = menor =  0
barato = " "
while True:
    produto = str(input("Qual produto você quer cadastrar?"))
    valor = float(input("Qual o valor do produto?R$ "))
    cont += 1
    total += valor
    if cont == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto
    if valor >= 1000:
        caro += 1
    pergunta = str(input("Deseja continuar?[S/N]")).strip().upper()
    if pergunta == "N":
        break
print(f"O total da compra deu {total}, {caro} produtos custam mais de R$ 1000 e o produto mais barato foi a {barato}")

