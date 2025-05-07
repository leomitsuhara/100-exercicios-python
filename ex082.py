"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores
ímpares digitados, respectivamente.
Ao final, mostre o conteúdo dos três listas geradas."""
lista_completa = []
lista_par = []
lista_impar = []
while True:
    número = int(input("Digite um número: "))
    lista_completa.append(número)
    if número % 2 == 0:
        lista_par.append(número)
    else:
        lista_impar.append(número)
    r = str(input("Deseja adicionar outro número a lista?[S/N]")).upper().strip()[0]
    if r in "N":
        break
print(f"A lista completa é {lista_completa}")
print(f"A lista de pares é {lista_par}")
print(f"A lista de ímpares é {lista_impar}")