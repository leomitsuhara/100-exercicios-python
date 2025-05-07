"""96. Faça um programa que tenha uma função chamada área()
que receba as dimensões de um terreno retangular (largura e
comprimento) e mostre a área do terreno."""
def área(largura, comprimento):
    dimensão = largura * comprimento
    print(f"A área do terreno {largura}x{comprimento} é de {dimensão}m²")

largura = float(input("Largura (m):"))
comprimento = float(input("Comprimento (m):"))
área(largura, comprimento)


