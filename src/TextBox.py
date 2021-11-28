import pygame


class TextBox():
    def set_text(self, screen, text, line=1):
        """
        Set the text displayed in the text box
        """
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

        screen.blit(pygame.font.Font.render(pygame.font.Font("assets/fonts/smallest_pixel-7.ttf", 16), text, True, (0, 0, 0)), (x, y))
        pygame.display.update()
