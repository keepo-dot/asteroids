# -------- IMPORTS --------

import pygame
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *
import sys
from shot import Shot

# ---------- END ----------

# ========= MAIN ==========

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    my_clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)


    while 1:

        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        updatable.update(dt)
        for thing in asteroids:
            for thing2 in player.shots:
                if thing2.collision(thing):
                    thing.kill()
                    thing2.kill()
            if player.collision(thing) == True:
                sys.exit("Game over!")

        for thing in drawable:
            thing.draw(screen)
        dt = my_clock.tick(60) / 1000
        pygame.display.flip()




# ========= END ===========

if __name__ == "__main__":
    main()
