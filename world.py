# world.py

# imports
import pygame

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
