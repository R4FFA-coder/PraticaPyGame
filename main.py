import pygame
from pygame.locals import *
from sys import exit

pygame.init()
clock = pygame.time.Clock()

width = 1280
height = 720

window = pygame.display.set_mode(size=(width, height))

while True:
    # # Check for all events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()  # Close Window
            exit()  # Quit Pygame
        pygame.draw.rect(window, (0, 101, 255), (100, 360, 40, 50))
        pygame.draw.circle(window, (255, 0, 0), (640, 200), 100)
        pygame.draw.line(window, (255, 255, 255), (540, 200), (120, 360), 5)
    pygame.display.update()
    clock.tick(60)
