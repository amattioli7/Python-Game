# chunk.py

# ideas:
"""
Each chunk should have a certain amount of tiles
Lets assume a 1000x1000 screen size
If each tile is 10x10, that means the screen will have 100x100 tiles
If we make each chunk 10x10 tiles, each chunk will contain 100 tiles (and be 1/10 of the screen in length and width)

So, we should be able to load in all of the chunks within a certain range of the player (instead of loading in every single chunk each time)

"""

# imports
import pygame
from tile import Tile
from entity import Entity
import noise
import random

class Chunk:

    # constructor for Chunk object
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tiles = []
        self.trees = []


    # getXCoord function to return tiles x coord
    def getXCoord(self):
        return self.x
    
    # getYCoord function to return tiles y coord
    def getYCoord(self):
        return self.y

    # getTiles function to return tiles of chunk
    def getTiles(self):
        return self.tiles

    # generateChunk function that generates 10x10 chunks
    def generateChunk(self):

        # loop to generate 100 tiles per chunk
        for yPos in range(10):
            for xPos in range(10):

                # setting x and y of chunk
                targetX = self.x + (xPos*32)
                targetY = self.y + (yPos*32)

                type = 0
                n = noise.pnoise2(float(targetX)/2000, float(targetY)/2000, octaves=2, lacunarity=2, persistence=0.5)
                #print(n)

                if n < -0.21:
                    type = 1 #water
                elif n < -0.18:
                    type = 2 #sand
                else:
                    # maybe generate a tree
                    chance = random.randint(0, 10)
                    if chance == 1 and targetX < (self.x + 272):
                        self.trees.append(Entity(targetX-16, targetY-112, 0))

                # now make the tile with the x and y
                t = Tile(targetX, targetY, type)
            
                # add the tile to the chunks list of tiles
                self.tiles.append(t)

    # drawEntities function that draws rocks, trees, etc...
    def drawEntities(self, window):
        print("hey")


    