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

def resumo(preço=0, taxaA=10, taxaR=5):
    print('-' * 30)
    print("RESUMO DO VALOR".center(30))
    print('-' * 30)
    print(f"Preço analisado: \t{moeda(preço)}")
    print(f"Dobro do preço: \t{dobro(preço, True)}")
    print(f"Metade do preço: \t{metade(preço, True)}")
    print(f"Com {taxaA}% de aumento: {aumentar(preço, taxaA, True)}")
    print(f"Com {taxaR}% de redução: {diminuir(preço, taxaR, True)}")
    print("-" * 30)