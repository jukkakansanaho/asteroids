import pygame as pg
import sys
from constants import *

def main():
    pg.init()
    color = (0, 0, 0) # black
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
                
        screen.fill(color)
        pg.display.flip()
        
        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()