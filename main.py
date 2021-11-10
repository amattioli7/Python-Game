# main.py

# imports
import pygame
import os
from player import Player
from enemy import Enemy
from world import World
from dataclasses import dataclass
import random

# setting up window
WIDTH, HEIGHT = 1600, 960
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Game")

# setting chunk size constant
CHUNK_SIZE = 320

# setting hardcoded fps
FPS = 60

# test player image
PLAYER_IMAGE = pygame.image.load(
    os.path.join('Assets', 'naruto.png')
)
PLAYER = pygame.transform.scale(PLAYER_IMAGE, (50, 50))

# create the player object
P = Player(500, 500, PLAYER)

# test enemy image
ENEMY_IMAGE = pygame.image.load(
    os.path.join('Assets', 'sasuke.png')
)
ENEMY = pygame.transform.scale(ENEMY_IMAGE, (50, 50))

# create the enemy object
E = Enemy(300, 300, ENEMY)

# load in the tile images ------------------------------------------------------------
GRASS_IMAGE = pygame.image.load(
                os.path.join('Assets', 'grass.png')
            ).convert()
GRASS = pygame.transform.scale(GRASS_IMAGE, (32, 32))

DGRASS_IMAGE = pygame.image.load(
                os.path.join('Assets', 'dgrass.png')
            ).convert()
DGRASS = pygame.transform.scale(DGRASS_IMAGE, (32, 32))

WATER_IMAGE = pygame.image.load(
                os.path.join('Assets', 'water.png')
            ).convert()
WATER = pygame.transform.scale(WATER_IMAGE, (32, 32))

SAND_IMAGE = pygame.image.load(
                os.path.join('Assets', 'sand.png')
            ).convert()
SAND = pygame.transform.scale(SAND_IMAGE, (32, 32))

TREE_IMAGE = pygame.image.load(
                os.path.join('Assets', 'tree.png')
            ).convert_alpha()
TREE = pygame.transform.scale(TREE_IMAGE, (64, 128))

ROCK_IMAGE = pygame.image.load(
                os.path.join('Assets', 'rock.png')
            ).convert_alpha()
ROCK = pygame.transform.scale(ROCK_IMAGE, (32, 32))

# scroll dataclass ---------------------------------------------------------------------
@dataclass
class Position:
    x = 0
    y = 0

scroll = Position()

# drawWorld function (only draw chunks near character!)
def drawWorld(world, scroll):

    # (HEIGHT/CHUNK_SIZE) + 1
    for y in range(5):
        # (WIDTH/CHUNK_SIZE) + 1
        for x in range(7):
            targetX = (x*CHUNK_SIZE) + (int(scroll.x/CHUNK_SIZE) * CHUNK_SIZE)
            targetY = (y*CHUNK_SIZE) + (int(scroll.y/CHUNK_SIZE) * CHUNK_SIZE)

            # making sure we don't render chunks that don't exist
            if targetX < (CHUNK_SIZE*world.xChunks) and targetY < (CHUNK_SIZE*world.yChunks):

                #here, we could call a function to check collisions of chunk entities (trees, rocks, etc)

                targetChunk = str(targetX) + ',' + str(targetY)
                #print("Chunk: " + targetChunk)

                # here, we can generate new chunks if we want to have infinite world
                #TODO

                # now, draw the tiles close to the player!
                for tile in world.map[targetChunk].tiles:
                    #draw it
                    if tile.type == 0: # grass
                        WINDOW.blit(GRASS, (tile.x - scroll.x, tile.y - scroll.y))
                    elif tile.type == 1: # water
                        WINDOW.blit(WATER, (tile.x - scroll.x, tile.y - scroll.y))
                    elif tile.type == 2: # sand
                        WINDOW.blit(SAND, (tile.x - scroll.x, tile.y - scroll.y))
                    else: # dark grass
                        WINDOW.blit(DGRASS, (tile.x - scroll.x, tile.y - scroll.y))

                # after this, draw everything else in the chunk!
                #world.map[targetChunk].drawEntities(WINDOW)
                for entity in world.map[targetChunk].entities:
                    if entity.type == 0: #tree
                        WINDOW.blit(TREE, (entity.x - scroll.x, entity.y - scroll.y))
                    elif entity.type == 1: #rock
                        WINDOW.blit(ROCK, (entity.x - scroll.x, entity.y - scroll.y))



# main function
def main():

    # create the world (20x20 chunks)
    W = World(20, 20, CHUNK_SIZE)

    # generate the map
    W.createWorld()

    # set up some variables
    xBorder = (CHUNK_SIZE*W.xChunks)-WIDTH
    yBorder = (CHUNK_SIZE*W.yChunks)-HEIGHT

    # set up clock variable
    clock = pygame.time.Clock()

    # game loop
    running = True
    while running:

        # set camera scroll values
        scroll.x += (P.x - scroll.x - (WIDTH/2))/20
        scroll.y += (P.y - scroll.y - (HEIGHT/2))/20

        # make sure scroll doesnt go outside of boundaries
        if scroll.x < 0:
            scroll.x = 0
        elif scroll.x > xBorder:
            scroll.x = xBorder
        if scroll.y < 0:
            scroll.y = 0
        elif scroll.y > yBorder:
            scroll.y = yBorder
        
        # cap the fps to 60
        clock.tick(FPS)

        # check each pygame event
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                running = False

        # draw the map
        drawWorld(W, scroll)

        # handle the players movement based on WASD
        P.handlePlayerMovement()

        # update the enemys movement
        E.move(P)

        # draw the test player
        P.draw(WINDOW, scroll)

        # draw the test enemy
        E.draw(WINDOW, scroll)

        # update the window
        pygame.display.update()

    
    # close the window
    pygame.quit()

# only run the game if this file is run!
if __name__ == "__main__":
    main()