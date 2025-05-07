def aumentar(valor = 0, taxa=0, formato=False):
    aumentar = valor +  (valor * 10 / 100)
    return aumentar if formato is False else moeda(aumentar)

def diminuir(valor = 0, taxa=0, formato=False):
    diminuir = valor - (valor * taxa / 100)
    return diminuir if formato is False else moeda(diminuir)

def dobro(valor = 0, formato=False):
    dobro = valor * 2
    return dobro if formato is False else moeda(dobro)

def metade(valor=0, formato=False):
    metade = valor / 2
    return metade if formato is False else moeda(metade)

def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',') #Troca os pontos por virgulas.