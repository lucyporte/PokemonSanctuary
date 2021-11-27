import pygame
class Text():
    def __init__(self):
        """self.line1 = None
        self.line2 = None
        self.line3 = None """   
        pass

    def add_text(self, text, screen, font, line = "line1"):
        print(f"here is my line: {line}")
        if line == "line1": x, y = 25, 410
        elif line == "line2": x, y = 25, 425
        elif line == "line3": x, y, = 25, 440
        screen.blit(font.Font.render(font.Font("smallest_pixel-7.ttf", 16), text, True, (0, 0, 0)), (x, y))
        pygame.display.update()

    """def add_line1(self, text, screen, font, x = 25, y = 410):
        print(self.line1)
        if text != self.line1: 
            input("pass if statement")
            screen.blit(font.Font.render(font.Font("smallest_pixel-7.ttf", 16), text, True, (0, 0, 0)), (x, y))
            pygame.display.update()
            self.line1 = text

    def add_line2(self, text, screen, font, x = 25, y = 425):
        if text != self.line2: 
            screen.blit(font.Font.render(font.Font("smallest_pixel-7.ttf", 16), text, True, (0, 0, 0)), (x, y))
            pygame.display.update()
            self.line2 = text

    def add_line3(self, text, screen, font, x = 25, y = 440):
        if text != self.line3:
            screen.blit(font.Font.render(font.Font("smallest_pixel-7.ttf", 16), text, True, (0, 0, 0)), (x, y))
            pygame.display.update()
            self.line3 = text"""