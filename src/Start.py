import pygame
import random
from utils import load_image
import TextBox
import db

class Start():
    """
    Controls the menu
    """

    def __init__(self, screen):
        self.start_surface = load_image("assets/images/start.png", 400, 400)
        self.key_pressed = ""
        self.finished = False
        self.display = screen

    def start(self, screen):
        """
        Runs start
        """
        while not self.finished:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    self.finished = True
            

