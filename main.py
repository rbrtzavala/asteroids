# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    half_screen_width = SCREEN_WIDTH / 2
    half_screen_height = SCREEN_HEIGHT / 2
    player = Player(half_screen_width, half_screen_height)
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create Sprit Groups
    asteroids = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    

    # Add Player class to Groups
    drawable.add(player)
    updatable.add(player)

    # Add containers class variable
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (drawable, updatable)
    Shot.containers = (shots, updatable, drawable)
    
    AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000, rect=None)

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collision(player):
                sys.exit("Game over!")
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.kill()
                    shot.kill()
                

if __name__ == "__main__":
    main()
