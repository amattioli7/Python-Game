# tile.py

# imports
import pygame
import os

class Tile:

    # constructor for Tile object
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    # getXCoord function to return tiles x coord
    def getXCoord(self):
        return self.x
    
    # getYCoord function to return tiles y coord
    def getYCoord(self):
        return self.y

    # getType function to return tiles type
    def getYCoord(self):
        return self.type

    def drawTile(self, window, scroll, tileHash):
        if self.type == 0: # grass
            window.blit(tileHash["grass"], (self.x - scroll.x, self.y - scroll.y))
        elif self.type == 1: # water
            window.blit(tileHash["water"], (self.x - scroll.x, self.y - scroll.y))
        elif self.type == 2: # sand
            window.blit(tileHash["sand"], (self.x - scroll.x, self.y - scroll.y))
