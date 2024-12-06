import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, SHOT_RADIUS)
        self.color = (255, 255, 255) # white
        self.line_width = 2
        self.rotation = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, self.line_width)

    def update(self, dt):
        self.position += (self.velocity * dt)