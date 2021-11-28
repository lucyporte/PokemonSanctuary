import pygame, random

class Combat():

    def load_image(self, filename, x_cord, y_cord):
        image = pygame.image.load(filename).convert()
        image = pygame.transform.scale(image, (x_cord, y_cord))
        return image

    def __init__(self, surface, player, enemy):
        self.player = player
        self.enemy = enemy
        self.combat_surface = self.load_image("assets/images/battle_bg.png", 400, 500)
        self.finished = False


    def update_combat(self, screen):
        enemyImage = pygame.image.load(self.enemy.data.getDownWalkSprite().getFrame1().getPath())
        screen.blit(pygame.transform.scale(enemyImage, (125, 125)), (50, 25))
        screen.blit(pygame.font.Font.render(pygame.font.Font("assets/fonts/smallest_pixel-7.ttf", 24), f"{str(self.player.hp)}/{str(self.player.max_hp)}" , True, (0, 0, 0)), (100, 320))
        screen.blit(pygame.font.Font.render(pygame.font.Font("assets/fonts/smallest_pixel-7.ttf", 24), f"{str(self.enemy.hp)}/{str(self.enemy.max_hp)}", True, (0, 0, 0)), (260, 60))
        screen.blit(pygame.font.Font.render(pygame.font.Font("assets/fonts/smallest_pixel-7.ttf", 24), self.combat_text(), True, (0, 0, 0)), (40, 400))
        pygame.display.update()

    def take_turn(self):
        acc = random.randint(0,100)
        if acc < 80:
            self.enemy.hp -= 5

        acc = random.randint(0,100)
        if acc < 60:
            self.player.hp -= 2

    def combat_text(self):
        if self.player.hp > 0 and self.enemy.hp > 0:
            return "Mash Space to see who wins!!"
        elif self.player.hp <= 0:
            self.finished = True
            return f"{self.enemy.data.getName()} wins!"
        elif self.enemy.hp <= 0:
            self.finished = True
            return "The Trainer wins!"
