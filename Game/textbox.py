import pygame
class Text():
    def __init__(self):  
        pass

    def add_text(self, text, screen, font, line = "line1"):
        print(f"here is my line: {line}")
        if line == "line1": x, y = 25, 410
        elif line == "line2": x, y = 25, 425
        elif line == "line3": x, y, = 25, 440
        elif line == "line4": x, y, = 25, 455
        elif line == "line5": x, y, = 25, 470
        screen.blit(font.Font.render(font.Font("smallest_pixel-7.ttf", 16), text, True, (0, 0, 0)), (x, y))
        pygame.display.update()
