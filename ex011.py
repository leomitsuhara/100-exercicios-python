""""Faça um programa que leia a largura e a altura de uma parede em metros, Calcule
 a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada
 litro de tinta, pinta uma área de 2m²"""
largura = float(input('Digite a largura:'))
altura = float(input('Digite a altura: '))
area = largura * altura
quantidade_tinta = area / 2
print('Sua área tem a dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(quantidade_tinta))