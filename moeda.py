def aumentar(valor):
    aumentar = valor +  (valor * 10 / 100)
    print(f"Aumentando 10%, temos R${aumentar:.2f}")

def diminuir(valor):
    diminuir = valor - (valor * 10 / 100)
    print(f"Diminuindo 10%, temos {diminuir:.2f}")

def dobro(valor):
    dobro = valor * 2
    print(f"O dobro de R${valor:.2f} é R${dobro:.2f}")

def metade(valor):
    meio = valor / 2
    print(f"A metade de R${valor:.2f} é R${meio:.2f}")