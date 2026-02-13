#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from sys import exit

from src.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(800,600))
    @staticmethod
    def run(self):
        clock = pygame.time.Clock()
        while True:
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
