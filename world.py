# world.py

# imports
import pygame
from chunk import generateChunk

class World:

    # constructor for World object
    def __init__(self, chunks):
        self.chunks = chunks

    # ideas
    """
        Most likely, there will have to be a function to draw chunks in proximity to player
        It will have to take player object in
        And only draw the chunks in a predefined proximity to the player
        
        Note: may have to keep track of which chunks are close if looping through all chunks takes too long
    """

def createWorld():
    for yPos in range(10):
        for xPos in range(10):
            targetX = xPos*100
            targetY = yPos*100
            chunkData = generateChunk(targetX, targetY)
            #print(chunkData)
