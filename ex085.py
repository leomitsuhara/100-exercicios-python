"""Crie um programa onde o usuário possa digitar sete valores
numéricos e cadastre-os em uma lista única que mantenha separados
os valores pares e ímpares. No final mostre os valores pares e ímpares
em ordem crescente. """

principal = [[],[]]
for v in range(0, 7):
    valor = int(input("Digite um valor: "))

    if valor % 2 == 0:
        principal[0].append(valor)
    else:
        principal[1].append(valor)

print(f"Números pares: {sorted(principal[0])}")
print(f"Números ímpares: {sorted(principal[1])}")
