import pygame
from pygame.locals import *
from random import randint


class Pokemon(pygame.sprite.Sprite):
    """
    Spawn a Pokemon
    """

    def __init__(self, obj):
        # Call superclass constructor
        pygame.sprite.Sprite.__init__(self)

        # Set X and Y velocities for Pokemon movement
        self.velocity_x = 0
        self.velocity_y = 0

        # Store Pokemon data
        self.data = obj

        # Set Pokemon health status
        self.hp = 20
        self.max_hp = 20

        # Set movement animation frames
        self.frame = 0

        # Load Pokemon textures
        self.images = [0]*4
        ALPHA = (0, 0, 0)
        for i, sprite in enumerate([obj.get_down_walk_sprite(), obj.get_left_walk_sprite(), obj.get_right_walk_sprite(), obj.get_right_walk_sprite()]):
            img = pygame.image.load(sprite.get_frame_1().get_path()).convert()
            img.convert_alpha()     # optimise
            img.set_colorkey(ALPHA)
            self.images[i] = img
        self.image = self.images[0]

        # Store Pokemon position
        self.rect = self.image.get_rect()

    def set_velocity_x(self, x):
        """
        Control Pokemon movement in the X direction
        -1 -> Move left
        0 -> No movement
        1 -> Move right
        """
        self.velocity_x = x

    def set_velocity_y(self, y):
        """
        Control Pokemon movement in the Y direction
        -1 -> Move left
        0 -> No movement
        1 -> Move right
        """
        self.velocity_y = y

    def update(self):
        """
        Update sprite position
        """
        # 1 in 20 chance of Pokemon moving around
        rand_move = randint(1, 500)
        if rand_move == 1:
            # Pick random direction
            rand_poke = randint(0, 3)
            self.image = self.images[rand_poke]
