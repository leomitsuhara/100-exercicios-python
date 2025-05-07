"""Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar. No final, mostre:

a) Quantas pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos."""

resp = "N"
cont = mulher = homem =  0

while True:
    idade = int(input("Qual a sua idade: "))
    sexo = str(input("Qual o seu sexo [M/F]:")).strip().upper()[0]
    if idade > 18:
        cont += 1
    if sexo == "M":
        homem += 1
    if sexo == "F" and idade <= 20:
        mulher += 1
    resp = str(input("Quer cadastrar outra pessoa?[S/N]")).strip().upper()[0]
    if resp == "N":
            break

print(f"Foram cadastradas {cont} pessoa com mais de 18 anos.")
print(f"Foram cadastrados {homem} homens.")
print(f"Tem {mulher} mulher com menos de 20 anos.")