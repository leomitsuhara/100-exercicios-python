"""104. Crie um programa que tenha a função leiaInt(), que vai funcionar de
uma forma semelhante à função input() do python, só que fazendo a validação
para aceitar apenas um valor numérico.
EX:
n = leiaINT('Digite um n')"""
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            if ok:
                break
        return valor


n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")