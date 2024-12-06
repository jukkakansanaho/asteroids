import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    color = (0, 0, 0) # black
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Create two groups and add Player to them
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Player - spwan in the middle of the screen
    # x = SCREEN_WIDTH / 2
    # y = SCREEN_HEIGHT / 2
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all objects        
        screen.fill(color)  # fill screen bg
        # Draw items in drawable group
        for item in drawable:
            item.draw(screen) # draw player
        # Update items in updatable group
        for item in updatable:
            item.update(dt)
        # Update items in asteroids group
        for item in asteroids:
            item.update(dt)
        for item in shots:
            item.update(dt)
        
        # Check Asteroid-Player collisions
        for item in asteroids:
            if item.is_colliding(player):
                print(f"Game Over!")
                return
        pygame.display.flip()   # refresh screen
        
        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()