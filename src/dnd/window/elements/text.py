import pygame

def CreateText(stuff: str, pos, newLine=False):
    font = pygame.font.SysFont('', 50)
    text = font.render(stuff, True, (0, 255, 0))
    textRect = text.get_rect()
    if newLine:
        pos["x"] = 50
        pos["y"] += textRect.height + 5

    textRect.topleft = (pos["x"], pos["y"])

    pos["x"] += textRect.width + 12

    return [text, textRect]