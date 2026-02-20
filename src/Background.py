#!/usr/bin/python
# -*- coding: utf-8 -*-
from src.Const import WIN_WIDTH, ENTITY_SPEED
from src.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, postition: tuple):
        super().__init__(name, postition)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <=0:
            self.rect.left = WIN_WIDTH
