# player.py

# imports
import pygame

class Player:

    # constructor for player object
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.center = (self.x + (self.width/2), self.y + (self.height/2))
        self.image = image
        self.inventory = []
        self.hotbar = []

    # draw function to draw player
    def draw(self, window, scroll):
        window.blit(self.image, (self.x -scroll.x, self.y - scroll.y))

    # handlePlayerMovement function to handle movement keypresses
    def handlePlayerMovement(self, keys_pressed):

        # set temporary values for x, y, and v
        x = 0
        y = 0
        v = 1

        # update the values based on key presses
        if keys_pressed[pygame.K_w]:
            y = -2
        if keys_pressed[pygame.K_s]:
            y = 2
        if keys_pressed[pygame.K_a]:
            x = -2
        if keys_pressed[pygame.K_d]:
            x = 2
        if keys_pressed[pygame.K_LSHIFT]:
            v = 2

        # update the players location
        self.updateLocation((self.x + (x*v)), (self.y + (y*v)))

    # updateLocation function to update the players location
    def updateLocation(self, x, y):
        self.x = x
        self.y = y
        #recalculate center
        self.center = (self.x + (self.width/2), self.y + (self.height/2))


    # getXCoord function to return players x coord
    def getXCoord(self):
        return self.x
    
    # getYCoord function to return players y coord
    def getYCoord(self):
        return self.y