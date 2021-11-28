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
        self.velocityX = 0
        self.velocityY = 0

        # Set movement animation frames
        self.frame = 0

        # Load Pokemon textures
        self.images = [0]*4
        ALPHA = (0, 0, 0)
        for i, sprite in enumerate([obj.getDownWalkSprite(), obj.getLeftWalkSprite(), obj.getRightWalkSprite(), obj.getRightWalkSprite()]):
            img = pygame.image.load(sprite.getFrame1().getPath()).convert()
            img.convert_alpha()     # optimise
            img.set_colorkey(ALPHA)
            self.images[i] = img
        self.image = self.images[0]

        # Store Pokemon position
        self.rect = self.image.get_rect()

    def setXVelocity(self, x):
        """
        Control Pokemon movement in the X direction
        -1 -> Move left
        0 -> No movement
        1 -> Move right
        """
        self.velocityX = x

    def setYVelocity(self, y):
        """
        Control Pokemon movement in the Y direction
        -1 -> Move left
        0 -> No movement
        1 -> Move right
        """
        self.velocityY = y

    def update(self):
        """
        Update sprite position
        """
        # 1 in 20 chance of Pokemon moving around
        randMove = randint(1, 20)
        if randMove == 1:
            # Pick random direction
            randPoke = randint(0, 3)
            self.image = self.images[randPoke]
