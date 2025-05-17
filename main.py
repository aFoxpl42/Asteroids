# Library Imports
from turtle import update
from networkx import draw
import pygame

# Internal Imports / Modules
from asteroid import Asteroid
import asteroid
from asteroidfield import AsteroidField
from constants import *
from circleshape import CircleShape
from player import Player

def main():
    # Initalization of pygame module
    pygame.init()
    # Setting display size of the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Initializion of the player
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    # FPS optimization stuff
    clock = pygame.time.Clock()
    dt = 0
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()
    
    Player.containers = (updateable, drawable)

    while True:
        # Handling of exiting from the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable.update(dt)
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        # Actual Limiting FPS to 60
        dt = clock.tick(60) / 1000
    

if __name__=="__main__":
    main()