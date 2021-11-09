# tile.py

# imports
import pygame
import os

GRASS_IMAGE = pygame.image.load(
                os.path.join('Assets', 'grass.png')
            )
GRASS = pygame.transform.scale(GRASS_IMAGE, (10, 10))

WATER_IMAGE = pygame.image.load(
                os.path.join('Assets', 'water.png')
            )
WATER = pygame.transform.scale(WATER_IMAGE, (10, 10))

SAND_IMAGE = pygame.image.load(
                os.path.join('Assets', 'sand.png')
            )
SAND = pygame.transform.scale(SAND_IMAGE, (10, 10))




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

    # drawTile function to draw a tile
    def drawTile(self, window):

        #these values will be temporary
        print("Here!")

        #grass
        if self.type == 0:
            window.blit(GRASS, (self.x, self.y))
        #water
        elif self.type == 1:
            window.blit(WATER, (self.x, self.y))

        #sand
        else:
            window.blit(SAND, (self.x, self.y))
