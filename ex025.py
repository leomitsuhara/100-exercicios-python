""""Crie um progtama que leia o nome de uma pessoa e diga se ela tem "Silva"
no nome."""

nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem silva? {}'.format('silva' in nome.lower()))