# -------- IMPORTS --------

import pygame
from constants import *
from player import Player

# ---------- END ----------

# ========= MAIN ==========

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    my_clock = pygame.time.Clock()
    dt = 0
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    


    while 1:

        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        player.update(dt)
        player.draw(screen)
        dt = my_clock.tick(60) / 1000
        pygame.display.flip()




# ========= END ===========

if __name__ == "__main__":
    main()
