# player.py

# imports
import pygame

class Player:

    # constructor for player object
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    # draw function to draw player (currently image based)
    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    # updateLocation function to update the players location
    def updateLocation(self, x, y):
        self.x = x
        self.y = y

    # getXCoord function to return players x coord
    def getXCoord(self):
        return self.x
    
    # getYCoord function to return players y coord
    def getYCoord(self):
        return self.y