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

class Chunk:

    # constructor for Chunk object
    def __init__(self, x, y, tiles):
        self.x = x
        self.y = y
        self.tiles = tiles

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
def generateChunk(x, y):

    # creating empty list of chunkData
    chunkData = []

    for yPos in range(10):
        for xPos in range(10):
            targetX = x + (xPos*10)
            targetY = y + (yPos*10)
            # set tile type
            # TODO

            # now make the tile with the x and y
            t = Tile(targetX, targetY, None, None)
            print(targetX, targetY)

    # return the list of 100 tiles (which are a 10x10 grid) for this chunk
    return chunkData


    