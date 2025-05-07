# Aula 23 - Erros e exceções
"""
- Erros:
* primt(x)
+ Esse é um erro de sintaxe na qual o correto seria print(x);
+ Mas mesmo assim está errado por que não foi dito o que é o X.
"""
###Exemplos de erro####

#Exemplo 1:
x = 8 # Sempre devemos inicializar a variável se não é um erro semântico
print(x)

"""
- Exceções:
* n = int(input('Número: ')), nesse caso era só botar um valor numérico, mas se botarmos
um valor por extenso, como, 'oito', ele dá um erro.
"""
###Exemplos de exceções####

#Exemplo 1:
n = int(input("Número: "))
print(f"Você digitou o número {n}")

#OBS: Então nesse caso se digitarmos 'oito' vai dar erro na linha 1 'n = int(input("Número: "))' chamada ValueError, erro de valor.
# Então é chamado de exceção por que o código está correto, mas dependendo de como o usuário vai responder da um erro.

#Exemplo 2:
a = int(input('Númerador: '))
b = int(input('Denominador: '))
r = a / b
print(f'O resultado é {r}')

# No exemplo dois de cima também é uma exceção por que se botarmos '0' no denominador vai dar o erro ZeroDivisionError.

"""
- try:
   operação
- except:
   falhou
* Esses dois comandos acima significa 'tente alguma coisa ou uma exceção ocorrerá'.
- else:
   deu certo
- finally
   certo/falha 
* O finally vai ocorrer independente se deu certo ou errado.
* Tanto else como finally são opcionais.
* Podemos ter quantos 'except' nós quisermos, para cada tipo de erro, como, except TypeError:,
except ValueError:, except OSError:, e etc. 
"""

###Exemplos de try: except:###

#Exemplo 1:
try:
    a = int(input('Númerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro: # Vai me mostrar o erro sem comprometer no terminal.
    print(f'Problema encontrado foi {erro.__class__}') # vai aparecer o erro da classe
else:
    print(f'O resultado é {r}')
finally: #vai ocorrer mesmo se o código der errado
    print('Volte sempre! Muito obrigado!')

#Exemplo 2:
try:
    a = int(input('Númerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r}')
finally: #vai ocorrer mesmo se o código der errado
    print('Volte sempre! Muito obrigado!')