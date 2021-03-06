# chunk.py

# ideas:
"""
Each chunk should have a certain amount of tiles
Lets assume a 1000x1000 screen size
If each tile is 10x10, that means the screen will have 100x100 tiles
If we make each chunk 10x10 tiles, each chunk will contain 100 tiles (and be 1/10 of the screen in length and width)

So, we should be able to load in all of the chunks within a certain range of the player (instead of loading in every single chunk each time)

"""

# imports
import pygame
from tile import Tile
from entity import Entity
from enemy import Enemy
import noise
import random

class Chunk:

    # constructor for Chunk object
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.tiles = []
        self.entities = []
        self.mobs = []
        self.items = []

        #we can have a flag or bool to show if this chunk is loaded
        #this could be useful for determining whether a chunk that is being loaded in should have a chance for enemies to spawn
        #aka if the spawning occurs when a new chunk is loaded in
        #we will also need a way to deload chunks though

        #or, we just consider spawning enemies on the edge chunks (the ones that are being rendered but that the player cannot see)

    # getXCoord function to return tiles x coord
    def getXCoord(self):
        return self.x
    
    # getYCoord function to return tiles y coord
    def getYCoord(self):
        return self.y

    # getTiles function to return tiles of chunk
    def getTiles(self):
        return self.tiles

    # generateChunk function that generates 10x10 chunks
    def generateChunk(self):

        # loop to generate 100 tiles per chunk
        for yPos in range(10):
            for xPos in range(10):

                # setting x and y of tile
                targetX = self.x + (xPos*32)
                targetY = self.y + (yPos*32)

                type = 0
                n = noise.pnoise2(float(targetX)/2000, float(targetY)/2000, octaves=2, lacunarity=2, persistence=0.5)
                #print(n)

                if n < -0.21:
                    type = 1 #water
                elif n < -0.18:
                    type = 2 #sand
                else:
                    # maybe generate a tree
                    chance = random.randint(0, 10)
                    if chance == 0 and targetX < (self.x + 272):
                        self.entities.append(Entity(targetX-16, targetY-112, 64, 128, 0))
                    elif chance == 1:
                        self.entities.append(Entity(targetX, targetY, 32, 32, 1))

                # random chance to spawn an enemy
                chance = random.randint(0, 250)
                if chance == 0:
                    self.mobs.append(Enemy(targetX, targetY, 50, 50, 0))

                # now make the tile with the x and y
                t = Tile(targetX, targetY, type)
            
                # add the tile to the chunks list of tiles
                self.tiles.append(t)

    # entityClicked function to determine if an entity in the chunk was clicked
    def entityClicked(self, mousePos, playerCenter):
        for entity in self.entities:
            #we clicked on the entity, so remove it
            if entity.hitbox.collidepoint(mousePos):
                #make sure entity is in range of player
                if inRangeOfEntity(entity.center, playerCenter):
                    #get the dropped items from the entity
                    itemList = entity.dropItems()
                    #append this itemList to the chunks itemList
                    self.items.extend(itemList)
                    #remove the entity from the chunk
                    self.entities.remove(entity)

    # itemGrabbed function to determine if an item in the chunk was picked up
    def itemGrabbed(self, player):
        for item in self.items:
            
            #make sure item is in range of player
            if inRangeOfItem(item.center, player.center):
                #add the item to the player inventory (if room!, for now don't check this)
                pickedUp = player.pickUp(item)
                
                #remove the item from the chunk, if picked up
                if pickedUp == True:
                    self.items.remove(item)


# inRangeOfEntity helper function to determine whether the player is in range to hit an entity
def inRangeOfEntity(entityCenter, playerCenter):
    #calculate euclidean distance
    distance = ( ((entityCenter[0] - playerCenter[0])**2) + ((entityCenter[1] - playerCenter[1])**2) )**0.5

    #if the player is 75 pixels or less away from the entity (and this could be changed based on weapon equipped, etc...)
    #or could be changed based on entity type

    if distance < 75:
        return True
    else:
        return False

# inRangeOfItem helper function to determine whether the player is in range to pick up an item
def inRangeOfItem(itemCenter, playerCenter):
    #calculate euclidean distance
    distance = ( ((itemCenter[0] - playerCenter[0])**2) + ((itemCenter[1] - playerCenter[1])**2) )**0.5

    #if the player is 75 pixels or less away from the entity (and this could be changed based on weapon equipped, etc...)
    #or could be changed based on entity type

    if distance < 25:
        return True
    else:
        return False
    
    

    