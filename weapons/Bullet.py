import pygame
import random
import math

class Bullet:
    def __init__(self, x, y, angle, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = 4 + 4 * random.random()
        self.spent = False
        self.angle = angle
    
    def update(self, targets):
        self.size = 3
        self.y -= math.sin(self.angle)
        self.x += math.sin(self.angle) / self.speed

        for t in targets:
            xDistance = abs(self.x - t.x)
            yDistance = abs(self.y - t.y)
            if (xDistance + yDistance) < self.size:
                t.takeDamage()

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x - self.size / 2, self.y - self.size / 2, self.size, self.size))