# player.py

# imports
import pygame

class Player:

    # constructor for player object
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.center = (self.x + (self.width/2), self.y + (self.height/2))
        self.inventory = [None] * 15 #making an empty inventory with 15 Nones
        self.hotbar = []

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

    # pickUp function to pick up or leave an item if the inventory is full, returns true if picked up
    def pickUp(self, item):

        for index, held in enumerate(self.inventory):

            #if the slot is "empty"
            if held is None:
                self.inventory[index] = item
                return True

            #add the item to existing stack
            elif item.type == held.type:
                    #increase the stack size by the stacksize
                    self.inventory[index].stackSize += item.stackSize
                    return True
        
        return False

    # draws the player
    def drawPlayer(self, window, scroll, spriteHash):
        window.blit(spriteHash["player"], (self.x - scroll.x, self.y - scroll.y))
            
    # getXCoord function to return players x coord
    def getXCoord(self):
        return self.x
    
    # getYCoord function to return players y coord
    def getYCoord(self):
        return self.y