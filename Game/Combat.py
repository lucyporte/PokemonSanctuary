import pygame
import random

from utils import load_image


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
        screen.blit(load_image(self.enemy.data.getDownWalkSprite().getFrame1().getPath(), 125, 125), (50, 10))
        # Player HP
        screen.blit(pygame.font.Font.render(pygame.font.Font("assets/fonts/smallest_pixel-7.ttf", 24), f"{str(self.player.hp)}/{str(self.player.max_hp)}", True, (0, 0, 0)), (100, 320))
        # Enemy HP
        screen.blit(pygame.font.Font.render(pygame.font.Font("assets/fonts/smallest_pixel-7.ttf", 24), f"{str(self.enemy.hp)}/{str(self.enemy.max_hp)}", True, (0, 0, 0)), (260, 60))
        # Combat Text
        screen.blit(pygame.font.Font.render(pygame.font.Font("assets/fonts/smallest_pixel-7.ttf", 24), self.combat_text(), True, (0, 0, 0)), (40, 400))
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
            return f"{self.enemy.data.getName()} wins!"
        elif self.enemy.hp <= 0:
            self.finished = True
            return "The Trainer wins!"
