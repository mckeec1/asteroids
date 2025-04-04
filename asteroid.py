import pygame, random

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity=None):
        super().__init__(x,y,radius)
        
        if velocity is not None:
            self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255),(int(self.position.x),int(self.position.y)),self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            vel_one = pygame.math.Vector2.rotate(self.velocity, angle)
            vel_two = pygame.math.Vector2.rotate(self.velocity, -angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            x,y = self.position.x,self.position.y
            Asteroid(x, y, new_radius, vel_one * 1.2)
            Asteroid(x, y, new_radius, vel_two * 1.2)


