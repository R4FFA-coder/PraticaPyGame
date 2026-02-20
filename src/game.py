#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from sys import exit
from src.Const import WIN_WIDTH, WIN_HEIGHT
from src.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT)) # Variavel window com o metodo que abre uma janela com tamanho determinado com parametro

    def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(24)
            menu = Menu(self.window)
            menu.run()
            pass

            # # Check for all events
            # for event in pygame.event.get():
            #     if event.type == QUIT:
            #         pygame.quit()  # Close Window
            #         exit()  # Quit Pygame
            # pygame.display.update()
            # clock.tick(60)
