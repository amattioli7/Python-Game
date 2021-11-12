# entity.py

# imports
import pygame
import os
from item import Item

class Entity:

    # constructor for Entity object
    def __init__(self, x, y, width, height, type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = type
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.center = (self.x + (self.width/2), self.y + (self.height/2))

    # getXCoord function to return entity x coord
    def getXCoord(self):
        return self.x
    
    # getYCoord function to return entity y coord
    def getYCoord(self):
        return self.y

    # getType function to return entity type
    def getType(self):
        return self.type

    # draws the current entity
    def drawEntity(self, window, scroll, spriteHash):
        if self.type == 0: # tree
            window.blit(spriteHash["tree"], (self.x - scroll.x, self.y - scroll.y))
        elif self.type == 1: # rock
            window.blit(spriteHash["rock"], (self.x - scroll.x, self.y - scroll.y))

    # drops an item when the entity is broken
    def dropItems(self):
        itemList = []

        if self.type == 0: # tree
            #drop wood and maybe sapling eventually?
            #can also randomize a stack size for each tree
            wood = Item(self.x, self.y, 20, 20, 1, 0)
            itemList.append(wood)
        elif self.type == 1: # rock
            #drop rock and maybe flint?
            stone = Item(self.x, self.y, 20, 20, 1, 1)
            itemList.append(stone)
        return itemList
            
