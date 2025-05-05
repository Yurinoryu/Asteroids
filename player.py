from constants import *
from circleshape import *
import pygame


white = (255,255,255)

class Player(CircleShape):
        def __init__(self, x, y):
            super().__init__(x, y, PLAYER_RADIUS)

            self.rotation = 0


        # Shape of player.
        def triangle(self):
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
            a = self.position + forward * self.radius
            b = self.position - forward * self.radius - right
            c = self.position - forward * self.radius + right
            return [a, b, c]

        def draw(self, screen):
            pygame.draw.polygon(screen, white, self.triangle())

        def rotate(self, dt):
            self.rotation += PLAYER_TURN_SPEED * dt

        def move(self, dt, direction=1):
            forward = pygame.Vector2(0,1).rotate(self.rotation)
            self.position += forward * PLAYER_SPEED * dt * direction

        def update(self, dt):
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                self.rotate(-dt)  # Rotate left by passing negative dt
            if keys[pygame.K_d]:
                self.rotate(dt)   # Rotate right by passing positive dt
            if keys[pygame.K_w]:
                self.move(dt, direction=1)  # Forward
            if keys[pygame.K_s]:
                self.move(dt, direction=-1)  # Backward
