import pygame
from constants import *
from player import *
from asteroidfield import *
from shot import *

import sys

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots,updatable,drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)
    asteroid_field = AsteroidField()

    dt = 0
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if(shot.check_collision(asteroid)):
                    asteroid.split()
                    shot.kill()

                
            coll_status = asteroid.check_collision(player)
            if coll_status:
                print("Game Over")
                sys.exit(0)
        screen.fill("black")
        for drawabl in drawable:
            drawabl.draw(screen)
        pygame.display.flip()
        delta_time = clock.tick(60)
        dt = delta_time / 1000

if __name__ == "__main__":
    main()
