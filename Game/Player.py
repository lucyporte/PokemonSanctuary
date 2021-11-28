import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        # Call superclass constructor
        pygame.sprite.Sprite.__init__(self)

        # Set X and Y velocities for player movement
        self.velocityX = 0
        self.velocityY = 0

        # Set movement animation frames
        self.frame = 0
        self.movement = 0
        self.images = []

        # Set player health and death status
        self.dead = False
        self.hp = 30
        self.max_hp = 30

        # Load player textures
        for i in range(1, 7):
            img = pygame.image.load('Player/player_' + str(i) + '.png').convert()

            # Prevent solid tecture background
            # TODO: Requires optimisation
            ALPHA = (0, 0, 0)
            img.convert_alpha()
            img.set_colorkey(ALPHA)

            self.images.append(img)
        self.image = self.images[0]

        # Store player position
        self.rect = self.image.get_rect()

    def setXVelocity(self, x):
        """
        Control player movement in the X direction
        -1 -> Move left
        0 -> No movement
        1 -> Move right
        """
        self.velocityX = x

    def setYVelocity(self, y):
        """
        Control player movement in the Y direction
        -1 -> Move left
        0 -> No movement
        1 -> Move right
        """
        self.velocityY = y

    def update(self):
        """
        Update sprite position
        """
        # Only move every 20th frame
        if self.movement == 0:
            # Determine new sprite position
            self.rect.x = self.rect.x + self.velocityX
            self.rect.y = self.rect.y + self.velocityY

            # Player moving up
            if self.velocityY < 0:
                # Animate movement
                self.frame += 1
                if self.frame > 7:
                    self.frame = 0
                # Use sprites where player is facing away
                self.image = self.images[self.frame // 4 + 4]

            # Player moving left
            elif self.velocityX < 0:
                # Animate movement
                self.frame += 1
                if self.frame > 7:
                    self.frame = 0
                # Use sprites where player is facing to the left
                self.image = self.images[self.frame // 4 + 2]

            # Player moving down or right
            elif self.velocityX > 0 or self.velocityY > 0:
                # Animate movement
                self.frame += 1
                if self.frame > 7:
                    self.frame = 0
                # Use sprites where player is facing to the left
                self.image = self.images[self.frame // 4]
        
        # Update Counter
        self.movement += 1
        if self.movement > 19:
            self.movement = 0
