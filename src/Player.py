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
        self.velocity_x = 0
        self.velocity_y = 0

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
            img = pygame.image.load('assets/images/player/player_' + str(i) + '.png').convert()

            # Prevent solid tecture background
            # TODO: Requires optimisation
            ALPHA = (0, 0, 0)
            img.convert_alpha()
            img.set_colorkey(ALPHA)

            self.images.append(img)
        self.image = self.images[0]

        # Store player position
        self.rect = self.image.get_rect()

    def set_x_velocity(self, x):
        """
        Control player movement in the X direction
        -1 -> Move left
        0 -> No movement
        1 -> Move right
        """
        self.velocity_x = x

    def set_y_velocity(self, y):
        """
        Control player movement in the Y direction
        -1 -> Move left
        0 -> No movement
        1 -> Move right
        """
        self.velocity_y = y

    def update(self):
        """
        Update sprite position
        """
        # Only move every 20th frame
        if self.movement == 0:
            # Determine new sprite position
            self.rect.x = self.rect.x + self.velocity_x
            self.rect.y = self.rect.y + self.velocity_y

            # Player moving up
            if self.velocity_y < 0:
                # Animate movement
                self.frame += 1
                if self.frame > 7:
                    self.frame = 0
                # Use sprites where player is facing away
                self.image = self.images[self.frame // 4 + 4]

            # Player moving left
            elif self.velocity_x < 0:
                # Animate movement
                self.frame += 1
                if self.frame > 7:
                    self.frame = 0
                # Use sprites where player is facing to the left
                self.image = self.images[self.frame // 4 + 2]

            # Player moving down or right
            elif self.velocity_x > 0 or self.velocity_y > 0:
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
