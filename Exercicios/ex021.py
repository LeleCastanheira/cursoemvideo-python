# Faça um programa em Python que abra e reproduza um arquivo mp3
'''import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
Esse método do professor não funcionou'''

from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input('Está ouvindo agora?')