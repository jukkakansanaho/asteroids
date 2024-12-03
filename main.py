import pygame as pg
import sys
from constants import *

def main():
    pg.init()
    color = (0, 0, 0) # black
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
                #pg.quit()
                #sys.exist()
        screen.fill(color)
        pg.display.flip()

if __name__ == "__main__":
    main()