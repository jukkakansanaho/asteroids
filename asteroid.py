import pygame
from circleshape import CircleShape
from constants import  *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = (255, 255, 255) # white
        self.line_width = 2
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, self.line_width)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        #print(f"Asteroid_old (pos,rad,velo): {self.position},{self.radius},{self.velocity}")
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        vect1 = self.velocity.rotate(random_angle)
        vect2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vect1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vect2 * 1.2
        #print(f"Asteroid_new_1 (pos,rad,velo): {asteroid1.position},{asteroid1.radius},{asteroid1.velocity}")
        #print(f"Asteroid_new_2 (pos,rad,velo): {asteroid2.position},{asteroid2.radius},{asteroid2.velocity}")
