# world.py

# imports
import pygame
from chunk import Chunk
import pickle

class World:

    # constructor for World object
    def __init__(self, xChunks, yChunks, chunkSize):
        self.map = {}
        self.xChunks = xChunks
        self.yChunks = yChunks
        self.chunkSize = chunkSize

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

        # loop through pre-defined chunk sizes and create the world chunk by chunk
        
        for yPos in range(self.yChunks):
            for xPos in range(self.xChunks):
                
                targetX = xPos*self.chunkSize
                targetY = yPos*self.chunkSize
                
                # make the new chunk
                c = Chunk(targetX, targetY, 320, 320)

                # generate the chunk
                c.generateChunk()
                
                self.map[str(targetX) + ',' + str(targetY)] = c

    # this function writes the world out to a file for future use
    def saveWorld(self, filename, player):
        #first, append the player data to the map dict
        self.map['PlayerObject'] = player

        with open(filename, 'wb') as writer:
            pickle.dump(self, writer, protocol=pickle.HIGHEST_PROTOCOL)

