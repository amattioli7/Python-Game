# main.py

# imports
import pygame
import os
from player import Player

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

P = Player(50, 50, PLAYER)

# main function
def main():

    # set up clock variable
    clock = pygame.time.Clock()

    # game loop
    running = True
    while running:

        # cap the fps to 60
        clock.tick(FPS)

        # check each pygame event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the window with white fill
        WINDOW.fill((255, 255, 255))

        # get the keys that are pressed
        keys_pressed = pygame.key.get_pressed()

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
        P.updateLocation((P.getXCoord() + (x*v)), (P.getYCoord() + (y*v)))
    

        # draw the test player
        P.draw(WINDOW)

        # update the window
        pygame.display.update()

    
    # close the window
    pygame.quit()

# only run the game if this file is run!
if __name__ == "__main__":
    main()