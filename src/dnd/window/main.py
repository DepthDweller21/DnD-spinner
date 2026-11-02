# Example file showing a circle moving on screen
from timeit import repeat
import pygame
from .elements.text import *
from .elements.button import *
from ..engine.main import start

# pygame setup
def main():

    pygame.font.init()
    pygame.font.get_init()

    display_surface = pygame.display.set_mode((1080, 720))

    pygame.display.set_caption('DnD')

    rolls=start()

    textElements = []
    pos:dict[str,int] = {"x":50,"y":50}
    for element in rolls:
        textElements.append(CreateText(f"{element['category']}: {element['tag']}",pos,True))
    
    pos["x"] = 50
    pos["y"] = 500
    while True:

        display_surface.fill((50,50,50))
        createButton(display_surface,pos)   

        for x in textElements:
            display_surface.blit(x[0],x[1])

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
            
                pygame.quit()
                quit()
            pygame.display.update()