import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius=SHOT_RADIUS, velocity=None):
        super().__init__(x, y, radius)
        if velocity is not None:
            self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255, 255), (int(self.position.x), int(self.position.y)),self.radius, 2)

    def update (self, dt):
        self.position += self.velocity * dt
