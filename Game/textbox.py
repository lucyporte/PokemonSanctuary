import pygame
class Text():
    def __init__(self):
        pass    

    def add_text(self, text, screen, font):
        screen.blit(font.Font.render(font.Font("smallest_pixel-7.ttf", 16), text, True, (0, 0, 0)), (25, 410))
        pygame.display.update()