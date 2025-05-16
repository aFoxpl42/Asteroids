# Library Imports
import pygame

# Internal Imports / Modules
from constants import *

def main():
    # Initalization of pygame module
    pygame.init()
    # Setting display size of the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # Handling of exiting from the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        screen.fill("black")
        pygame.display.flip()
    

if __name__=="__main__":
    main()