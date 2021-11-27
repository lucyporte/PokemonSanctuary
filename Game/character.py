import pygame
import os
from pygame.locals import *

class player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0 # move along X
        self.movey = 0 # move along Y
        self.frame = 0 # count frames
        self.images = []
        for i in range(1, 8):
          img = pygame.image.load('Game/Player/player_' + str(i) + '.png').convert()
          ALPHA = (0, 0, 0)
          img.convert_alpha()     # optimise
          img.set_colorkey(ALPHA)
          self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
    def setXVelocity(self,x):
      """
      control player movement in the x direction
      """
      self.movex = x
    def setYVelocity(self,y):
      """
      control player movement in the y direction
      """
      self.movey = y
    def update(self):
        """
        Update sprite position
        """
        ani = 4
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 8:
                self.frame = 0
            self.image = self.images[self.frame//4]

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 8:
                self.frame = 0
            self.image = self.images[self.frame//4]