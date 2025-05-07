"""114. Crie um código em python que teste se o site Pudim está acessível
pelo computador usado."""
import urllib
import urllib.request
import urllib.error


try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')