# item.py

# imports
import pygame
import os

class Item:

    # constructor for Item object
    def __init__(self, x, y, width, height, stackSize, type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.stackSize = stackSize
        self.type = type
        #self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.center = (self.x + (self.width/2), self.y + (self.height/2)) #we can probably use distance for pickups

    # draws the current item
    def drawItem(self, window, scroll, spriteHash):
        if self.type == 0: # woodItem
            window.blit(spriteHash["woodItem"], (self.x - scroll.x, self.y - scroll.y))