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

        # draw the test player
        P.updateLocation(P.getXCoord()+1, P.getYCoord()+1)
        P.draw(WINDOW)

        # update the window
        pygame.display.update()

    
    # close the window
    pygame.quit()

# only run the game if this file is run!
if __name__ == "__main__":
    main()