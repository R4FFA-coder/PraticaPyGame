import pygame
from pygame.locals import *
from sys import exit

pygame.init()

width = 1280
height = 720

window = pygame.display.set_mode(size=(width, height))

while True:
    # # Check for all events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()  # Close Window
            exit()  # Quit Pygame
    pygame.display.update()