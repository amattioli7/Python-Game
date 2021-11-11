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
import noise
import random

class Chunk:

    # constructor for Chunk object
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tiles = []
        self.entities = []


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
                    self.entities.remove(entity)

# inRangeOfEntity helper function to determine whether the player is in range to hit an entity
def inRangeOfEntity(entityCenter, playerCenter):
    #calculate euclidean distance
    distance = ( ((entityCenter[0] - playerCenter[0])**2) + ((entityCenter[1] - playerCenter[1])**2) )**0.5
    #print("Entity Center: " + str(entityCenter[0]) + ',' + str(entityCenter[1]))
    #print("Player Center: " + str(playerCenter[0]) + ',' + str(playerCenter[1]))
    #print("Distance: " + str(distance))

    #if the player is 75 pixels or less away from the entity (and this could be changed based on weapon equipped, etc...)
    if distance < 75:
        return True
    else:
        return False
    
    

    