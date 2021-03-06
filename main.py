# main.py

# imports
import pygame
import pickle
import os
from os.path import exists
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

# make a tile hashmap
spriteHash = {}

# test player image
PLAYER_IMAGE = pygame.image.load(
    os.path.join('Assets', 'naruto.png')
)
PLAYER = pygame.transform.scale(PLAYER_IMAGE, (50, 50))

spriteHash['player'] = PLAYER

# test enemy image
ENEMY_IMAGE = pygame.image.load(
    os.path.join('Assets', 'sasuke.png')
)
ENEMY = pygame.transform.scale(ENEMY_IMAGE, (50, 50))

# load in the tile images ------------------------------------------------------------
GRASS = pygame.image.load(
                os.path.join('Assets', 'grass.png')
            ).convert()

spriteHash["grass"] = GRASS

WATER_IMAGE = pygame.image.load(
                os.path.join('Assets', 'water.png')
            ).convert()
WATER = pygame.transform.scale(WATER_IMAGE, (32, 32))

spriteHash["water"] = WATER

SAND_IMAGE = pygame.image.load(
                os.path.join('Assets', 'sand.png')
            ).convert()
SAND = pygame.transform.scale(SAND_IMAGE, (32, 32))

spriteHash["sand"] = SAND

TREE_IMAGE = pygame.image.load(
                os.path.join('Assets', 'tree.png')
            ).convert_alpha()
TREE = pygame.transform.scale(TREE_IMAGE, (64, 128))

spriteHash["tree"] = TREE

ROCK_IMAGE = pygame.image.load(
                os.path.join('Assets', 'rock.png')
            ).convert_alpha()
ROCK = pygame.transform.scale(ROCK_IMAGE, (32, 32))

spriteHash["rock"] = ROCK

WOODITEM_IMAGE = pygame.image.load(
                os.path.join('Assets', 'wooditem.png')
            ).convert_alpha()
WOODITEM = pygame.transform.scale(WOODITEM_IMAGE, (20, 20))

spriteHash["woodItem"] = WOODITEM

STONEITEM_IMAGE = pygame.image.load(
                os.path.join('Assets', 'stoneitem.png')
            ).convert_alpha()
STONEITEM = pygame.transform.scale(STONEITEM_IMAGE, (20, 20))

spriteHash["stoneItem"] = STONEITEM


# scroll dataclass ---------------------------------------------------------------------
@dataclass
class Position:
    x = 0
    y = 0

# drawWorld function (only draw chunks near character!)
def drawWorld(player, world, scroll, clickEventPos):

    # (HEIGHT/CHUNK_SIZE) + 1
    for y in range(5):
        # (WIDTH/CHUNK_SIZE) + 1
        for x in range(7):
            targetX = (x*CHUNK_SIZE) + (int(scroll.x/CHUNK_SIZE) * CHUNK_SIZE)
            targetY = (y*CHUNK_SIZE) + (int(scroll.y/CHUNK_SIZE) * CHUNK_SIZE)

            # making sure we don't render chunks that don't exist
            if targetX < (CHUNK_SIZE*world.xChunks) and targetY < (CHUNK_SIZE*world.yChunks):

                # make the key for the map dict
                targetChunk = str(targetX) + ',' + str(targetY)
                
                #now, check collisions of chunk entities (trees, rocks, etc)
                if clickEventPos is not None:
                    adjustedCoords = (clickEventPos[0] + scroll.x, clickEventPos[1] + scroll.y)
                    world.map[targetChunk].entityClicked(adjustedCoords, player.center)

                # here, we can generate new chunks if we want to have infinite world
                #TODO

                # now, draw the tiles close to the player!
                for tile in world.map[targetChunk].tiles:
                    #draw it
                    tile.drawTile(WINDOW, scroll, spriteHash)

                # after this, draw everything else in the chunk!
                #draw the entities
                for entity in world.map[targetChunk].entities:
                    #draw it
                    entity.drawEntity(WINDOW, scroll, spriteHash)

                #draw the items
                for item in world.map[targetChunk].items:
                    item.drawItem(WINDOW, scroll, spriteHash)
                    #check if the item got picked up
                    world.map[targetChunk].itemGrabbed(player)
                    

               

                    

def drawMobs(player, world, scroll, clickEventPos):

    #we can also change this function to draw the entities as well, so we can have the players and things drawn
    #on top of the world tiles but behind the entities

    # (HEIGHT/CHUNK_SIZE) + 1
    for y in range(5):
        # (WIDTH/CHUNK_SIZE) + 1
        for x in range(7):
            targetX = (x*CHUNK_SIZE) + (int(scroll.x/CHUNK_SIZE) * CHUNK_SIZE)
            targetY = (y*CHUNK_SIZE) + (int(scroll.y/CHUNK_SIZE) * CHUNK_SIZE)

            # making sure we don't render chunks that don't exist
            if targetX < (CHUNK_SIZE*world.xChunks) and targetY < (CHUNK_SIZE*world.yChunks):

                # make the key for the map dict
                targetChunk = str(targetX) + ',' + str(targetY)

                # now, draw the mobs
                for mob in world.map[targetChunk].mobs:

                    #update mob position
                    mob.move(player)

                    #must check if it moved out of chunk (we have to put it in new chunk
                    mobCoords = (mob.x, mob.y)


                    if world.map[targetChunk].hitbox.collidepoint(mobCoords) is False:
                        #print("exited chunk")

                        #get coords of old chunk
                        chunkX = world.map[targetChunk].x
                        chunkY = world.map[targetChunk].y
                        #figure out which direction the enemy went
                        if mob.x < chunkX: # mob went left
                            # move mob into new chunk
                            world.map[str(chunkX-320) + ',' + str(chunkY)].mobs.append(mob)
                        elif mob.x >= (chunkX+320): # mob went right
                            # move mob into new chunk
                            world.map[str(chunkX+320) + ',' + str(chunkY)].mobs.append(mob)
                        elif mob.y < chunkY: # mob went up
                            # move mob into new chunk
                            world.map[str(chunkX) + ',' + str(chunkY-320)].mobs.append(mob)
                        elif mob.y >= (chunkY+320): # mob went down
                            # move mob into new chunk
                            world.map[str(chunkX) + ',' + str(chunkY+320)].mobs.append(mob)

                        # remove mob from old chunk
                        world.map[targetChunk].mobs.remove(mob)
                        
                    

                    if mob.type == 0: #sasuke
                        WINDOW.blit(ENEMY, (mob.x - scroll.x, mob.y - scroll.y))

def handleInventory(player):
        #call the show inventory loop

        #set up all the rects for the inventory
        background = pygame.Rect(WIDTH/4, HEIGHT/4, WIDTH/2, HEIGHT/2)

        rectList = []
        for y in range(3):
            for x in range(5):
                rectSlot = pygame.Rect((background.x+background.width/20) + (x*background.width/5), (background.y+background.height/12) + (y*background.height/3),background.width/10, background.height/6)
                rectList.append(rectSlot)


        #we want to give the inventory 15 slots (3 rows of 5)
        #plus the hotbar of 5 items


        #set up the two variables for swapping
        slot1 = None
        slot2 = None


        exitInventory = False
        while True:
            eventList = pygame.event.get()
            for event in eventList:
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_TAB:
                        # handle other button presses (inventory)
                        exitInventory = True
                        break

                #check if one of the slots was clicked
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    clickEventPos = pygame.mouse.get_pos()
                    for index, slot in enumerate(rectList):
                        # we have clicked on the first item, just set slot 1
                        if slot.collidepoint(clickEventPos) and slot1 is None:
                            slot1 = index
                        # we have clicked on the second item, and need to swap. Also, need to reset slot1 and slt 2 to none after
                        elif slot.collidepoint(clickEventPos) and slot1 is not None:
                            slot2 = index

                            #now, swap the items at slot 1 and slot 2
                            tempItem = player.inventory[slot1]
                            player.inventory[slot1] = player.inventory[slot2]
                            player.inventory[slot2] = tempItem

                            #reset slots to None
                            slot1 = None
                            slot2 = None
                    
            if exitInventory == True:
                break
            else:
                #show the inventory
                pygame.draw.rect(WINDOW, (255, 255, 255), background)

                #make the font object
                font = pygame.font.SysFont(None, 24)

                for index, rect in enumerate(rectList):
                    pygame.draw.rect(WINDOW, (0, 0, 0), rect) 

                    # get the inventory item
                    #if index < len(player.inventory):
                    item = player.inventory[index]

                    #check if item exists, if it does, draw it
                    if item is not None:
                        item.drawItemInventory(WINDOW, spriteHash, rect.x, rect.y)
                        #also draw how many items is in the stack (maybe we can max it at 99?)
                        numberOfItems = "x" + str(item.stackSize)
                        text = font.render(numberOfItems, True, (255, 255, 255))
                        WINDOW.blit(text, (rect.x + 20, rect.y + 20))



                #print(P.inventory)
                # update the screen
                pygame.display.update()

                #we need to allow swaps for the inventory
                #have two variables (clickedOne and clickedTwo)
                #once both are filled, and they arent the same, swap

                        


# main function
def main():

    #init pygame
    pygame.init()

    W = None
    P = None
    scroll = Position()

    # check if a world file is saved or not
    if exists('world.pickle') == False:
        # make a new world
        # create the world (20x20 chunks)
        W = World(20, 20, CHUNK_SIZE)

        # generate the map
        W.createWorld()

        # make a new player
        # create the player object
        P = Player(500, 500, 50, 50)

        print("Made a new world and player!")

    # load the world in from mem
    else:
        with open('world.pickle', 'rb') as reader:

            # read the world in from pickle file
            W = pickle.load(reader)
            
            # read the player and scroll value in from the pickle file, and then remove them from the map dict
            P = W.map.pop('PlayerObject')
            scroll = W.map.pop('ScrollObject')

            print("Loaded a saved world and player!")


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
        

        #print("X: " + str(scroll.x))
        #print("Y: " + str(scroll.y))
        
        # cap the fps to 60
        clock.tick(FPS)

        # check each pygame event
        eventList = pygame.event.get()
        clickEventPos = None
        for event in eventList:
            if event.type == pygame.QUIT:
                #write the world to file
                W.saveWorld('world.pickle', P, scroll)
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clickEventPos = pygame.mouse.get_pos()
            elif event.type == pygame.KEYDOWN:
                #call the inventory function
                if event.key == pygame.K_TAB:
                    # handle other button presses (inventory)
                    handleInventory(P)


        # draw the map
        drawWorld(P, W, scroll, clickEventPos)
        drawMobs(P, W, scroll, clickEventPos)

        # handle the players movement based on WASD
        # get the keys that are pressed
        keys_pressed = pygame.key.get_pressed()
        P.handlePlayerMovement(keys_pressed)

        # draw the test player
        P.drawPlayer(WINDOW, scroll, spriteHash)

        # update the window
        pygame.display.update()

    
    # close the window
    pygame.quit()

# only run the game if this file is run!
if __name__ == "__main__":
    main()