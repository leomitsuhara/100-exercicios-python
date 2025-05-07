def aumentar(valor = 0):
    aumentar = valor +  (valor * 10 / 100)
    return aumentar

def diminuir(valor = 0):
    diminuir = valor - (valor * 10 / 100)
    return diminuir

def dobro(valor = 0):
    dobro = valor * 2
    return dobro

def metade(valor=0):
    metade = valor / 2
    return metade

def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',') #Troca os pontos por virgulas.