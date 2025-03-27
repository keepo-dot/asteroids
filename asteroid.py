import circleshape
import pygame
from constants import *


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius, asteroid_field_class):
        super().__init__(x, y, radius)
        self.radius = radius
        self.asteroid_field_class = asteroid_field_class
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    def split(self)
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        spawn_angle = random.uniform(20, 50)
        v1 =  self.velocity.rotate(spawn_angle) * 1.2
        v2 = self.velocity.rotate(spawn_angle * -1) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = self.asteroid_field_class.spawn(self, new_radius, self.position, v1)
        new_asteroid2 = self.asteroid_field_class.spawn(self, new_radius, self.position, v2)
