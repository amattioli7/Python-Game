# tile.py

# imports
import pygame

class Tile:

    # constructor for Tile object
    def __init__(self, x, y, type, image):
        self.x = x
        self.y = y
        self.type = type
        self.image = image

    # draw function to draw tile
    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    # getXCoord function to return tiles x coord
    def getXCoord(self):
        return self.x
    
    # getYCoord function to return tiles y coord
    def getYCoord(self):
        return self.y

    # getType function to return tiles type
    def getYCoord(self):
        return self.type