# Import Modules
import os
import pygame
from pygame.locals import *
import sklearn
from character import Player

# if not pg.font:
#     print("Warning, fonts disabled")
# if not pg.mixer:
#     print("Warning, sound disabled")

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
      
    def load_image(self, filename, x_cord, y_cord):
      image = pygame.image.load(filename).convert()
      image = pygame.transform.scale(image,(x_cord, y_cord))
      return image
 
    def on_init(self):
        pygame.init()
        character = player()   # spawn player
        character.rect.x = 10   # go to x
        character.rect.y = 10  # go to y
        player_list = pygame.sprite.Group()
        player_list.add(character)
        # this is the screen size, initial screen setup
        self._display_surf = pygame.display.set_mode((400,400), pygame.HWSURFACE)

        self._running = True # is game running

        # this is how you load a Surface object (i.e. an image)
        self._image_surf = self.load_image("assets/sample_map.png", 400, 400)
        # this is how you resize an image
        self._water_tile= self.load_image("assets/water_anim.png", 40, 40)
        
 
    def on_event(self, event): #if we press the X button that quits
        if event.type == QUIT:
            self._running = False
            
    def on_loop(self): #game loop possibly
        pass
        
    def on_render(self):
      # this loads an image onto the surface (you can also load images on top of images)
      # surface_object_to_draw_on.blit(image_to_draw, (x,y)) # (0,0) is top left
        self._display_surf.blit(self._image_surf,(0,0))
        self._display_surf.blit(self._water_tile,(0,0))
        pygame.display.flip() #changes assets

        
 
    def on_cleanup(self): # Quit 
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App() # runs __init__()
    theApp.on_execute() # runs on_init(), then the game loop

