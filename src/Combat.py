import pygame
import random

from utils import load_image, render_text
import db

class Combat():
    """
    Controls the combat functionality in the game
    """

    def __init__(self, surface, player, enemy):
        self.player = player
        self.enemy = enemy
        self.combat_surface = load_image("assets/images/battle_bg.png", 400, 500)
        self.finished = False

    def update_combat(self, screen):
        """
        Redraws combat GUI
        """
        # Enemy Sprite
        screen.blit(load_image(self.enemy.data.get_down_walk_sprite().get_frame_1().get_path(), 125, 125), (50, 10))
        # Player HP
        screen.blit(render_text(f"{str(self.player.hp)}/{str(self.player.max_hp)}"), (100, 320))
        # Enemy HP
        screen.blit(render_text(f"{str(self.enemy.hp)}/{str(self.enemy.max_hp)}"), (260, 60))
        # Combat Text
        screen.blit(render_text(self.combat_text()), (40, 400))
        # Make Update
        pygame.display.update()

    def take_turn(self):
        """
        Control turn taking between the player and enemy
        """
        acc = random.randint(0, 100)
        if acc < 80:
            self.enemy.hp -= 5

        acc = random.randint(0, 100)
        if acc < 60:
            self.player.hp -= 2

    def combat_text(self):
        """
        Control the text displayed on the combat screen
        """
        if self.player.hp > 0 and self.enemy.hp > 0:
            return "Mash Space to see who wins!!"
        elif self.player.hp <= 0:
            self.finished = True
            db.update(self.enemy.data.get_id(), -1)
            return f"{self.enemy.data.getName()} wins!"
        elif self.enemy.hp <= 0:
            self.finished = True
            db.update(self.enemy.data.get_id(), 1)
            return "The Trainer wins!"
