# entity.py

# imports
import pygame
import os

class Entity:

    # constructor for Entity object
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    # getXCoord function to return entity x coord
    def getXCoord(self):
        return self.x
    
    # getYCoord function to return entity y coord
    def getYCoord(self):
        return self.y

    # getType function to return entity type
    def getYCoord(self):
        return self.type