# -------- IMPORTS --------

import pygame
from constants import *

# ---------- END ----------

# ========= MAIN ==========

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    


    while 1:
        screen.fill((0,0,0))
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                return


# ========= END ===========

if __name__ == "__main__":
    main()
