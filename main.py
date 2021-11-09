# main.py

# imports
import pygame

# setting up window
WIDTH, HEIGHT = 1000, 1000
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# main function
def main():

    # game loop
    running = True
    while running:

        # check each pygame event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    # close the window
    pygame.quit()

# only run the game if this file is run!
if __name__ == "__main__":
    main()