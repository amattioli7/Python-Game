# player.py

# imports
import pygame

class Player:

    # constructor for player object
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))