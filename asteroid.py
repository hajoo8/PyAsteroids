import random
import circleshape
from constants import *
import pygame

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        #direction = pygame.Vector2(0,-1)
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_angle = random.uniform(20, 50)
            new_velocity1 = self.velocity.rotate(new_angle)
            new_velocity2 = self.velocity.rotate(-new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_ast1.velocity = new_velocity1 * 1.2
            new_ast2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_ast2.velocity = new_velocity2 * 1.2