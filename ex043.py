"""Desenvolva uma lógica que leia o peso e uma altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- Acima de 40: Obesidade mórbida"""

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print(f"Seu IMC deu {imc:.2f}, você está ABAIXO DO PESO!")
elif 18.5 < imc <= 25:
    print(f"Seu IMC deu {imc:.2f}, você está com o PESO IDEAL!")
elif 25 < imc <= 30:
    print(f"Seu IMC deu {imc:.2f}, você está com SOBREPESO!")
elif 30 < imc <= 40:
    print(f"Seu imc deu {imc:.2f}, você está com OBESIDADE!")
else:
    print(f"Seu IMC deu {imc:.2f}, você está com OBESIDADE MÓRBIDA!")