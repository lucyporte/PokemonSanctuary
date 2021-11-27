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

tile1 = Tile("assets/tile1.png")
tile2 = TileWall("assets/tile2.png")
tile3 = TileClickable("assets/tile3.png", "Thanks for clicking!")

map_grid_1 = [
[tile1, tile1, tile2, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile2, tile1, tile1, tile1, tile1, tile1, tile1, tile1],
[tile1, tile1, tile2, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile2, tile1, tile1, tile1, tile1, tile1, tile1, tile1],
[tile1, tile2, None, tile1, tile1, tile3, tile1, tile1, tile1, tile1, tile1, tile2, tile1, tile1, tile1, tile1, tile1, tile1, tile1],
[tile1, tile2, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile2, tile1, tile1, tile1, tile1, tile1, tile1, tile1],
[tile1, tile2, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile2, tile1, tile1, tile1, tile1, tile1, tile1, tile1],
[tile2, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile2, tile1, tile1, tile1, tile1, tile1, tile1, tile1]
]
