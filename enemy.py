# enemy.py

# imports
import pygame

class Enemy:

    # constructor for enemy object
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    # draw function to draw enemy
    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def move(self, player):

        x = 0
        y = 0

        if player.getXCoord() < self.x:
            x = -1

        elif player.getXCoord() > self.x:
            x = 1

        if player.getYCoord() < self.y:
            y = -1

        elif player.getYCoord() > self.y:
            y = 1

        # update the enemys location
        self.updateLocation((self.x + x), (self.y + y))

    # updateLocation function to update the enemys location
    def updateLocation(self, x, y):
        self.x = x
        self.y = y

    # getXCoord function to return enemys x coord
    def getXCoord(self):
        return self.x
    
    # getYCoord function to return enemys y coord
    def getYCoord(self):
        return self.y