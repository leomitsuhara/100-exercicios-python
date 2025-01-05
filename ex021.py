"""Faça um programa em python que abra e reproduza um audio de um arquivo mp3"""
import pygame

# Inicializa o mixer do pygame
pygame.mixer.init()

# Solicita ao usuário o nome do arquivo de música
arquivo = input("Digite o caminho da música (ex: musica.mp3): ")

# Tenta carregar e tocar o arquivo
try:
    pygame.mixer.music.load(arquivo)
    pygame.mixer.music.play()

    print("Reproduzindo música... Pressione 'Enter' para parar.")
    input()  # Aguarda o usuário pressionar Enter para parar
    pygame.mixer.music.stop()

except Exception as e:
    print(f"Erro ao tentar reproduzir a música: {e}")
