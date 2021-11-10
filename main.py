# main.py

# imports
import pygame
import os
from player import Player
from enemy import Enemy
from world import World
from dataclasses import dataclass

# setting up window
WIDTH, HEIGHT = 1000, 1000
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Game")

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

# load in the tile images
GRASS_IMAGE = pygame.image.load(
                os.path.join('Assets', 'grass.png')
            ).convert()
GRASS = pygame.transform.scale(GRASS_IMAGE, (10, 10))

WATER_IMAGE = pygame.image.load(
                os.path.join('Assets', 'water.png')
            ).convert()
WATER = pygame.transform.scale(WATER_IMAGE, (10, 10))

SAND_IMAGE = pygame.image.load(
                os.path.join('Assets', 'sand.png')
            ).convert()
SAND = pygame.transform.scale(SAND_IMAGE, (10, 10))

# scroll dataclass
@dataclass
class Position:
    x = 0
    y = 0

scroll = Position()

# drawWorld function
def drawWorld(world, scroll):

    # loop through the list of tiles and draw each one
    for chunk in world.map:
        for tile in world.map[chunk].tiles:
            #draw it
            if tile.type == 0: # grass
                WINDOW.blit(GRASS, (tile.x - scroll.x, tile.y - scroll.y))

            elif tile.type == 1: # water
                WINDOW.blit(WATER, (tile.x - scroll.x, tile.y - scroll.y))
            else: # sand
                WINDOW.blit(SAND, (tile.x - scroll.x, tile.y - scroll.y))


# main function
def main():

    # create the world
    W = World()

    # generate the map
    W.createWorld()

    # set up clock variable
    clock = pygame.time.Clock()

    # game loop
    running = True
    while running:

        # set camera scroll values
        scroll.x += (P.x - scroll.x - 500)/20
        scroll.y += (P.y - scroll.y - 500)/20
        
        # cap the fps to 60
        clock.tick(FPS)

        # check each pygame event
        for event in pygame.event.get():
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