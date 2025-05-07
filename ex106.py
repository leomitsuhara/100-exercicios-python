"""106. Faça um mini-sistema que utilize Interactive Help do Python. O usuário vai digitar
 o comando e o manuel vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa
 se encerrará.
 OBS: use cores."""
from time import sleep

# Definição das cores ANSI
c = ('\033[m',        # 0 - sem cores (padrão)
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2 - verde
     '\033[0;30;43m', # 3 - amarelo
     '\033[0;30;44m', # 4 - azul
     '\033[0;30;45m', # 5 - roxo
     '\033[7;97m')    # 6 - branco com fundo escuro (melhor legibilidade)

def ajuda(com):
    """Exibe o manual de ajuda do Python para um determinado comando."""
    título(f"Acessando o manual do comando '{com}'", 4)
    print(c[6], end='')  # Define a cor branca para melhor visibilidade
    help(com)
    print(c[0], end='')  # Restaura a cor padrão do terminal
    sleep(1)

def título(msg, cor=0):
    """Exibe um título formatado com uma cor específica."""
    tam = len(msg) + 4
    print(c[cor], end='')
    print("~" * tam)
    print(f"  {msg}  ")
    print("~" * tam)
    print(c[0], end='')
    sleep(1)

# Programa principal
while True:
    título("SISTEMA DE AJUDA PYHELP", 2)
    comando = input("Função ou biblioteca > ").strip()
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

título("ATÉ LOGO", 1)

