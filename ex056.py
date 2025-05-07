"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final
 do programa, mostre:
 - A média de idade do grupo.
 - Qual é o nome do homem mais velho.
 - Quantas mulheres têm menos de 20 anos."""

somaidadade = 0
médiaidade = 0
maioriadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range (1, 5):
    print(F"---- {p}ª PESSOA ----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidadade += idade
    if p == 1 and sexo in "Mm":
        maioriadehomem = idade
        nomevelho = nome
    if sexo  in "Mm" and idade > maioriadehomem:
        maioriadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
       totmulher20  += 1
médiaidade = somaidadade /4
print(f"A média de idade do grupo é de {médiaidade} anos")
print(f"O homem mais velho tem {maioriadehomem} anos e se chama {nomevelho}")
print(f"Ao todo são {totmulher20} mulheres com menos de 20 anos")