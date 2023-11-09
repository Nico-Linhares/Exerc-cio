'Faça um programa que abra e reproduza uma musica em mp3'

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex008.mp3')
pygame.mixer.music.play()
pygame.event.wait()


