"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros"""

produto = float(input("Quanto custa o seu produto: R$"))
print("Selecione a forma de pagamento:")
print("1 - À VISTA/CHEQUE")
print("2 - À VISTA NO CARTÃO")
print("3 - EM ATÉ 2x NO CARTÃO")
print("4 - EM 3x OU MAIS NO CARTÃO")
opção = int(input("Digite a opção correspondente: "))
dinheiro = produto - (10/100)
vista = produto - (5/100)
parcela2 = produto
parcela3 = produto + (20/100)

if opção == 1:
    print(f"À VISTA/CHEQUE o valor do produto fica em R${dinheiro:.2f}")
elif opção == 2:
    print(f"À VISTA NO CARTÃO o valor do produto fica em R${vista:.2f}")
elif opção == 3:
    print(f"EM ATÉ 2x NO CARTÃO o valor do produto fica em R${parcela2:.2f}")
elif opção == 4:
    print(f"EM 3x OU MAIS NO CARTÃO o valor do produto fica em R${parcela3:.2f}")
else:
    print("O número não corresponde as alternativas.")


