from circleshape import *
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = pygame.math.Vector2(velocity)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 0), (int(self.position.x), int(self.position.y)), SHOT_RADIUS)
