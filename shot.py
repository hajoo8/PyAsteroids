import circleshape
from constants import *
import pygame

class Shot(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        #direction = pygame.Vector2(0,-1)
        self.position += self.velocity * dt