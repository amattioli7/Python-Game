# enemy.py

# imports
import pygame
import random

class Enemy:

    # constructor for enemy object
    def __init__(self, x, y, width, height, type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.center = (self.x + (self.width/2), self.y + (self.height/2))
        self.type = type

    # draw function to draw enemy
    def draw(self, window, image, scroll):
        window.blit(image, (self.x - scroll.x, self.y - scroll.y))

    # move function to make the enemy follow the player
    def move(self, player):

        if inRangeOfPlayer(self.center, player.center):

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
        
        #else
            #wander
            

        
    # updateLocation function to update the enemys location
    def updateLocation(self, x, y):
        self.x = x
        self.y = y

        #update center
        self.center = (self.x + (self.width/2), self.y + (self.height/2))

    # getXCoord function to return enemys x coord
    def getXCoord(self):
        return self.x
    
    # getYCoord function to return enemys y coord
    def getYCoord(self):
        return self.y

# inRangeOfPlayer helper function to determine whether the enemy is in range of the player
def inRangeOfPlayer(enemyCenter, playerCenter):
    #calculate euclidean distance
    distance = ( ((enemyCenter[0] - playerCenter[0])**2) + ((enemyCenter[1] - playerCenter[1])**2) )**0.5

    #if the player is 75 pixels or less away from the entity (and this could be changed based on weapon equipped, etc...)
    #or could be changed based on entity type

    if distance < 200:
        return True
    else:
        return False