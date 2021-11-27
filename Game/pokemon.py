import pygame
import os
from pygame.locals import *

class pokemon(pygame.sprite.Sprite):
    """
    Spawn a Pokemon
    """

    def __init__(self, obj):
        print(obj)
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0 # move along X
        self.movey = 0 # move along Y
        self.frame = 0 # count frames
        self.images = []
        for i in range(1, 8):
          img = pygame.image.load(obj.getDownWalkSprite().getFrame1().getPath()).convert()
          ALPHA = (0, 0, 0)
          img.convert_alpha()     # optimise
          img.set_colorkey(ALPHA)
          self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
    def setXVelocity(self,x):
      """
      control movement in the x direction
      """
      self.movex = x
    def setYVelocity(self,y):
      """
      control movement in the y direction
      """
      self.movey = y
    def update(self):
        """
        Update sprite position
        """
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        # # moving left
        # if self.movex < 0:
        #     self.frame += 1
        #     if self.frame > 8:
        #         self.frame = 0
        #     self.image = self.images[self.frame//1]

        # # moving right
        # if self.movex > 0:
        #     self.frame += 1
        #     if self.frame > 8:
        #         self.frame = 0
        #     self.image = self.images[self.frame//1]