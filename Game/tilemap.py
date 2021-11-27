import pygame
from pygame.locals import *

class Map:
    def __init__(self, grid):
        self.tiles = grid

class Tile:
  def __init__(self, filepath):
    self.filepath = filepath
    self.blocked = False

class TileWall(Tile):
  def __init__(self, filepath):
    super().__init__(filepath)
    self.blocked = True

class TileClickable(Tile):
  def __init__(self, filepath, message):
    super().__init__(filepath)
    self.blocked = True
    self.click_message = message
