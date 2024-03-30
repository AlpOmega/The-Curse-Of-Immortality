import pygame
import sys
import random
import json
import arabic_reshaper
import PyInstaller
from bidi.algorithm import get_display

class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def show(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    # static button make instance

class Captain:
    def __init__(self, image, x, y,  w=None, h=None, stamina=None, attack=None, defense=None, dodge=None):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        # self.hp = hp
        # self.max_hp = max_hp
        # self.w = w
        # self.h = h
    
    def player_sprite(self, screen):
        screen.blit(self.image, self.rect.topleft)
    
    # def draw(self, screen):
    #     raito = self.hp / self.max_hp
    #     pygame.draw.rect(screen, "red", (self.x, self.y, self.w, self.h))
    #     pygame.draw.rect(screen, "green", (self.x, self.y, self.w * ratio, self.h))




class Hunter(Captain):
    def __init__(self, image, x, y, health = None):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.health = health
    
    def hunter_sprite(self, screen):
        screen.blit(self.image, self.rect.topleft)
    
    def boss_health(self, health):
        health = 100