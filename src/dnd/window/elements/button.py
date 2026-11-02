import pygame
from pygame.rect import Rect

def createButton(surface:pygame.Surface,pos):
    rect = Rect(pos["x"],pos["y"],100,100)
    button = pygame.draw.rect(surface,(200,0,0),rect)
    return button