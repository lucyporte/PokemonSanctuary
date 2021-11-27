import pygame
import os
from pygame import image
from pygame.locals import *
from random import randint

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
        self.images = [0]*4
        ALPHA = (0, 0, 0)
        #randPoke = randint(1, 4)
        img = pygame.image.load(obj.getDownWalkSprite().getFrame1().getPath()).convert()
        img.convert_alpha()     # optimise
        img.set_colorkey(ALPHA)
        self.images[0] = img
        img = pygame.image.load(obj.getLeftWalkSprite().getFrame1().getPath()).convert()
        img.convert_alpha()     # optimise
        img.set_colorkey(ALPHA)
        self.images[1] = img
        img = pygame.image.load(obj.getRightWalkSprite().getFrame1().getPath()).convert()
        img.convert_alpha()     # optimise
        img.set_colorkey(ALPHA)
        self.images[2] = img
        img = pygame.image.load(obj.getRightWalkSprite().getFrame1().getPath()).convert()
        img.convert_alpha()     # optimise
        img.set_colorkey(ALPHA)
        self.images[3] = img
        #pygame.image.load(obj.getRightWalkSprite().getFrame1().getPath()).convert()
        #self.images[3] = pygame.image.load(obj.getUpWalkSprite().getFrame1().getPath()).convert()
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
        randMove = randint(1,20)
        if randMove == 1:
          randPoke = randint(0,3)
          self.image = self.images[randPoke]
