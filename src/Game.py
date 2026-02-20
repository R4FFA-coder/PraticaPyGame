#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from sys import exit
from src.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from src.Level import Level
from src.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT)) # Variavel window com o metodo que abre uma janela com tamanho determinado com parametro

    def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(24)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1],MENU_OPTION[2]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()

            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                exit()
            else:
                pass