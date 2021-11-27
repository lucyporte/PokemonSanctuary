# Import Modules
import os
import pygame
from pygame.locals import *
# import sklearn
from character import player
from textbox import Text
from tilemap import Map, Tile, TileWall, TileClickable
import mapmanager
import pokemonmanager
from pokemon import pokemon
import sys

# if not pg.font:
#     print("Warning, fonts disabled")
# if not pg.mixer:
#     print("Warning, sound disabled")

tile1 = Tile("assets/tile1.png")
tile2 = TileWall("assets/tile2.png")
tile3 = TileClickable("assets/tile3.png", "Thanks for clicking!")

map_grid_1  = [
[tile1, tile1, tile2, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile2, tile1, tile1, tile1, tile1, tile1, tile1, tile1],
[tile1, tile1, tile2, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile2, tile1, tile1, tile1, tile1, tile1, tile1, tile1],
[tile1, tile2, None, tile1, tile1, tile3, tile1, tile1, tile1, tile1, tile1, tile2, tile1, tile1, tile1, tile1, tile1, tile1, tile1],
[tile1, tile2, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile2, tile1, tile1, tile1, tile1, tile1, tile1, tile1],
[tile1, tile2, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile2, tile1, tile1, tile1, tile1, tile1, tile1, tile1],
[tile2, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile1, tile2, tile1, tile1, tile1, tile1, tile1, tile1, tile1]
]

myMap = Map(map_grid_1)


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._map = myMap

    def load_image(self, filename, x_cord, y_cord):
        image = pygame.image.load(filename).convert()
        image = pygame.transform.scale(image, (x_cord, y_cord))
        return image

    def load_tile_image(self, filename, x_cord, y_cord, x_resize=16, y_resize=16):
        image = pygame.image.load(filename).convert()
        image = pygame.transform.scale(image, (x_resize, y_resize))
        image.set_alpha(0)
        self._display_surf.blit(image, (x_cord, y_cord))
        return image

    def load_map(self, map, resolution=16):
        x = 0
        y = 0
        for t_row in map.tiles:
            for t in t_row:
                if t == None:
                    x += resolution
                    continue
                self.load_tile_image(t.filepath, x, y)
                x += resolution
            y += resolution
            x = 0

    def get_tile_by_position(self, pos):
        if pos[0] > len(self._map.tiles[0] * 16) or pos[1] > len(self._map.tiles * 16):
            print("Clicking outside of map range")
            return False
        x_dex = pos[0] // 16
        y_dex = pos[1] // 16
        print(f"You clicked at ({x_dex}, {y_dex})")
        return self._map.tiles[y_dex][x_dex]

    def on_init(self):
        # Open a window on the screen
        screen_width = 400 
        screen_height = 500
        self._display_surf = pygame.display.set_mode([screen_width, screen_height])
        pygame.init()
        self.character = player()  # spawn player
        self.textbox = Text() # spawn textbox
        self.character.rect.x = 200  # go to x
        self.character.rect.y = 140  # go to y
        self.player_list = pygame.sprite.Group()
        self.player_list.add(self.character)
        self.pokemon = None
        self.pokemon_list = pygame.sprite.Group()
        self.map = mapmanager.getFirstMap()
        self.pokemon_manager = pokemonmanager.getAll()
        # this is the screen size, initial screen setup
        # self._display_surf = pygame.display.set_mode((400,400), pygame.HWSURFACE)

        self._running = True  # is game running

        # this is how you load a Surface object (i.e. an image)
        self._image_surf = self.load_image(self.map.getImage(), 400, 400)
        # this is how you resize an image
        self._water_tile= self.load_image("assets/water_anim.png", 40, 40)
        # Load textbox image
        self._tb= self.load_image("assets/menubox.png", 400, 100)
        # Display the textbox
        self._display_surf.blit(self._tb,(0,400))

    def on_event(self, event):  # if we press the X button that quits
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

            
    def on_loop(self):  # game loop possibly
        self.character.update()
        if self.map.isDisallowedRegion(self.character.rect.x, self.character.rect.y):
            if self.character.movex == 1: 
                self.character.rect.x -= 1
            if self.character.movex == -1: 
                self.character.rect.x += 1
            if self.character.movey == 1: 
                self.character.rect.y -= 1
            if self.character.movey == -1: 
                self.character.rect.y += 1
        if self.map.isDangerRegion(self.character.rect.x, self.character.rect.y):
            self.player_list.empty()
            self.character.dead = True

        if self.character.rect.x == 0 and self.map.getLeft() != None:
            self.map = self.map.getLeft()
            self.on_map_change()
            self.character.rect.x = 390 - self.character.rect.x
        elif self.character.rect.x < 0:
            self.character.rect.x = 0
        if self.character.rect.x == 395 and self.map.getRight() != None:
            self.map = self.map.getRight()
            self.on_map_change()
            self.character.rect.x = 10
        elif self.character.rect.x > 395:
            self.character.rect.x = 395
        if self.character.rect.y == 0 and self.map.getAbove() != None:
            self.map = self.map.getAbove()
            self.on_map_change()
            self.character.rect.y = 385
        elif self.character.rect.y < 0:
            self.character.rect.y = 0
        if self.character.rect.y == 385 and self.map.getBeneath() != None:
            self.map = self.map.getBeneath()
            self.on_map_change()
            self.character.rect.y = 10
        elif self.character.rect.y > 395:
            self.character.rect.y = 395

    def on_render(self):
        # this loads an image onto the surface (you can also load images on top of images)
        # surface_object_to_draw_on.blit(image_to_draw, (x,y)) # (0,0) is top left
        self._display_surf.blit(self._image_surf, (0, 0))
        self.player_list.draw(self._display_surf)  # draw player
        self.pokemon_list.draw(self._display_surf) # draw pokemon
        self.load_map(self._map)
        pygame.display.flip()  # changes assets
        # self.load_map(self._map)

    def on_map_change(self):
        self._image_surf = self.load_image(self.map.getImage(), 400, 400)
        self.pokemon_list.empty()
        new_pokemon = pokemonmanager.getRandom()
        coords = self.map.getRandomPokemonSpawn()
        self.pokemon = pokemon(new_pokemon)
        self.pokemon.rect.x = coords[0]
        self.pokemon.rect.y = coords[1]
        self.pokemon_list.add(self.pokemon)

    def on_cleanup(self):  # Quit
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
        self.textbox.add_text(text, screen, pygame.font, line)

if __name__ == "__main__":
    theApp = App()  # runs __init__()
    theApp.on_execute()  # runs on_init(), then the game loop
