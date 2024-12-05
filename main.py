import pygame as pg
from constants import *
from player import Player

def main():
    pg.init()
    color = (0, 0, 0) # black
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0

    # Create two groups and add Player to them
    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    Player.containers = (updatable, drawable)

    # Player - spwan in the middle of the screen
    # x = SCREEN_WIDTH / 2
    # y = SCREEN_HEIGHT / 2
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
                
        screen.fill(color)  # fill screen bg
        # Draw items in drawable group
        for item in drawable:
            item.draw(screen) # draw player
        # Update items in updatable group
        for item in updatable:
            item.update(dt)
        
        pg.display.flip()   # refresh screen
        
        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()