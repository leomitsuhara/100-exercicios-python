# Aula 22 - Módulos e pacotes
""""
- Modularização:
* Surgiu no início da década de 60;
* Sistemas ficando cada vez maiores;
* Foco: dividir um programa muito grande;
* Foco: aumentar a legibilidade;
* Foco: Facilitar a manutenção.

+ VANTAGENS:
* Organização do código;
* Facilita na manutenção;
* Ocultação de código detalhado;
* Reutilização em outros projetos.

"""
###Exemplo de modularização###

# Exemplo 1:
# Foi criado um arquivo uteis.py e a def fatorial, def dobro e def triplo foram postas lá.
# Foi exluído a pasta e criado pacotes.

from uteis import numeros
num = int(input("Digite um valor: "))
fat = numeros.fatorial(num) #Usar numeros. para chamar
print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {numeros.dobro(num)}")
print(f"O triplo de {num} é {numeros.triplo(num)}")

"""
- PACOTES:
* Uma pasta que contem  módulos;
* Serve para quando os modulos também ficarem muitos grande e ficar difícil a manutenção;
* Criar uma pasta com o nome 'Pacote uteis', assim podemos separar por assunto;
* Sempre que criamos uma pasta vem junto o __init__.py;
* Exemplo disso é que podemos separar por funções numéricas, strings, datas, cores, etc;
* comando 'from uteis import datas'.
"""
