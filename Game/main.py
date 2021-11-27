# Import Modules
import os
import pygame
from pygame.locals import *
import sys
# import sklearn
from character import player
from textbox import Text

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
        # Open a window on the screen
        screen_width=400
        screen_height=500
        self._display_surf = pygame.display.set_mode([screen_width,screen_height])
        pygame.init()
        self.character = player()   # spawn player
        self.textbox = Text() # spawn textbox
        self.character.rect.x = 10   # go to x
        self.character.rect.y = 10  # go to y
        self.player_list = pygame.sprite.Group()
        self.player_list.add(self.character)
        # this is the screen size, initial screen setup
        #self._display_surf = pygame.display.set_mode((400,400), pygame.HWSURFACE)

        self._running = True # is game running

        # this is how you load a Surface object (i.e. an image)
        self._image_surf = self.load_image("assets/sample_map.png", 400, 400)
        # this is how you resize an image
        self._water_tile= self.load_image("assets/water_anim.png", 40, 40)
        # Load textbox image
        self._tb= self.load_image("assets/menubox.png", 400, 100)
        
 
    def on_event(self, event): #if we press the X button that quits
        if event.type == QUIT:
            self._running = False

        if event.type == MOUSEBUTTONDOWN:
            obj = self.get_tile_by_position(event.pos)
            if isinstance(obj, TileWall):
                pass
                # print("This is a wall")
            elif isinstance(obj, TileClickable):
                print(obj.click_message)

        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_LEFT] or event.key == ord("a"):
                self.character.setXVelocity(-1)
            if event.key == pygame.K_RIGHT or event.key == ord("d"):
                self.character.setXVelocity(1)
            if event.key == pygame.K_UP or event.key == ord("w"):
                self.character.setYVelocity(-1)
            if event.key == pygame.K_DOWN or event.key == ord("s"):
                self.character.setYVelocity(1)
            pygame.display.flip()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord("a") or event.key == pygame.K_RIGHT or event.key == ord("d"):
                self.character.setXVelocity(0)
            if event.key == pygame.K_UP or event.key == ord("w") or event.key == pygame.K_DOWN or event.key == ord("s"):
                self.character.setYVelocity(0)
            if event.key == ord("q"):
                pygame.quit()
                sys.exit()

        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                print("Space")
                sample_txt = "Here is our text"
                sample_2 = "please work"
                sample_3 = "ugh work"
                self.text_surface(sample_txt, self._display_surf)
                self.text_surface(sample_2, self._display_surf, "line2")
                self.text_surface(sample_3, self._display_surf, "line3")              

            
    def on_loop(self): #game loop possibly
        pass
        
    def on_render(self):
      # this loads an image onto the surface (you can also load images on top of images)
      # surface_object_to_draw_on.blit(image_to_draw, (x,y)) # (0,0) is top left
        self._display_surf.blit(self._image_surf,(0,0))
        self._display_surf.blit(self._water_tile,(0,0))
        self.player_list.draw(self._display_surf) # draw player

        # For the text box
        self._display_surf.blit(self._tb,(0,400))

        pygame.display.flip() #changes assets

    def on_cleanup(self): # Quit 
        pygame.quit()
 
    def on_execute(self):
            if self.on_init() == False:
                self._running = False

            while self._running:
                for event in pygame.event.get():
                    self.on_event(event)
                self.on_loop()
                self.on_render()
            self.on_cleanup()

    def text_surface(self, text, screen, line = "line1"):
        self.textbox.add_line1(text, screen, pygame.font, line)
 
if __name__ == "__main__" :
    theApp = App() # runs __init__()
    theApp.on_execute() # runs on_init(), then the game loop


