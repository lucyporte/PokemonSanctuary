import pygame


def load_image(filename, x_cord, y_cord):
    """
    Loads and scales a Pygame image
    """
    image = pygame.image.load(filename).convert()
    image.convert_alpha()
    image.set_colorkey((0, 0, 0))
    return pygame.transform.scale(image, (x_cord, y_cord))
