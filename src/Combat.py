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
        self.turn = 1
        self.screen = surface
        self.message1 = ""
        self.message2 = ""
        self.message3 = ""
        self.overwrite = False
        self.dead = False

    def update_combat(self):
        """
        Redraws combat GUI
        """
        # Enemy Sprite
        self.screen.blit(load_image(self.enemy.data.get_down_walk_sprite().get_frame_1().get_path(), 125, 125), (50, 10))
        # Player HP
        self.screen.blit(render_text(f"{str(self.player.hp)}/{str(self.player.max_hp)}"), (100, 320))
        # Enemy HP
        self.screen.blit(render_text(f"{str(self.enemy.hp)}/{str(self.enemy.max_hp)}"), (260, 60))
        # Combat Text
        self.update_combat_text()
        if not self.overwrite:
            self.screen.blit(render_text(self.message1), (40, 400))
            self.screen.blit(render_text(self.message2), (40, 420))
            self.screen.blit(render_text(self.message3), (40, 440))
        # Make Update
        pygame.display.update()

    def player_attack(self, action):
        """
        Control turn taking between the player and enemy
        """

        # Player attacks for 5 Damage (80% chance)
        if action == "attack":
            self.overwrite = True
            acc = random.randint(0, 100)
            enemy_acc = random.randint(0,100)
            # player attack
            if acc < 80:
                self.enemy.hp -= 5

                # Combat Text
                self.message1 = "You attack for 5 damage"
                # Make Update
            else:
                self.message1 = "You swing but miss..."

            if enemy_acc < 60:
                self.player.hp -= 5

                # Combat Text
                self.message2 = "They attack for 5 damage"
                # Make Update
            else:
                self.message2 = "They swing but miss..."
        elif action == "defend":
            acc = random.randint(0, 100)
            enemy_acc = random.randint(0,100)
            # player attack
            if acc < 30:
                self.enemy.hp -= 5

                # Combat Text
                self.message1 = "You attack for 3 damage"
                # Make Update
            else:
                self.message1 = "You swing but miss..."

            if enemy_acc < 30:
                self.player.hp -= 5

                # Combat Text
                self.message2 = "They attack for 5 damage"
                # Make Update
            else:
                self.message2 = "They swing but miss..."

        self.screen.blit(render_text(self.message1), (40, 400))
        self.screen.blit(render_text(self.message2), (40, 420))
        pygame.display.update()

        pygame.time.wait(1500)
        self.update_combat_text()
        self.overwrite = False
        self.turn += 1

    def update_combat_text(self):
        """
        Control the text displayed on the combat screen
        """
        if self.player.hp > 0 and self.enemy.hp > 0:
            self.turn += 1
            self.message1 = ""
            self.message2 = ""
            self.message3 = "(A)ttack or (D)efend?"
        elif self.player.hp <= 0:
            self.finished = True
            db.update(self.enemy.data.get_id(), -1)
            self.message1 = "The enemy wins!"
            #self.message1 = f"{self.enemy.data.getName()} wins!"
            self.dead = True
        elif self.enemy.hp <= 0:
            self.finished = True
            db.update(self.enemy.data.get_id(), 1)
            self.message1 = "The Trainer wins!"
