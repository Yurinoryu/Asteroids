import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from Shots import Shot
black = (0,0,0)


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Shot.containers = (shots, updatables, drawables)
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)



    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatables:
            if isinstance(obj, Player):
                obj.update(dt, shots)
            else:
                obj.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.position.distance_to(shot.position) <= (asteroid.radius + shot.radius):
                    asteroid.split()
                    shot.kill()
                    break

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                pygame.quit()
                sys.exit()

        screen.fill(black)
        for obj in drawables:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
