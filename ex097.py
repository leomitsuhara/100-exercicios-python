"""97. Faça um programa que tenha a função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem
com tamanho adaptável.
ex:
escreva('Olá, mundo!')
Saída:
~~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~~"""

def escreva(text):
    print("~" * len(text))
    print(text)
    print("~" * len(text))



escreva("Curso de video em python")