# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    half_screen_width = SCREEN_WIDTH / 2
    half_screen_height = SCREEN_HEIGHT / 2
    player = Player(half_screen_width, half_screen_height)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create Sprit Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Add Player class to Groups
    updatable.add(player)
    drawable.add(player)

    # Add containers class variable
    Player.containers = (updatable, drawable)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000, rect=None)
        # drawable.draw(screen)
        for d in drawable:
            d.draw(screen)
        # player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        # player.update(dt)

if __name__ == "__main__":
    main()
