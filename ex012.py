import pygame

#inicializar o mixer
pygame.mixer.init()

#entrada, carregar o arquivo .mp3
pygame.mixer.music.load('audio.mp3') # Substir pelo nome do arquivo .mp3, que deveria estar na mesma página do código

#Reproduzir áduio
pygame.mixer.music.play()

#Mantém o programa rodando até o áudio terminar
while pygame.mixer.music.get_busy():
    continue