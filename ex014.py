""""Escreva um programa que converta uma temperatura digitada em grau censius
para Grau Fahrenheit"""
c = int(input('Qual a temperatura?°C'))
fah = (c * 1.8) + 32
print('A nova temperatura em Fahrenheit será de {:.0f}°F'.format(fah))