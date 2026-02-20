#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from pygame.locals import *

from src.Const import *


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBG.jpg')  # Variavel que recebe o metodo com o caminho da imagem a ser carregada
        self.rect = self.surf.get_rect(left=0, top=0)  # Precisamos desenhar um retangulo para representar o espaco em que a imagem sera usada


    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/RuasdeSP.wav') # Metodo para carregar musica
        pygame.mixer_music.play(-1) # metodo que coloca a musica em loop
        while True:
            # Detalhe, pensando na lógica de camadas, o texto precisa ser criado depois da imagem, senao a imagem de fundo sobreescreve o que tinha sido criado
            self.window.blit(source=self.surf, dest=self.rect)  # Carrega a imagem e joga no retagunlo que desenhamos
            self.menu_text(80, 'JOVI', COLOR_WHITE, (WIN_WIDTH / 2 - 30, 127)) # Inicializo o metodo para criar o texto
            self.menu_text(55, 'WAR', COLOR_WHITE, (WIN_WIDTH / 2 + 60, 164)) # Inicializo o metodo para criar o texto

            for i in range(len(MENU_OPTION)): # for para iterar com o tamanho da tupla, com um metodo text com um calculo para separar os prints
                if i == menu_option:
                    self.menu_text(30, MENU_OPTION[i], COLOR_YELLOW, (WIN_WIDTH / 2, 265 + 30 * i))
                else:
                    self.menu_text(30, MENU_OPTION[i], COLOR_BLUE, (WIN_WIDTH / 2, 265 + 30 * i))
            pygame.display.flip()  # Atualiza a imagem para mostrar na janela

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()  # Close Window
                    exit()  # Quit Pygame
                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == K_RETURN:
                        return MENU_OPTION[menu_option]




    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        """Metodo que cria texto para o menu
            A Logica é a mesma de criar uma imagem de fundo, um texto sera como uma imagem projetada em um retangulo que criaremos
        """
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size) # padroniza uma fonte e o tamanho
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha() # Renderiza o texto
        text_rect: Rect = text_surf.get_rect(center=text_center_pos) # Desenha um retangulo que será a área em que o texto ocupará
        self.window.blit(source=text_surf, dest=text_rect) # carrega o texto e imprime na area do retangulo