# world.py

# imports
import pygame
from chunk import Chunk

class World:

    # constructor for World object
    def __init__(self):
        self.map = {}

    # ideas
    """
        Most likely, there will have to be a function to draw chunks in proximity to player
        It will have to take player object in
        And only draw the chunks in a predefined proximity to the player
        
        Note: may have to keep track of which chunks are close if looping through all chunks takes too long
        Note: we are going to want to render 11 chunks on x and y at all times (thats all we need to render)
    """

    # createWorld function creates the world by generating chunks and adding them to the world dictionary
    def createWorld(self):

        # loop through to create 100 chunks (for now)
        for yPos in range(10):
            for xPos in range(10):
                targetX = xPos*100
                targetY = yPos*100
                
                # make the new chunk
                c = Chunk(targetX, targetY)

                # generate the chunk
                c.generateChunk()
                
                self.map[str(targetX) + ',' + str(targetY)] = c

