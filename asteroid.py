from circleshape import *
import pygame
import random
from constants import *


gray = (150, 150, 150)

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, gray, self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        vel1 = self.velocity.rotate(random_angle) * 1.2
        vel2 = self.velocity.rotate(-random_angle) * 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vel1

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vel2

        for group in self.containers:
            group.add(asteroid1, asteroid2)
