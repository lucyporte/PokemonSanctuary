import pygame

from utils import load_image, render_text


class TextBox():
    def __init__(self, screen):
        self.textbox_background = load_image("assets/images/menubox.png", 400, 100)
        self.screen = screen
        self.screen.blit(self.textbox_background, (0, 400))

    def set_text(self, text, line=1):
        """
        Set the text displayed in the text box
        """
        # Reset textbox each time
        self.screen.blit(self.textbox_background, (0, 400))

        if line == 1:
            x, y = 25, 410
        elif line == 2:
            x, y = 25, 425
        elif line == 3:
            x, y, = 25, 440
        elif line == 4:
            x, y, = 25, 455
        elif line == 5:
            x, y, = 25, 470

        self.screen.blit(render_text(text), (x, y))
        pygame.display.update()
